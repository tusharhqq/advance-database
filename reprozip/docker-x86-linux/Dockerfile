FROM ghcr.io/astral-sh/uv:0.9.30-python3.11-bookworm-slim@sha256:4f5d923c9dcea037f57bda425dd209f3ec643da2f0b74227f68d09dab0b3bb36

ENV PYTHONUNBUFFERED=1
RUN uv pip install --system "reprozip==1.3.2" "reprounzip==1.3.2"

WORKDIR /work
CMD ["bash"]
