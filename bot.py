import os
import openai
from telegram.ext import Application, MessageHandler, filters, CommandHandler

TELEGRAM_TOKEN = os.environ.get("8770450139:AAEMM-O7qg0S3hsyhsVGtcFD-bARrOyOK3E")
DEEPSEEK_API_KEY = os.environ.get("sk-cc1a4d1894a14be3abd7804bf24da707")

if not TELEGRAM_TOKEN:
    print("Ошибка: TELEGRAM_TOKEN не задан")
    exit(1)
if not DEEPSEEK_API_KEY:
    print("Ошибка: DEEPSEEK_API_KEY не задан")
    exit(1)

client = openai.OpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com/v1"
)

async def start(update, context):
    await update.message.reply_text("✅ Бот работает! Отправьте любое сообщение.")

async def handle(update, context):
    user_text = update.message.text
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": user_text}],
            temperature=0.9
        )
        answer = response.choices[0].message.content
        await update.message.reply_text(answer)
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {str(e)[:200]}")

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

print("🚀 Бот запущен")
app.run_polling()
