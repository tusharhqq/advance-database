# Local reprozip Docker image

From repo root (Apple Silicon: keep `--platform=linux/amd64` — ReproZip's tracer is x86_64-only):

```bash
docker build --platform=linux/amd64 -t reprozip:local -f dockerr/reprozip/Dockerfile dockerr/reprozip

docker run --rm -it --platform=linux/amd64 \
  -v "$PWD/mountain/reprozip:/work" -w /work reprozip:local
```

Inside the container, e.g. `reprozip trace python3 hi.py` then `reprozip pack mypack`.
