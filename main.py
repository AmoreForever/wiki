import logging
from aiogram import Bot, Dispatcher, types
import wikipedia, re, asyncio

logging.basicConfig( 
	level=logging.INFO
	)

logging.info("Log started")

print("Bot started")

token = "5873603854:AAGwg2iN_JLwG2gi-BInK-07QRQ2lnzsfKk"


bot = Bot(token=token)
dp = Dispatcher(bot)

wikipedia.set_lang("ru")

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
        return 'В энциклопедии нет информации об этом'

@dp.message_handler(commands=['start'])
async def wikistart(message: types.Message):
    if message.chat.type == "private":
        await message.answer("Добро пожаловать!\nВведите свой запрос снизу\nDev: @amorescam")
        await bot.send_message(742333517, f"Bot started\n ID: {message.from_user.id}\n USERNAME: @{message.from_user.username}\n FIRST NAME: {message.from_user.first_name}\n PREMIUM: {message.from_user.is_premium}")

@dp.message_handler(commands=['wiki'])
async def wiki(message: types.Message):
    if message.chat.type == "private":
        return False
    else:
        await message.answer(getwiki(message.text[6:]))

@dp.message_handler(content_types=['text'])
async def text(message: types.Message):
    if message.chat.type == "private":
        await message.answer(getwiki(message.text))
    else:
        return False

async def main():
	await dp.start_polling(bot)#type: ignore
if __name__ == "__main__":
    asyncio.run(main())
