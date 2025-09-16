FROM golang:1.25.1 AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y make && apt-get clean

COPY . .

RUN make build

FROM debian

WORKDIR /app

COPY --from=builder /app/movie-server .

EXPOSE 8080
CMD ["./movie-server"]