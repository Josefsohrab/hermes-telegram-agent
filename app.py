#!/usr/bin/env python3
"""Hermes Agent + 9Router — Hugging Face Space (Gradio Edition)"""

import subprocess, os, sys, time, threading

ROUTER_PORT = 9000
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "not-set")
TELEGRAM_USER_ID = os.environ.get("TELEGRAM_USER_ID", "0")

def install_and_start_services():
    """Install 9Router + Hermes, then start both in background."""
    try:
        # 1. Install 9Router
        print("[1/5] Installing 9Router...", flush=True)
        subprocess.run(["npm", "install", "-g", "9router"], check=True,
                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[1/5] Done.")

        # 2. Install Hermes
        print("[2/5] Installing Hermes Agent...", flush=True)
        subprocess.run(
            "curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash",
            shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[2/5] Done.")

        # 3. Generate Hermes config
        print("[3/5] Generating config...", flush=True)
        hermes_dir = os.path.expanduser("~/.hermes")
        os.makedirs(hermes_dir, exist_ok=True)

        with open(os.path.join(hermes_dir, "config.yaml"), "w") as f:
            f.write(f"""model:
  default: "kr/claude-sonnet-4.5"
  provider: "custom"
  base_url: "http://127.0.0.1:{ROUTER_PORT}/v1"

platforms:
  telegram:
    enabled: true
    token: "{TELEGRAM_BOT_TOKEN}"
    allowed_users: [{TELEGRAM_USER_ID}]
""")
        with open(os.path.join(hermes_dir, ".env"), "w") as f:
            f.write(f"OPENAI_API_KEY=9router\nTELEGRAM_BOT_TOKEN={TELEGRAM_BOT_TOKEN}\nTELEGRAM_ALLOWED_USERS={TELEGRAM_USER_ID}\n")
        print("[3/5] Done.")

        # 4. Start 9Router
        print(f"[4/5] Starting 9Router on port {ROUTER_PORT}...", flush=True)
        subprocess.Popen(["9router", "--port", str(ROUTER_PORT), "--host", "0.0.0.0"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        import urllib.request
        for i in range(30):
            try:
                urllib.request.urlopen(f"http://127.0.0.1:{ROUTER_PORT}/v1/models", timeout=2)
                print(f"[4/5] 9Router ready! (attempt {i+1})")
                break
            except Exception:
                time.sleep(2)

        # 5. Start Hermes Gateway
        print("[5/5] Starting Hermes Telegram Gateway...", flush=True)
        env = os.environ.copy()
        env["OPENAI_API_KEY"] = "9router"
        subprocess.Popen(["hermes", "gateway"], env=env,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("[5/5] Done! Bot is starting...", flush=True)
        return True
    except Exception as e:
        print(f"ERROR: {e}", flush=True)
        return False

# Start services in background thread
service_thread = threading.Thread(target=install_and_start_services, daemon=True)
service_thread.start()

# ── Gradio UI ──
import gradio as gr

with gr.Blocks(title="Hermes Agent", theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.Markdown("""
    # 🤖 Hermes Agent — ربات تلگرام هوشمند
    
    > ربات تلگرام شما در حال راه‌اندازی در پس‌زمینه این Space است.
    > لطفاً ۲ تا ۳ دقیقه صبر کنید تا نصب و راه‌اندازی کامل شود.
    
    ---
    
    ## ✅ وضعیت
    """)
    
    with gr.Row():
        gr.Markdown("🟢 **9Router** — سرویس API هوش مصنوعی")
        gr.Markdown("🟢 **Hermes Gateway** — اتصال به تلگرام")
    
    gr.Markdown("""
    ---
    
    ## 📱 نحوه استفاده
    
    ۱. در تلگرام، ربات خود را جستجو کنید
    ۲. دکمه **START** را بزنید یا `/start` بفرستید
    ۳. ربات با **Claude Sonnet 4.5** به شما پاسخ می‌دهد!
    
    ---
    
    ⚠️ **نکته:** این Space هر چند ساعت یکبار restart می‌شود (طبیعی است). ربات پس از restart دوباره فعال می‌شود.
    """)

demo.launch(server_name="0.0.0.0", server_port=7860)
