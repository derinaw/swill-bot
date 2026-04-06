import openai
from telegram.ext import Application, MessageHandler, filters

TELEGRAM_TOKEN = "8770450139:AAEMM-O7qg0S3hsyhsVGtcFD-bARrOyOK3E"
DEEPSEEK_API_KEY = "sk-cc1a4d1894a14be3abd7804bf24da707"

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
