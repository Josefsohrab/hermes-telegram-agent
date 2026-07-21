#!/usr/bin/env python3
"""Hermes Agent + 9Router — Hugging Face Space Edition"""

import subprocess, os, sys, time

ROUTER_PORT = 9000
LISTEN_PORT = int(os.environ.get("PORT", "7860")) 
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID", "")

def run(cmd, shell=False):
    print(f"▶ {cmd if isinstance(cmd, str) else ' '.join(cmd)}")
    subprocess.run(cmd, shell=shell, check=True)

# ── 1. Install 9Router ──
print("📦 Installing 9Router...")
run(["npm", "install", "-g", "9router"])

# ── 2. Install Hermes ──
print("📦 Installing Hermes Agent...")
run("curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash", shell=True)

# ── 3. Generate config ──
print("⚙ Generating Hermes config...")
hermes_dir = os.path.expanduser("~/.hermes")
os.makedirs(hermes_dir, exist_ok=True)

config = f"""model:
  default: "kr/claude-sonnet-4.5"
  provider: "custom"
  base_url: "http://127.0.0.1:{ROUTER_PORT}/v1"

platforms:
  telegram:
    enabled: true
    token: "{TELEGRAM_BOT_TOKEN}"
    allowed_users: [{TELEGRAM_USER_ID}]
"""
with open(os.path.join(hermes_dir, "config.yaml"), "w") as f:
    f.write(config)

env_content = f"""OPENAI_API_KEY=9router
TELEGRAM_BOT_TOKEN={TELEGRAM_BOT_TOKEN}
TELEGRAM_ALLOWED_USERS={TELEGRAM_USER_ID}
"""
with open(os.path.join(hermes_dir, ".env"), "w") as f:
    f.write(env_content)

# ── 4. Start 9Router ──
print(f"🚀 Starting 9Router on port {ROUTER_PORT}...")
subprocess.Popen(["9router", "--port", str(ROUTER_PORT), "--host", "0.0.0.0"],
                 stdout=sys.stdout, stderr=sys.stderr)

import urllib.request
for i in range(30):
    try:
        urllib.request.urlopen(f"http://127.0.0.1:{ROUTER_PORT}/v1/models", timeout=2)
        print(f"✅ 9Router ready! (attempt {i+1})")
        break
    except Exception:
        print(f"⏳ Waiting... ({i+1}/30)")
        time.sleep(2)

# ── 5. Start Hermes ──
print("🚀 Starting Hermes Telegram Gateway...")
env = os.environ.copy()
env["OPENAI_API_KEY"] = "9router"
subprocess.Popen(["hermes", "gateway"], env=env, stdout=sys.stdout, stderr=sys.stderr)

# ── 6. Simple health server on HF port ──
from http.server import HTTPServer, BaseHTTPRequestHandler

HTML = """<!DOCTYPE html><html dir=rtl lang=fa>
<head><meta charset=UTF-8><title>Hermes Agent</title>
<style>body{font-family:system-ui;display:flex;justify-content:center;align-items:center;min-height:100vh;margin:0;background:#0f172a;color:#e2e8f0}.card{text-align:center;padding:3rem;background:#1e293b;border-radius:1rem;box-shadow:0 4px 24px rgba(0,0,0,.3)}.dot{display:inline-block;width:12px;height:12px;border-radius:50%;background:#22c55e;margin-left:8px;animation:pulse 2s infinite}@keyframes pulse{0%,100%{opacity:1}50%{opacity:.5}}h1{font-size:2rem;margin-bottom:.5rem}p{color:#94a3b8}code{background:#334155;padding:2px 8px;border-radius:4px}</style>
</head><body><div class=card><h1>🤖 Hermes Agent <span class=dot></span></h1><p>ربات تلگرام در حال اجراست ✅</p><p>به تلگرام بروید و <code>/start</code> را بفرستید</p></div></body></html>"""

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode())
    def log_message(self, *a): pass

print(f"🌐 Health page on port {LISTEN_PORT}")
HTTPServer(("0.0.0.0", LISTEN_PORT), H).serve_forever()
