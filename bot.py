import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.types.input_file import FSInputFile  # <-- Важно!

TOKEN = "7997196303:AAGPCnEIu_mNeEU8S-QSoZXQccOElfZmduw"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# Создаем клавиатуру
kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Студенты 👨‍🎓"), KeyboardButton(text="Тех документация")],
        [KeyboardButton(text="Презентация")]
    ],
    resize_keyboard=True  # Делаем кнопки компактными
)

@dp.message(F.text == "/start")  # Новый синтаксис для фильтрации команд
async def start(message: Message):
    await message.answer("Привет!", reply_markup=kb)

@dp.message(F.text == "Студенты 👨‍🎓")
async def students(message: Message):
    students_list = ["Толебек Алимансур", "Декабрь Еркежан"]
    await message.answer("\n".join(students_list))

@dp.message(F.text == "Тех документация")
async def send_tech_doc(message: Message):
    file_path = "/Users/mackbook/my_telegram_bot/aaa.docx"  # Укажи правильный путь
    try:
        document = FSInputFile(file_path)  # <-- Используем FSInputFile
        await message.answer_document(document, caption="Техническая документация")
    except Exception as e:
        await message.answer(f"Ошибка при отправке файла: {e}")

@dp.message(F.text == "Презентация")
async def send_presentation(message: Message):
    file_path = "/Users/mackbook/my_telegram_bot/presentation.pptx"  # Укажи правильный путь
    try:
        document = FSInputFile(file_path)  # <-- Используем FSInputFile
        await message.answer_document(document, caption="Презентация")
    except Exception as e:
        await message.answer(f"Ошибка при отправке файла: {e}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
