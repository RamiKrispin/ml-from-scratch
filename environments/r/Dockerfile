FROM r-base:4.6.1@sha256:ad9b3bbca751f3ead77704fed4c20246127647b3d567b2bf970b7789e8d7b9a8

ARG DEBIAN_FRONTEND=noninteractive
ARG QUARTO_VERSION=1.10.19
ARG TARGETARCH

RUN mkdir -p /opt/r/library \
    && mkdir -p /workspace \
    && chown docker:staff /workspace

RUN case "${TARGETARCH}" in \
      amd64) QUARTO_FILE="quarto-${QUARTO_VERSION}-linux-amd64.deb"; QUARTO_SHA="7f0c4769e7f0e55f50d922f44b18db5118fb388d2b8fd27291fe1f8beafb43eb" ;; \
      arm64) QUARTO_FILE="quarto-${QUARTO_VERSION}-linux-arm64.deb"; QUARTO_SHA="35bb613052da98bef92ec3b7de77c3405a8e546363c7d2aa3abe15a39efa5045" ;; \
      *) echo "Unsupported architecture: ${TARGETARCH}" >&2; exit 1 ;; \
    esac \
    && wget --quiet --output-document="/tmp/${QUARTO_FILE}" \
      "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/${QUARTO_FILE}" \
    && echo "${QUARTO_SHA}  /tmp/${QUARTO_FILE}" | sha256sum --check --strict \
    && dpkg --install "/tmp/${QUARTO_FILE}" \
    && rm -f "/tmp/${QUARTO_FILE}"

COPY environments/r/renv.lock /opt/r/renv.lock

ENV USE_BUNDLED_LIBUV=1

RUN R -e 'install.packages("renv", repos = "https://cloud.r-project.org")' \
    && R -e 'renv::restore(project = "/opt/r", lockfile = "/opt/r/renv.lock", library = "/opt/r/library", prompt = FALSE)'

ENV R_LIBS_USER=/opt/r/library

WORKDIR /workspace
USER docker

CMD ["R"]
