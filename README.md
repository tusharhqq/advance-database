# Local Docker images

| Image | Dir |
| --- | --- |
| aquery | [`aquery/`](aquery/) |
| reprozip | [`reprozip/`](reprozip/) |
| combined_mega | [`combined_mega/`](combined_mega/) |

Modal image builds stay under `<name>/image/`; these Dockerfiles are for running locally.

## Dockerfile formatting and linting

```sh
brew install dprint hadolint
dprint fmt
hadolint aquery/Dockerfile combined_mega/Dockerfile reprozip/Dockerfile
```

Use `dprint check` to verify formatting without changing files.
