# Set up a framework environment

The tutorial series has three independent implementation tracks: NumPy, MLX,
and base R. Only one environment is required to follow a tutorial. Each track
has its own dependency definition and container so installing one does not
require installing the other two.

Run every command in this guide from the repository root.

## Environment options

There are three ways to use a track:

1. **VS Code Dev Container:** the simplest reproducible setup when Docker and
   the VS Code Dev Containers extension are available.
2. **Local environment:** useful for normal development and required for MLX
   access to the Apple silicon GPU.
3. **Docker Compose:** useful for command-line checks without opening VS Code.

The reference environments are:

| Track | Local isolation | Container backend | Reference runtime |
| --- | --- | --- | --- |
| NumPy | Dedicated `uv` project | Linux CPU | Python 3.12, NumPy 2.4.6, and plotnine 0.15.8 |
| MLX | Dedicated `uv` project | Linux CPU | Python 3.12, MLX 0.32.4, and plotnine 0.15.8 |
| Base R | Dedicated `renv` project | Linux CPU | R 4.6.1, ggplot2 4.0.3, and Quarto 1.10.19 |

## Option 1: VS Code Dev Containers

Install these prerequisites:

- [Docker Desktop](https://www.docker.com/products/docker-desktop/) or another
  Docker installation compatible with Docker Compose.
- [Visual Studio Code](https://code.visualstudio.com/).
- The [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).

Open the repository folder in VS Code. From the Command Palette, run
**Dev Containers: Reopen in Container**, then select one environment:

- **ML from Scratch — NumPy**
- **ML from Scratch — MLX (Linux CPU)**
- **ML from Scratch — Base R**

VS Code builds the selected image, mounts the repository at `/workspace`, and
installs the appropriate Jupyter or R/Quarto extensions. Open a new VS Code
window to work in another framework container.

After the container opens, verify the selected environment:

```bash
# NumPy container
python environments/numpy/smoke_test.py

# MLX container
python environments/mlx/smoke_test.py

# Base R container
Rscript environments/r/smoke_test.R
```

The MLX Dev Container uses the Linux CPU backend. It checks that an MLX example
runs and produces the expected numerical result, but it does not test Apple's
Metal backend.

## Option 2: Local environments

### NumPy

The NumPy track uses [`uv`](https://docs.astral.sh/uv/) to manage Python 3.12,
the project virtual environment, and the committed lockfile.

Install `uv`, then synchronize the environment:

```bash
uv sync --project environments/numpy --locked
```

Run the verification script inside the environment:

```bash
uv run --project environments/numpy \
  python environments/numpy/smoke_test.py
```

The check should report NumPy 2.4.6, the `float64` dtype, and a dot product of
`32.0`.

Open a NumPy tutorial notebook in JupyterLab with the same environment:

```bash
uv run --project environments/numpy jupyter lab path/to/example.ipynb
```

Manual activation is optional. When an activated shell is preferred, run:

```bash
source environments/numpy/.venv/bin/activate
```

### MLX

The native MLX environment requires Apple silicon and macOS 14 or newer. It is
the reference environment for Metal device behavior and any performance
observation. On another platform, use the MLX Dev Container or Docker Compose
service for a Linux CPU run.

Install `uv`, then synchronize the MLX environment:

```bash
uv sync --project environments/mlx --locked
```

Run the verification script:

```bash
uv run --project environments/mlx \
  python environments/mlx/smoke_test.py
```

On a supported Mac, the check should report MLX 0.32.4, `Device(gpu, 0)`, the
`mlx.core.float32` dtype, and a dot product of `32.0`.

Open an MLX tutorial notebook with:

```bash
uv run --project environments/mlx jupyter lab path/to/example.ipynb
```

Manual activation is optional:

```bash
source environments/mlx/.venv/bin/activate
```

The MLX dependency is selected by platform. The lockfile installs native `mlx`
on Apple silicon macOS and `mlx[cpu]` on Linux.

### Base R

Base R performs the numerical work, while ggplot2 provides the series'
visualizations. Quarto executes the R notebooks through knitr. The
`environments/r` project uses `renv` to isolate and pin the R package library.
Install R, Quarto, and the `renv` package locally, then restore the project
once:

```bash
cd environments/r
Rscript -e 'renv::restore(prompt = FALSE)'
```

Run the verification script while the R project is active:

```bash
Rscript smoke_test.R
```

The check reports the local R version and platform, followed by a dot product.
Return to the repository root to open a Quarto notebook:

```bash
cd ../..
RENV_PROJECT="$PWD/environments/r" \
R_PROFILE_USER="$PWD/environments/r/.Rprofile" \
  quarto preview tutorials/path/to/example.qmd
```

The lockfile records ggplot2, knitr, rmarkdown, and their transitive
dependencies. Numerical implementations continue to use base R rather than a
model-fitting package.

To reproduce the exact reference R 4.6.1 runtime now, use the Base R container.

## Option 3: Docker Compose

Build all framework images:

```bash
docker compose build
```

Run each track's verification script independently:

```bash
docker compose run --rm numpy \
  python environments/numpy/smoke_test.py

docker compose run --rm mlx \
  python environments/mlx/smoke_test.py

docker compose run --rm r \
  Rscript environments/r/smoke_test.R
```

The NumPy and MLX containers use their locked virtual environments. The MLX
container should report `Device(cpu, 0)`, while the R container should report R
4.6.1. Each temporary container is removed after its command finishes.

Execute a tutorial notebook from a temporary container:

```bash
docker compose run --rm numpy sh -c \
  'cd path/to/tutorial && jupyter nbconvert --execute --to notebook --output-dir /tmp example.ipynb'
docker compose run --rm mlx sh -c \
  'cd path/to/tutorial && jupyter nbconvert --execute --to notebook --output-dir /tmp example.ipynb'
docker compose run --rm r quarto render path/to/example.qmd --output-dir /tmp/rendered
```

## Environment files

The environment definitions are stored separately:

```text
environments/
├── numpy/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── smoke_test.py
│   └── uv.lock
├── mlx/
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── smoke_test.py
│   └── uv.lock
└── r/
    ├── .Rprofile
    ├── DESCRIPTION
    ├── Dockerfile
    ├── renv.lock
    ├── renv/
    │   ├── activate.R
    │   └── settings.json
    └── smoke_test.R
```

The Python lockfiles are committed. A host `.venv` must not be copied into a
container because virtual environments contain platform-specific paths and
binaries. Each Docker build recreates its environment from the corresponding
lockfile.

## Updating an environment

Update one track at a time and rerun its smoke check plus all existing examples
for that track. For Python, change the constraint in the track's
`pyproject.toml`, regenerate only that track's `uv.lock`, and rebuild its image.
For R, change the Docker base reference or Quarto version and verify the
notebooks against the matching local R release. Update a base image's tag and
digest together; update Quarto's package checksum with its version.

Record Linux container results separately from native results. For MLX, always
record the selected device when reporting runtime or performance behavior.
