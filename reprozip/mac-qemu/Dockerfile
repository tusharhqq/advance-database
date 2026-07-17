# Docker Desktop on macOS runs Linux containers. ReproZip tracer requires linux/amd64.
FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

ENV PYTHONUNBUFFERED=1
RUN uv pip install --system "reprozip==1.3.2" "reprounzip==1.3.2"

WORKDIR /work
CMD ["bash"]
