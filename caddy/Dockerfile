# Stage 1: Builder
FROM caddy:2.11.4-builder@sha256:08aab4980494ed7ed38d0249705d6f39b482c3373b578af7494168d19df62411 AS builder

RUN xcaddy build \
    --with github.com/hslatman/caddy-crowdsec-bouncer@v0.12.1 \
    --output /usr/bin/caddy

# Stage 2: Final
FROM caddy:2.11.4@sha256:533f1bff9a76426aee55fb2934636c25a2769aad8fb57f34dd39cca8cd2bab84

COPY --from=builder /usr/bin/caddy /usr/bin/caddy
