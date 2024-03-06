FROM python:3.9 as builder

WORKDIR /app

COPY main.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=builder /app/main.py .

RUN apt update && \
    apt install curl -y

EXPOSE 8000

CMD ["python", "main.py"]