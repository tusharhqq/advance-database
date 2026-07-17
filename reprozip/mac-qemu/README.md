# reprozip on macOS

## Docker

Requires Docker Desktop. On Apple Silicon, Docker runs this x86-64 ReproZip image through QEMU emulation — the tracer does not support aarch64.

```bash
docker build --platform=linux/amd64 -t reprozip:mac \
  -f reprozip/mac-qemu/Dockerfile reprozip/mac-qemu

docker run --rm -it --platform=linux/amd64 \
  -v "$PWD:/work" -w /work reprozip:mac
```

Inside the container, e.g. `reprozip trace python3 hi.py` then `reprozip pack mypack`.
