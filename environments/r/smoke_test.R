left <- c(1, 2, 3)
right <- c(4, 5, 6)
result <- sum(left * right)

if (!isTRUE(all.equal(result, 32))) {
  stop(sprintf("Expected dot product 32, received %s", result))
}

cat(sprintf("R %s\n", getRversion()))
cat(sprintf("platform: %s\n", R.version$platform))
cat(sprintf("dot product: %s\n", result))
