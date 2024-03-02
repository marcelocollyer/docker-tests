FROM node:21 as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

FROM node:21-alpine

WORKDIR /app

COPY --from=builder /app .

EXPOSE 8001

CMD ["node", "server.js"]
