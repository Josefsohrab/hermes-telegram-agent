#!/bin/bash
set -e

# Create Hermes config directory
mkdir -p /root/.hermes

# Generate Hermes config from environment variables
cat <<EOF > /root/.hermes/config.yaml
model:
  default: "kr/claude-sonnet-4.5"
  provider: "custom"
  base_url: "http://127.0.0.1:8080/v1"

platforms:
  telegram:
    enabled: true
    token: "${TELEGRAM_BOT_TOKEN}"
    allowed_users: [${TELEGRAM_USER_ID}]
EOF

# Create .env file
cat <<EOF > /root/.hermes/.env
OPENAI_API_KEY=9router
TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
TELEGRAM_ALLOWED_USERS=${TELEGRAM_USER_ID}
EOF

# Start 9Router on port 8080
echo "Starting 9Router on port 8080..."
9router --port 8080 --host 0.0.0.0 &

# Wait for 9Router to be ready
echo "Waiting for 9Router to start..."
for i in $(seq 1 30); do
    if curl -s http://127.0.0.1:8080/v1/models > /dev/null 2>&1; then
        echo "9Router is ready!"
        break
    fi
    if [ $i -eq 30 ]; then
        echo "WARNING: 9Router may not be fully ready after 60 seconds"
    fi
    echo "Waiting... ($i/30)"
    sleep 2
done

# Check Hermes configuration
hermes config check

# Start Telegram gateway
echo "Starting Hermes Agent Telegram Gateway..."
exec hermes gateway
