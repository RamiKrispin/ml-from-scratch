from importlib.metadata import version

import numpy as np


left = np.array([1.0, 2.0, 3.0], dtype=np.float64)
right = np.array([4.0, 5.0, 6.0], dtype=np.float64)
result = float(np.dot(left, right))

if not np.isclose(result, 32.0):
    raise AssertionError(f"Expected dot product 32.0, received {result}")

print(f"Python NumPy {version('numpy')}")
print(f"dtype: {left.dtype}")
print(f"dot product: {result}")
