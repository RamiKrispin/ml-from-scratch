FROM ghcr.io/astral-sh/uv:0.13.5@sha256:32a7bb39b496babbd997b0a39a4d66c126bdaf5661b302bf6f06abda8deca6ff AS uv
FROM python:3.12.15-slim-trixie@sha256:a0f57064cbdcd6285fa45f51237ab0b35ea8ebaed06a1f5973e89e19dfb86704

ARG DEBIAN_FRONTEND=noninteractive
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates git \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} --create-home ${USERNAME}

COPY --from=uv /uv /uvx /usr/local/bin/
COPY environments/numpy/pyproject.toml environments/numpy/uv.lock /opt/numpy/

ENV UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=never

RUN uv sync --project /opt/numpy --locked \
    && chown -R ${USERNAME}:${USERNAME} /opt/numpy \
    && mkdir -p /workspace \
    && chown ${USERNAME}:${USERNAME} /workspace

ENV PATH="/opt/numpy/.venv/bin:${PATH}"

WORKDIR /workspace
USER ${USERNAME}

CMD ["python"]
