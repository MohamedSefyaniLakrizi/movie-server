FROM golang:1.25.1 AS builder

WORKDIR /app

# Install make for the build step
RUN apt-get update && apt-get install -y make && apt-get clean

# Copy everything into the build context
COPY . .

# Run make to build the image-server binary
RUN make build

# Use a minimal base image for the final output
FROM debian

WORKDIR /app

# Copy the built binary from the builder stage
COPY --from=builder /app/movie-server .

EXPOSE 8080
CMD ["./movie-server"]