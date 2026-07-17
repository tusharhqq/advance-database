# aquery on macOS

## kdb+ Community License

A kdb+ license is required.

1. [Sign up with KX](https://developer.kx.com/products/kdb-x/install) and copy your community license from the KX website.
2. From the repository root, create your local environment file:
   ```sh
   cp .env.example .env
   ```
3. Open `.env` and paste the license after `KDB_LICENSE_B64=`:
   ```env
   KDB_LICENSE_B64=paste_your_license_here
   ```

<img width="2746" height="1436" alt="KX license sign-up page" src="https://github.com/user-attachments/assets/6107d3ed-5f82-4cad-806b-47e656972786" />

<img width="2824" height="1402" alt="KX license download page" src="https://github.com/user-attachments/assets/518a167e-7f36-4e87-a470-7013c5ed84c4" />

## Docker

Requires Docker Desktop. On Apple Silicon, Docker runs this x86-64 kdb+ image through emulation.

```bash
docker build --platform=linux/amd64 -t aquery:mac \
  -f aquery/docker-mac/Dockerfile aquery
docker run --rm -it --platform=linux/amd64 --env-file .env aquery:mac
```
