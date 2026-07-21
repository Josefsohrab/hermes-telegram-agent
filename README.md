# Hermes Agent + 9Router on Koyeb 🚀

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/Josefsohrab/hermes-telegram-agent&branch=main&name=hermes-telegram-agent&ports=8080;http;/)

راه‌اندازی **ربات تلگرام Hermes Agent** با استفاده از **9Router** روی پلتفرم ابری **Koyeb** به صورت کاملاً رایگان و ۲۴ ساعته.

## ⚡ دیپلوی با یک کلیک

روی دکمه بالا کلیک کنید ← دو متغیر زیر را وارد کنید ← تمام!

## 📋 پیش‌نیازها

قبل از دیپلوی، این دو مقدار را آماده کنید:

| نیاز | از کجا بگیرم | مثال |
|------|-------------|------|
| **توکن ربات تلگرام** | [@BotFather](https://t.me/BotFather) ← `/newbot` | `123456:ABCdef...` |
| **آی‌دی عددی تلگرام** | [@userinfobot](https://t.me/userinfobot) ← `/start` | `987654321` |

## 🚀 روش دوم: دیپلوی دستی

### گام ۱: Fork کنید

این ریپازیتوری را Fork کنید یا از طریق پنل Koyeb مستقیماً به آن متصل شوید.

### گام ۲: سرویس جدید در Koyeb

1. وارد [Koyeb](https://app.koyeb.com) شوید
2. روی **Create Service** کلیک کنید
3. گزینه **GitHub** ← این ریپازیتوری را انتخاب کنید
4. فایل `koyeb.yaml` به طور خودکار تنظیمات را اعمال می‌کند

### گام ۳: متغیرهای مخفی (Secrets)

| متغیر | توضیح |
|-------|-------|
| `TELEGRAM_BOT_TOKEN` | توکن دریافتی از BotFather |
| `TELEGRAM_USER_ID` | آی‌دی عددی شما از userinfobot |

### گام ۴: دیپلوی 🎯

روی **Deploy** کلیک کنید. سرویس پس از ۲-۳ دقیقه آماده می‌شود!

## 🛠 ساختار پروژه

| فایل | توضیح |
|------|-------|
| `Dockerfile` | Node 22 Alpine + Python + 9Router + Hermes |
| `entrypoint.sh` | راه‌اندازی با health check هوشمند |
| `koyeb.yaml` | پیکربندی خودکار سرویس Koyeb |

## ✨ ویژگی‌ها

- ✅ **Alpine Linux** — حجم کم، سرعت بالا
- ✅ **Health check خودکار** 9Router با ۳۰ تلاش
- ✅ **متغیر `LISTEN_HOST`** به جای `HOSTNAME` برای جلوگیری از تداخل
- ✅ **اجرای ۲۴/۷** روی پلن رایگان Koyeb (بدون خواب!)
- ✅ **پیکربندی خودکار** با فایل `koyeb.yaml`

## ⚠️ نکات مهم

- پلن رایگان Koyeb: **۵۱۲MB رم** و **۱ vCPU**
- منطقه پیش‌فرض: **Paris (par)** — برای تأخیر کمتر می‌توانید تغییر دهید
- لاگ‌ها را از پنل Koyeb بررسی کنید
- در صورت نیاز به منابع بیشتر، instance را به `micro` یا `small` ارتقا دهید

## 📊 وضعیت سرویس

پس از دیپلوی موفق، نشانگر وضعیت در پنل Koyeb باید **Healthy** باشد:

```
✓ Build completed
✓ Deployment successful  
✓ Health check: Healthy
```

---

⚡ ساخته شده برای اجرای آسان — فقط با یک کلیک!
