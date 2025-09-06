FROM node:20-alpine3.19 AS builder

WORKDIR /app

COPY package*.json ./
COPY yarn.lock ./
RUN yarn install --frozen-lockfile

COPY . .

RUN yarn build

FROM nginx:1.25.4-alpine-slim

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]