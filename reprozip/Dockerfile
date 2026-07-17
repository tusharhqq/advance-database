# Local Docker image mirroring Modal named Image ``reprozip``.
# Build (from repo root):
# docker build --platform=linux/amd64 -t reprozip:local -f dockerr/reprozip/Dockerfile dockerr/reprozip
# (linux/amd64 required — ReproZip tracer does not support aarch64.)

FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ENV PYTHONUNBUFFERED=1
RUN uv pip install --system "reprozip==1.3.2" "reprounzip==1.3.2"

WORKDIR /work
CMD ["bash"]
