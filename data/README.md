# Public datasets

This directory contains frozen dataset snapshots shared by the NumPy, MLX,
and base R tutorial tracks. Tutorial code should read these local files rather
than download data at runtime. Fixed train, validation, and test indices will
be added separately when the relevant tutorial briefs define them.

## Tutorial fixtures

Path: `fixtures/linear-algebra/`

Tutorial 2 uses a synthetic three-by-two feature matrix, a two-value
coefficient vector, a two-equation system, and flattened expected results.
The fixture README records the file roles and tolerance. These values are
teaching inputs rather than a fitted model or a real dataset.

## Regression: Auto MPG

Path: `regression/auto-mpg/`

- `auto-mpg.csv` is the cross-track CSV used by tutorial code.
- `raw/auto-mpg.data` is the official UCI data file.
- `raw/auto-mpg.names` is the accompanying UCI metadata file.

The dataset has 398 observations. The target is `mpg`; the predictors are
`cylinders`, `displacement`, `horsepower`, `weight`, `acceleration`,
`model_year`, and `origin`. `car_name` is retained as an identifier.
`horsepower` has six missing values.

The CSV was created from the official data file by adding the documented
column names and replacing the `?` missing-value marker in `horsepower` with
an empty CSV field. Row order and numeric values were otherwise preserved.

Source: [UCI Machine Learning Repository — Auto MPG](https://archive.ics.uci.edu/dataset/9/auto%2Bmpg)

Citation: Quinlan, R. (1993). *Auto MPG* [Dataset]. UCI Machine Learning
Repository. <https://doi.org/10.24432/C5859H>

## Classification: Palmer Penguins

Path: `classification/palmer-penguins/`

- `penguins.csv` is the official curated CSV distributed by the
  `palmerpenguins` project.

The dataset has 344 observations and eight columns. It includes three penguin
species and four numeric measurements: bill length, bill depth, flipper
length, and body mass. There are 333 complete observations.

Source: [palmerpenguins dataset documentation](https://allisonhorst.github.io/palmerpenguins/)

Data contributors: Dr. Kristen Gorman, Palmer Station Long Term Ecological
Research program, and the `palmerpenguins` maintainers.

## Snapshot integrity

The files were downloaded and prepared on 2026-10-24. SHA-256 hashes are
recorded in `SHA256SUMS` so later changes can be detected explicitly.
