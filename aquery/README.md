# Local aquery Docker image

This image requires a licensed version of kdb+.

From the repository root, add your base64-encoded license to `.env`:

```env
KDB_LICENSE_B64=your_base64_encoded_kdb_license
```

Build the image (keep `--platform=linux/amd64` on Apple Silicon):

```bash
docker build --platform=linux/amd64 -t aquery:local -f aquery/Dockerfile aquery
```

Compile an aquery program with the license loaded:

```bash
docker run --rm --platform=linux/amd64 --env-file .env \
  -v "$PWD/example/hw1_11:/work" -w /work aquery:local \
  /opt/kx/with-kx-license a2q -c -a 1 \
  -o max_loss.generated.q max_loss.a
```

Start an interactive licensed kdb+ shell:

```bash
docker run --rm -it --platform=linux/amd64 --env-file .env \
  -v "$PWD/example/hw1_11:/work" -w /work aquery:local \
  /opt/kx/with-kx-license q
```
