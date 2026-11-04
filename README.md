# Machine Learning from Scratch

This repository contains the runnable companion code for the Machine Learning
from Scratch tutorial series. Each coding tutorial provides equivalent tracks
for NumPy, MLX, and base R while sharing the same frozen inputs and expected
results.

The framework environments are defined once under [`environments/`](environments/README.md).
They can run locally, through Docker Compose, or as isolated VS Code Dev
Containers.

## Choose an environment

### VS Code Dev Containers

Install Docker and the VS Code **Dev Containers** extension. Open this
repository in VS Code, run **Dev Containers: Reopen in Container** from the
Command Palette, and select one of the repository configurations:

- **ML from Scratch — NumPy**
- **ML from Scratch — MLX (Linux CPU)**
- **ML from Scratch — Base R**

Each configuration opens the full repository at `/workspace` and installs the
language extensions appropriate for that track. One VS Code window connects to
one framework container at a time.

The MLX container uses the Linux CPU backend. On an Apple silicon Mac, use the
native MLX environment when checking Metal device behavior or performance.

### Docker Compose

Build all three images from the repository root:

```bash
docker compose build
```

Run the environment checks independently:

```bash
docker compose run --rm numpy python environments/numpy/smoke_test.py
docker compose run --rm mlx python environments/mlx/smoke_test.py
docker compose run --rm r Rscript environments/r/smoke_test.R
```

### Local environments

NumPy and MLX use separate `uv` projects and lockfiles. `uv run` creates and
updates the corresponding `.venv` automatically.

```bash
uv sync --project environments/numpy --locked
uv run --project environments/numpy python environments/numpy/smoke_test.py
```

On an Apple silicon Mac with macOS 14 or newer, create the native MLX
environment with:

```bash
uv sync --project environments/mlx --locked
uv run --project environments/mlx python environments/mlx/smoke_test.py
```

The base R track uses an `renv` project under `environments/r` to pin ggplot2,
knitr, and rmarkdown for Quarto notebooks. Restore it once, then run the smoke
check from that project directory:

```bash
cd environments/r
Rscript -e 'renv::restore(prompt = FALSE)'
Rscript smoke_test.R
cd ../..
```

The container pins the reference R version and restores the same lockfile.
Numerical implementations remain in base R; ggplot2 is used only for
visualization. The Base R container also pins the Quarto CLI.

See [`environments/README.md`](environments/README.md) for version choices,
container behavior, and update instructions.

## Available supporting code

- [Tutorial 2: vectors, matrices, and linear algebra](tutorials/02-linear-algebra/README.md)
