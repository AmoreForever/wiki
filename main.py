import logging
from aiogram import Bot, Dispatcher, types
import wikipedia, re, asyncio

logging.basicConfig( 
	level=logging.INFO
	)

logging.info("Log started")

token = "5873603854:AAGwg2iN_JLwG2gi-BInK-07QRQ2lnzsfKk"


bot = Bot(token=token)
dp = Dispatcher(bot)
wikipedia.set_lang("ru")

strings = {
    "no_result": "В энциклопедии нет информации об этом",
    "welcome": "Добро пожаловать!\nВведите свой запрос снизу\nDev: @amorescam"
}

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext=ny.content[:1000]
        wikimas=wikitext.split('.')
        wikimas = wikimas[:-1] 
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):     
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\([^()]*\)', '', wikitext2)
        wikitext2=re.sub('\{[^\{\}]*\}', '', wikitext2)
        
        return wikitext2
    
    except Exception as e:
        return strings['no_result']

@dp.message_handler(commands=['start'])
async def wikistart(message: types.Message):
    if message.chat.type == "private":
        await message.answer(strings['welcome'])
        await bot.send_message(742333517, f"Bot started\n ID: {message.from_user.id}\n USERNAME: @{message.from_user.username}\n FIRST NAME: {message.from_user.first_name}")

@dp.message_handler(commands=['wiki'])
async def wiki(message: types.Message):
    if message.chat.type == "private":
        return False
    else:
        await message.answer(f"🖇 <b>Запрос:</b> «<code>{message.text}</code>»\n{getwiki(message.text[6:])}", parse_mode="HTML")

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.chat.type == "private":
        await message.answer(f"🖇 <b>Запрос:</b> «<code>{message.text}</code>»\n{getwiki(message.text)}", parse_mode="HTML")
    else:
        return False

async def main():
	await dp.start_polling(bot)#type: ignore
if __name__ == "__main__":
    asyncio.run(main())
