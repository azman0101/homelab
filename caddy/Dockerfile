# Stage 1: Builder
FROM caddy:2.11.7-builder@sha256:b25f47453fa02f7e66c0828b4b1343658808b9000950b6825c4a1cb0c988f5f8 AS builder

RUN xcaddy build \
    --with github.com/hslatman/caddy-crowdsec-bouncer@v0.12.1 \
    --output /usr/bin/caddy

# Stage 2: Final
FROM caddy:2.11.7@sha256:f2a1290d0463aad60660d4ec134943f183ee2a5f6c3eb7bf32dd984f2f020772

LABEL org.opencontainers.image.description="Caddy web server with CrowdSec bouncer"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
