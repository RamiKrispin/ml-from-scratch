from importlib.metadata import version

import mlx.core as mx


left = mx.array([1.0, 2.0, 3.0])
right = mx.array([4.0, 5.0, 6.0])
result = mx.sum(left * right)
mx.eval(result)
value = float(result.item())

if abs(value - 32.0) > 1e-6:
    raise AssertionError(f"Expected dot product 32.0, received {value}")

print(f"Python MLX {version('mlx')}")
print(f"default device: {mx.default_device()}")
print(f"dtype: {left.dtype}")
print(f"dot product: {value}")
