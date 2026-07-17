# Local combined_mega Docker image

From repo root (Apple Silicon: keep `--platform=linux/amd64`):

```bash
docker build --platform=linux/amd64 -t combined_mega:local \
  -f dockerr/combined_mega/Dockerfile combined_mega

docker run --rm --platform=linux/amd64 \
  -v "$PWD/mountain/hw2_1:/work" -w /work combined_mega:local \
  duckdb -c "SELECT 1;"
```

Shell: `docker run --rm -it --platform=linux/amd64 -v "$PWD/mountain/combined_mega:/work" -w /work combined_mega:local`

To run `q` / pykx, put `KDB_LICENSE_B64=...` in repo-root `.env` (gitignored), then use `--env-file .env` and `/opt/kx/with-kx-license`.

## Modal (same Dockerfile)

```bash
modal run dockerr/combined_mega/run_on_modal.py
```

Builds `dockerr/combined_mega/Dockerfile` with context `combined_mega/` via
`Image.from_dockerfile`, then smoke-tests (needs Secret `kx-license`).
