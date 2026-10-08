# Stage 1: Builder
FROM caddy:2.11.6-builder@sha256:f5b1a66449d305280e559dba0ab9f7ce9a2a14c527c79d7c6fb48abc8f895818 AS builder

RUN xcaddy build \
    --with github.com/hslatman/caddy-crowdsec-bouncer@v0.12.1 \
    --output /usr/bin/caddy

# Stage 2: Final
FROM caddy:2.11.6@sha256:3422ce6de165df66534f9b9ba50efaf457114ec961763cc52f5dbdaac2972d73

LABEL org.opencontainers.image.description="Caddy web server with CrowdSec bouncer"

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
