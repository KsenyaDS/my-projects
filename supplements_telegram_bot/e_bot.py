from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import re  
from supplements_data import supplements_info, danger_levels_info,danger_levels_order
from function_e_bot import prepare_text, get_supplement_info
TOKEN = ""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
@dp.message_handler(commands=['start', 'help'])
async def send_welcome(msg: types.Message):
    await msg.reply(f'Пришли мне состав продукта через запятую, например: Кокосовая стружка, растворимое кукурузное волокно, изомальтоолигосахарид, инулин, вода очищенная. Узнай насколько вредны пищевые добавки.')
    
    


@dp.message_handler(content_types=['text'])
async def get_text_messages(msg: types.Message):
    prepared_text = prepare_text(msg.text)
    return_string = get_supplement_info(prepared_text)

    await msg.answer(return_string or "В составе нет пищевых добавок.", parse_mode="HTML") 


if __name__ == '__main__':
    executor.start_polling(dp)
