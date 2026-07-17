# Local Docker image mirroring Modal named Image ``combined_mega``
# (aquery + reprozip + duckdb + postgres + uv/ruff/ty).
# Requires linux/amd64 (KDB-X + AQuery + ReproZip tracer).
#
# Build (from repo root):
# docker build --platform=linux/amd64 -t combined_mega:local \
# -f dockerr/combined_mega/Dockerfile combined_mega

FROM azul/zulu-openjdk@sha256:772cff8aa0094d620beb36d2e068db8e6b7e18da9ce7edf8a44826a8adbfd6b6

ENV DEBIAN_FRONTEND=noninteractive \
    KDBX_HOME=/opt/kx \
    QHOME=/opt/kx \
    QLIC=/tmp/kx-lic \
    PATH=/opt/kx/bin:/root/.local/bin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PYTHONUNBUFFERED=1

# Ubuntu jammy Postgres packages resolved 2026-07-15 (smoke: 14.23).
ARG POSTGRES_APT=14.23-0ubuntu0.22.04.1

RUN apt-get update && apt-get install -y --no-install-recommends bash ca-certificates curl file git gzip unzip rlwrap python3 python3-venv python3-dev gcc g++ sqlite3 libsqlite3-dev libssl-dev libffi-dev make "postgresql-14=${POSTGRES_APT}" "postgresql-client-14=${POSTGRES_APT}" "libpq-dev=${POSTGRES_APT}" && rm -rf /var/lib/apt/lists/* && ln -sf /usr/bin/python3 /usr/local/bin/python && for d in /usr/lib/postgresql/*/bin; do [ -d "$d" ] && ln -sf "$d"/* /usr/local/bin/; done && command -v postgres && command -v pg_ctl && command -v psql

COPY image/install_kdbx.sh /opt/install_kdbx.sh
COPY image/install_aquery.sh /opt/install_aquery.sh
COPY image/install_tooling.sh /opt/install_tooling.sh
COPY image/with_kx_license.sh /opt/kx/with-kx-license

RUN chmod +x /opt/install_kdbx.sh /opt/install_aquery.sh /opt/install_tooling.sh /opt/kx/with-kx-license && KDBX_HOME=/opt/kx /opt/install_kdbx.sh && PATH=/root/.local/bin:$PATH /opt/install_aquery.sh && /opt/install_tooling.sh && uv pip install --system "pykx==4.0.0" "reprozip==1.3.2" "reprounzip==1.3.2" "duckdb==1.5.4" "ruff==0.15.21" "ty==0.0.58" && test -x /opt/kx/bin/q && test -x /root/.local/bin/a2q && test -x /opt/kx/with-kx-license && test -x /usr/local/bin/uv && test -x /usr/local/bin/duckdb && python -c "import duckdb, sqlite3; print(duckdb.__version__, sqlite3.sqlite_version)" && reprozip --help >/dev/null && reprounzip --help >/dev/null && command -v ruff && command -v ty

WORKDIR /work

# Do not force with-kx-license as ENTRYPOINT so a2q / duckdb / psql work without a license.
CMD ["bash"]
