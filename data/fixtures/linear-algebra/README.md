# T02 linear-algebra fixtures

These small CSV files define the shared inputs and expected outputs for
Tutorial 2. NumPy, MLX, and base R load the same serialized values so parity
does not depend on language-specific random-number generators.

- `feature-matrix.csv` contains three observations and two ordered features.
- `coefficient-vector.csv` contains one coefficient for each feature, in the
  same order as the feature-matrix columns.
- `linear-system.csv` contains a two-by-two coefficient matrix and its
  right-hand-side vector.
- `expected-results.csv` contains flattened reference values checked by all
  three implementations with absolute and relative tolerances of `1e-6`.

The values are synthetic teaching inputs. They are not observations from the
public regression or classification datasets and do not represent a fitted
model.
