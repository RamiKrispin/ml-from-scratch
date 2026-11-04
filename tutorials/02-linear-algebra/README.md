# Tutorial 2 supporting code: vectors, matrices, and linear algebra

Choose one notebook track. NumPy and MLX run in Jupyter; base R runs as a
Quarto notebook. All three load the same fixtures, compute the same reference
results, demonstrate a shape error, and show a directly labeled matrix-
multiplication diagram.

Python visuals use plotnine and R visuals use ggplot2. The diagram is rendered
inline, so the repository does not store three copies of the same image.

## Files

- `numpy.ipynb`: Jupyter notebook using NumPy.
- `mlx.ipynb`: Jupyter notebook using MLX.
- `r.qmd`: Quarto notebook using base R.
- `python_helpers.py`: shared Python fixture-loading and plotnine helpers.
- `r_helpers.R`: R fixture-loading, checking, and ggplot2 helpers.
- `../../data/fixtures/linear-algebra/`: shared inputs and expected results.

The helper files hide repetitive setup only. The mathematical operations stay
visible in each notebook.

## Run one track

Run setup commands from the repository root. Then execute every cell in the
notebook you selected.

### NumPy in Jupyter

```bash
uv sync --project environments/numpy --locked
uv run --project environments/numpy \
  jupyter lab tutorials/02-linear-algebra/numpy.ipynb
```

### MLX in Jupyter

On Apple silicon, the local environment uses the Metal backend. On another
platform, use the MLX Dev Container or Docker service.

```bash
uv sync --project environments/mlx --locked
uv run --project environments/mlx \
  jupyter lab tutorials/02-linear-algebra/mlx.ipynb
```

MLX 0.32.4 runs the small `linalg.solve` example on an explicit CPU stream
because its GPU backend does not implement that operation. Other operations use
the selected default device.

### Base R in Quarto

Install Quarto, then restore the isolated R package library once:

```bash
cd environments/r
Rscript -e 'renv::restore(prompt = FALSE)'
cd ../..
```

Open `tutorials/02-linear-algebra/r.qmd` in a Quarto-aware editor, or preview it
from the repository root:

```bash
RENV_PROJECT="$PWD/environments/r" \
R_PROFILE_USER="$PWD/environments/r/.Rprofile" \
  quarto preview tutorials/02-linear-algebra/r.qmd
```

The Base R Dev Container includes Quarto and the Quarto VS Code extension.

## Docker and Dev Containers

The VS Code Dev Container configurations provide Jupyter support for NumPy and
MLX and Quarto support for base R. After building the images, command-line
execution checks are also available:

```bash
docker compose build numpy mlx r

docker compose run --rm numpy sh -c \
  'cd tutorials/02-linear-algebra && jupyter nbconvert --execute --to notebook --output-dir /tmp numpy.ipynb'

docker compose run --rm mlx sh -c \
  'cd tutorials/02-linear-algebra && jupyter nbconvert --execute --to notebook --output-dir /tmp mlx.ipynb'

docker compose run --rm r \
  quarto render tutorials/02-linear-algebra/r.qmd --output-dir /tmp/t02-r
```

The MLX container verifies CPU correctness. Native Apple silicon remains the
reference for Metal device behavior.

## Expected checks

A complete run shows:

- feature-matrix shape `3 × 2` and coefficient length `2`;
- predictions `-1.5, -2.5, -3.5`;
- coefficient norm approximately `1.118033988750`;
- Gram matrix `[[35, 44], [44, 56]]`;
- linear-system solution `2, 3`;
- an expected incompatible-shape error;
- an inline, directly labeled matrix-multiplication diagram; and
- an `All T02 ... checks passed.` message.

Python also shows row-wise broadcasting for `X + beta`. R displays both its
column-major recycling result and the intended column-wise result created with
`sweep()`. Numerical comparisons use absolute and relative tolerances of
`1e-6`.
