# Small data-loading and plotting helpers for the T02 Quarto notebook.

load_fixture_tables <- function() {
  fixture_dir <- file.path("..", "..", "data", "fixtures", "linear-algebra")

  list(
    features = read.csv(
      file.path(fixture_dir, "feature-matrix.csv"),
      check.names = FALSE
    ),
    coefficients = read.csv(
      file.path(fixture_dir, "coefficient-vector.csv"),
      check.names = FALSE
    ),
    system = read.csv(
      file.path(fixture_dir, "linear-system.csv"),
      check.names = FALSE
    ),
    expected = read.csv(
      file.path(fixture_dir, "expected-results.csv"),
      check.names = FALSE
    )
  )
}


assert_close <- function(actual, target, label, tolerance = 1e-6) {
  matches <- isTRUE(all.equal(
    unname(actual),
    unname(target),
    tolerance = tolerance,
    check.attributes = FALSE
  ))

  if (!matches) {
    stop(sprintf("%s did not match the shared reference.", label))
  }
}


matrix_multiplication_plot <- function(features, coefficients, predictions) {
  tile_data <- data.frame(
    x = numeric(),
    y = numeric(),
    label = character(),
    component = character()
  )

  for (row in seq_len(nrow(features))) {
    for (column in seq_len(ncol(features))) {
      tile_data <- rbind(
        tile_data,
        data.frame(
          x = column - 1,
          y = 4 - row,
          label = format(features[row, column], trim = TRUE),
          component = "Feature matrix X"
        )
      )
    }
  }

  for (row in seq_along(coefficients)) {
    tile_data <- rbind(
      tile_data,
      data.frame(
        x = 3,
        y = 4 - row,
        label = format(coefficients[row], trim = TRUE),
        component = "Coefficients beta"
      )
    )
  }

  for (row in seq_along(predictions)) {
    tile_data <- rbind(
      tile_data,
      data.frame(
        x = 5,
        y = 4 - row,
        label = format(predictions[row], trim = TRUE),
        component = "Predictions X beta"
      )
    )
  }

  ggplot(tile_data, aes(x = x, y = y, fill = component, label = label)) +
    geom_tile(width = 0.82, height = 0.82, color = "#253238", linewidth = 0.8) +
    geom_text(size = 5, color = "#101820") +
    annotate("text", x = 0.5, y = 3.75, label = "X  (3 x 2)", size = 5) +
    annotate("text", x = 3, y = 3.75, label = "beta  (2 x 1)", size = 5) +
    annotate("text", x = 5, y = 3.75, label = "X beta  (3 x 1)", size = 5) +
    annotate("text", x = 2, y = 2, label = "x", size = 8, fontface = "bold") +
    annotate("text", x = 4, y = 2, label = "=", size = 8, fontface = "bold") +
    scale_fill_manual(values = c(
      "Feature matrix X" = "#8ECAE6",
      "Coefficients beta" = "#FFB703",
      "Predictions X beta" = "#90BE6D"
    )) +
    coord_fixed(xlim = c(-0.7, 5.7), ylim = c(0.4, 4.15), clip = "off") +
    labs(
      title = "Matrix multiplication keeps the outer dimensions",
      subtitle = "(3 x 2) x (2 x 1) -> (3 x 1): the inner dimensions match"
    ) +
    theme_void(base_size = 14) +
    theme(
      legend.position = "none",
      plot.title = element_text(size = 16, face = "bold"),
      plot.subtitle = element_text(size = 12)
    )
}
