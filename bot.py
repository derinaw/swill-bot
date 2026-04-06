import openai
from telegram.ext import Application, MessageHandler, filters

TELEGRAM_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"
DEEPSEEK_API_KEY = "sk-ваш_ключ"

openai.api_key = DEEPSEEK_API_KEY
openai.base_url = "https://api.deepseek.com/v1"

async def handle(update, context):
    user_text = update.message.text
    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": user_text}],
        temperature=0.9
    )
    await update.message.reply_text(response.choices[0].message.content)

app = Application.builder().token(TELEGRAM_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()
