FROM golang:1.25.1 AS builder
WORKDIR /app

COPY go.mod go.sum ./
RUN go mod download

COPY . .
RUN CGO_ENABLED=0 GOOS=linux go build -o movie-server

# final minimal image
FROM scratch
WORKDIR /app
COPY --from=builder /app/movie-server .
EXPOSE 8080
CMD ["./movie-server"]
