FROM python:3.9 as builder

WORKDIR /app

COPY server.py .

FROM python:3.9-alpine

WORKDIR /app

COPY --from=builder /app/server.py .

RUN apk add --update curl && \
    rm -rf /var/cache/apk/*

EXPOSE 8000

CMD ["python", "server.py"]