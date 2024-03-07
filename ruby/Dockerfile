# Stage 1: Build the Ruby server
FROM ruby:latest AS builder

# Copy the server.rb file into the container
COPY server.rb /app/server.rb

# Set the working directory to /app
WORKDIR /app

# Install the WEBrick gem
RUN gem install webrick

# Stage 2: Create the final image
FROM ruby:slim

# Copy the built gems from the builder stage
COPY --from=builder /usr/local/bundle /usr/local/bundle

# Copy the server.rb file from the builder stage
COPY --from=builder /app/server.rb /app/server.rb

# Set the working directory to /app
WORKDIR /app

# Expose port 8000
EXPOSE 8000

# Command to run the Ruby server
CMD ["ruby", "server.rb"]
