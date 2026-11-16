# Stage 1: Builder
FROM caddy:2.11.9-builder@sha256:3fddbec729442a56b942d4c9eaef1df80893dbf2cf5b86701bfae6aad1408eeb AS builder

RUN xcaddy build \
    --with github.com/hslatman/caddy-crowdsec-bouncer@v0.12.1 \
    --output /usr/bin/caddy

# Stage 2: Final
FROM caddy:2.11.9@sha256:0c2243efcf437ab7f7a978f1027fcf0d4f9be8a75df27b1b3fbc5dbe0ffa8cf0

LABEL org.opencontainers.image.description="Caddy web server with CrowdSec bouncer"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
