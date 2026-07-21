---
title: Hermes Agent Telegram Bot
emoji: 🤖
colorFrom: blue
colorTo: indigo
sdk: docker
pinned: false
---

# 🤖 Hermes Agent + 9Router

**ربات هوشمند تلگرام** با پشتیبانی از Claude Sonnet 4.5 — کاملاً رایگان و بدون نیاز به کارت اعتباری.

## 🚀 نحوه استفاده

۱. در تلگرام به [@BotFather](https://t.me/BotFather) بروید و یک ربات جدید بسازید
۲. توکن ربات را دریافت کنید
۳. آی‌دی عددی خود را از [@userinfobot](https://t.me/userinfobot) بگیرید
۴. در تنظیمات این Space (تب Settings) به بخش **Repository secrets** بروید
۵. دو secret زیر را اضافه کنید:

| Name | Value |
|------|-------|
| `TELEGRAM_BOT_TOKEN` | توکن دریافتی از BotFather |
| `TELEGRAM_USER_ID` | آی‌دی عددی شما |

۶. به تب **Settings** برگردید و مطمئن شوید **Factory reboot** زده نشده
۷. Space به طور خودکار restart می‌شود و ربات شما آنلاین می‌شود!

## ✨ ویژگی‌ها

- ✅ کاملاً رایگان — بدون کارت اعتباری
- ✅ اجرای ۲۴/۷ روی سرورهای Hugging Face
- ✅ Claude Sonnet 4.5 از طریق 9Router
- ✅ فقط مخصوص شما — با محدودیت user ID تلگرام
