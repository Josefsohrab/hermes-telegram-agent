FROM node:22-alpine

# Install Python and essential system tools
RUN apk add --no-cache \
    python3 \
    py3-pip \
    curl \
    git \
    make \
    g++

WORKDIR /app

# Install 9Router globally
RUN npm install -g 9router

# Install Hermes Agent
RUN curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
ENV PATH="/root/.local/bin:${PATH}"

# Define port for the application
ENV PORT=8080
ENV LISTEN_HOST=0.0.0.0

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8080

ENTRYPOINT ["/entrypoint.sh"]