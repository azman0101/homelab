# Stage 1: Builder
FROM caddy:2.11.7-builder@sha256:c4cd20eaa0b69112fd5d4f721ffc9671687e1d5d0b155c8620cf7546dbef94c0 AS builder

RUN xcaddy build \
    --with github.com/hslatman/caddy-crowdsec-bouncer@v0.12.1 \
    --output /usr/bin/caddy

# Stage 2: Final
FROM caddy:2.11.7@sha256:36c24ad91a7ff7bc4c87fe22bfa8df3c4b18da0773d73fc12ee2c52b98c0bb7e

LABEL org.opencontainers.image.description="Caddy web server with CrowdSec bouncer"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
