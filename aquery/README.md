# Local aquery Docker image

From repo root (Apple Silicon: keep `--platform=linux/amd64`):

```bash
docker build --platform=linux/amd64 -t aquery:local -f dockerr/aquery/Dockerfile aquery

# compile only (no license)
docker run --rm --platform=linux/amd64 \
  -v "$PWD/mountain/hw1_11:/work" -w /work aquery:local \
  a2q -c -a 1 -o max_loss.generated.q max_loss.a
```

To run `q` / pykx, put `KDB_LICENSE_B64=...` in repo-root `.env` (gitignored), then:

```bash
docker run --rm --platform=linux/amd64 --env-file .env \
  -v "$PWD/mountain/hw1_11:/work" -w /work aquery:local \
  /opt/kx/with-kx-license bash
```

Shell: `docker run --rm -it --platform=linux/amd64 --env-file .env -v "$PWD/mountain/hw1_11:/work" -w /work aquery:local`
