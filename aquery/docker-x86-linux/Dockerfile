FROM --platform=linux/amd64 azul/zulu-openjdk@sha256:772cff8aa0094d620beb36d2e068db8e6b7e18da9ce7edf8a44826a8adbfd6b6

ENV DEBIAN_FRONTEND=noninteractive \
    KDBX_HOME=/opt/kx \
    QHOME=/opt/kx \
    QLIC=/tmp/kx-lic \
    PATH=/opt/kx/bin:/root/.local/bin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends ca-certificates curl file git gzip unzip rlwrap python3 python3-venv \
    && rm -rf /var/lib/apt/lists/* \
    && ln -sf /usr/bin/python3 /usr/local/bin/python

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv
COPY image/install_kdbx.sh /opt/install_kdbx.sh
COPY image/install_aquery.sh /opt/install_aquery.sh
COPY image/with_kx_license.sh /opt/kx/with-kx-license

RUN chmod +x /opt/install_kdbx.sh /opt/install_aquery.sh /opt/kx/with-kx-license \
    && KDBX_HOME=/opt/kx /opt/install_kdbx.sh \
    && PATH=/root/.local/bin:$PATH /opt/install_aquery.sh \
    && uv pip install --system "pykx==4.0.0" \
    && test -x /opt/kx/bin/q \
    && test -x /root/.local/bin/a2q

WORKDIR /work
ENTRYPOINT ["/opt/kx/with-kx-license"]
CMD ["q"]
