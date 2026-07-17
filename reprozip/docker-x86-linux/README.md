# reprozip on x86 Linux

## Docker

Requires an x86-64 Linux host.

```bash
docker build --platform=linux/amd64 -t reprozip:linux-x86 \
  -f reprozip/docker-x86-linux/Dockerfile reprozip/docker-x86-linux

docker run --rm -it \
  -v "$PWD:/work" -w /work reprozip:linux-x86
```

Inside the container, e.g. `reprozip trace python3 hi.py` then `reprozip pack mypack`.
