# Hermes Agent + 9Router on Render 🚀

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/Josefsohrab/hermes-telegram-agent)

راه‌اندازی **ربات تلگرام Hermes Agent** با استفاده از **9Router** روی پلتفرم ابری **Render** — کاملاً رایگان.

## ⚡ دیپلوی با یک کلیک

روی دکمه بالا کلیک کنید ← دو متغیر را وارد کنید ← تمام!

## 📋 پیش‌نیازها (۲ دقیقه)

قبل از دیپلوی، این دو مقدار را از تلگرام دریافت کنید:

| نیاز | از کجا بگیرم | مثال |
|------|-------------|------|
| **توکن ربات تلگرام** | [@BotFather](https://t.me/BotFather) ← `/newbot` | `123456:ABCdef...` |
| **آی‌دی عددی تلگرام** | [@userinfobot](https://t.me/userinfobot) ← `/start` | `987654321` |

## 🚀 روش اول: دیپلوی با یک کلیک (ساده‌ترین)

1. روی دکمه **Deploy to Render** در بالای صفحه کلیک کنید
2. در صفحه باز شده، نام سرویس را به دلخواه تنظیم کنید (پیش‌فرض: `hermes-telegram-agent`)
3. در بخش **Environment Variables**، این دو متغیر را اضافه کنید:

   | Key | Value |
   |-----|-------|
   | `TELEGRAM_BOT_TOKEN` | توکن دریافتی از BotFather |
   | `TELEGRAM_USER_ID` | آی‌دی عددی شما از userinfobot |

4. روی **Apply** کلیک کنید — حدود ۵ دقیقه صبر کنید تا بیلد تمام شود.

## 🚀 روش دوم: دیپلوی دستی

1. وارد [dashboard.render.com](https://dashboard.render.com) شوید
2. **New Web Service** ← GitHub ← این ریپازیتوری را انتخاب کنید
3. همه تنظیمات از فایل `render.yaml` خوانده می‌شود
4. متغیرهای `TELEGRAM_BOT_TOKEN` و `TELEGRAM_USER_ID` را اضافه کنید
5. روی **Create Web Service** کلیک کنید

## ⏰ مشکل خواب ۱۵ دقیقه‌ای — راه حل

⚠️ Render در پلن رایگان، سرویس را بعد از ۱۵ دقیقه بی‌کار ماندن می‌خواباند.

✅ **راه حل:** دو گزینه دارید:

### گزینه A: UptimeRobot (کاملاً رایگان — توصیه می‌شود)

1. به [uptimerobot.com](https://uptimerobot.com) بروید و ثبت‌نام کنید
2. **Add New Monitor** ← نوع **HTTP(s)** را انتخاب کنید
3. Friendly Name: `Hermes Agent`
4. URL: آدرس سرویس Render خود را وارد کنید (مثلاً `https://hermes-telegram-agent.onrender.com/v1/models`)
5. Monitoring Interval: **Every 5 minutes**
6. روی **Create Monitor** کلیک کنید

به همین سادگی! UptimeRobot هر ۵ دقیقه سرویس شما را پینگ می‌کند و هرگز نمی‌خوابد.

### گزینه B: Cron-job.org (جایگزین)

1. به [cron-job.org](https://cron-job.org) بروید
2. یک Cronjob با تنظیمات:
   - URL: `https://hermes-telegram-agent.onrender.com/v1/models`
   - Interval: **Every 5 minutes**
3. ذخیره کنید.

## 🛠 ساختار پروژه

| فایل | توضیح |
|------|-------|
| `Dockerfile` | Node 22 Alpine + Python + 9Router + Hermes |
| `entrypoint.sh` | راه‌اندازی با `PORT` داینامیک و health check هوشمند |
| `render.yaml` | پیکربندی خودکار سرویس Render |

## ✨ ویژگی‌های بهینه‌شده برای Render

- ✅ **پورت داینامیک** — `${PORT:-8080}` سازگار با Render
- ✅ **Alpine Linux** — حجم و رم کمتر، سرعت بالاتر
- ✅ **Health check خودکار** — ۳۰ تلاش تا آماده شدن 9Router
- ✅ **پلن رایگان دائمی** — ۵۱۲MB رم + ۰.۱ CPU
- ✅ **فعال‌سازی مجدد خودکار** — با ورود پیام تلگرام، سرویس در ۳۰-۶۰ ثانیه بیدار می‌شود

## ⚠️ نکات مهم

| نکته | توضیح |
|------|-------|
| **زمان بیدار شدن** | ۳۰-۶۰ ثانیه بعد از دریافت پیام — صبور باشید |
| **اولین پیام** | بعد از `/start` ممکن است ۱ دقیقه طول بکشد تا پاسخ بیاید |
| **محدودیت ماهانه** | ۷۵۰ ساعت رایگان (معادل تمام ماه) |
| **UptimeRobot** | حتماً تنظیم کنید تا سرویس نخوابد |

## 📊 وضعیت سرویس

پس از دیپلوی موفق، در پنل Render باید ببینید:

```
✓ Build successful
✓ Deploying...
✓ Your service is live 🟢
```

---

⚡ ساخته شده برای اجرای آسان — فقط با یک کلیک!
