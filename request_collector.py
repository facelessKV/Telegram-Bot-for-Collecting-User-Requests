import logging
import os
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    Message, 
    CallbackQuery,
    ReplyKeyboardRemove
)
import asyncio
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Настраиваем логирование
logging.basicConfig(level=logging.INFO)

# Токен бота из переменной окружения
# Создайте файл .env и добавьте строку: BOT_TOKEN=ваш_токен
BOT_TOKEN = os.getenv("BOT_TOKEN")

# ID чата администратора/группы, куда будут отправляться заявки
# В файле .env добавьте: ADMIN_CHAT_ID=ваш_id_чата
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

# Инициализируем роутер
router = Router()

# Определяем состояния для FSM (машины состояний)
class Form(StatesGroup):
    name = State()       # Состояние ожидания имени
    phone = State()      # Состояние ожидания телефона
    email = State()      # Состояние ожидания email
    comment = State()    # Состояние ожидания комментария
    confirmation = State()  # Состояние подтверждения данных

# Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message, state: FSMContext):
    """
    Обрабатывает команду /start, начинает сбор данных
    """
    # Сбрасываем предыдущее состояние, если было
    await state.clear()
    
    # Отправляем приветственное сообщение и запрашиваем имя
    await message.answer(
        "Привет! Я бот для сбора заявок.\n"
        "Давайте заполним форму. Для отмены нажмите /cancel.\n\n"
        "Как вас зовут?"
    )
    
    # Устанавливаем состояние ожидания имени
    await state.set_state(Form.name)

# Обработчик команды /cancel
@router.message(Command("cancel"))
async def cmd_cancel(message: Message, state: FSMContext):
    """
    Позволяет пользователю отменить заполнение формы
    """
    # Проверяем, находится ли пользователь в процессе заполнения
    current_state = await state.get_state()
    if current_state is None:
        # Если нет активного состояния, ничего не делаем
        return
    
    # Сбрасываем состояние и уведомляем пользователя
    await state.clear()
    await message.answer(
        "Заполнение формы отменено.",
        reply_markup=ReplyKeyboardRemove()
    )

# Обработчик ввода имени
@router.message(Form.name)
async def process_name(message: Message, state: FSMContext):
    """
    Обрабатывает ввод имени пользователя
    """
    # Сохраняем имя в хранилище состояний
    await state.update_data(name=message.text)
    
    # Запрашиваем номер телефона
    await message.answer("Спасибо! Теперь введите ваш номер телефона:")
    
    # Переходим к состоянию ожидания телефона
    await state.set_state(Form.phone)

# Обработчик ввода телефона
@router.message(Form.phone)
async def process_phone(message: Message, state: FSMContext):
    """
    Обрабатывает ввод телефона пользователя
    """
    # Здесь можно добавить валидацию номера телефона
    # Например, проверить формат с помощью регулярного выражения
    
    # Сохраняем телефон в хранилище состояний
    await state.update_data(phone=message.text)
    
    # Запрашиваем email
    await message.answer("Отлично! Теперь введите ваш email:")
    
    # Переходим к состоянию ожидания email
    await state.set_state(Form.email)

# Обработчик ввода email
@router.message(Form.email)
async def process_email(message: Message, state: FSMContext):
    """
    Обрабатывает ввод email пользователя
    """
    # Здесь можно добавить валидацию email
    # Например, проверить наличие @ и домена
    
    # Сохраняем email в хранилище состояний
    await state.update_data(email=message.text)
    
    # Запрашиваем комментарий
    await message.answer("Почти готово! Оставьте комментарий к заявке:")
    
    # Переходим к состоянию ожидания комментария
    await state.set_state(Form.comment)

# Обработчик ввода комментария
@router.message(Form.comment)
async def process_comment(message: Message, state: FSMContext):
    """
    Обрабатывает ввод комментария и показывает все собранные данные
    """
    # Сохраняем комментарий в хранилище состояний
    await state.update_data(comment=message.text)
    
    # Получаем все собранные данные
    data = await state.get_data()
    
    # Формируем сообщение для подтверждения
    confirmation_text = (
        "Проверьте введенные данные:\n\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Email: {data['email']}\n"
        f"Комментарий: {data['comment']}"
    )
    
    # Создаем клавиатуру с кнопками подтверждения и отмены
    confirm_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Подтвердить", callback_data="confirm")],
            [InlineKeyboardButton(text="Отменить", callback_data="cancel")]
        ]
    )
    
    # Отправляем сообщение с кнопками
    await message.answer(confirmation_text, reply_markup=confirm_kb)
    
    # Переходим к состоянию ожидания подтверждения
    await state.set_state(Form.confirmation)

# Обработчик нажатия кнопки "Подтвердить"
@router.callback_query(Form.confirmation, F.data == "confirm")
async def process_confirm(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает подтверждение заявки пользователем
    """
    # Получаем все данные
    data = await state.get_data()
    
    # Формируем сообщение для администратора
    admin_message = (
        "Новая заявка!\n\n"
        f"Имя: {data['name']}\n"
        f"Телефон: {data['phone']}\n"
        f"Email: {data['email']}\n"
        f"Комментарий: {data['comment']}\n\n"
        f"От пользователя: @{callback.from_user.username or 'Нет юзернейма'} "
        f"(ID: {callback.from_user.id})"
    )
    
    # Отправляем сообщение администратору
    await callback.bot.send_message(ADMIN_CHAT_ID, admin_message)
    
    # Благодарим пользователя
    await callback.message.edit_text(
        "Спасибо! Ваша заявка отправлена.\n"
        "Мы свяжемся с вами в ближайшее время."
    )
    
    # Сбрасываем состояние
    await state.clear()
    
    # Отвечаем на callback_query, чтобы убрать индикатор загрузки
    await callback.answer()

# Обработчик нажатия кнопки "Отменить"
@router.callback_query(Form.confirmation, F.data == "cancel")
async def process_cancel(callback: CallbackQuery, state: FSMContext):
    """
    Обрабатывает отмену заявки пользователем
    """
    # Сообщаем об отмене заявки
    await callback.message.edit_text("Заявка отменена.")
    
    # Сбрасываем состояние
    await state.clear()
    
    # Отвечаем на callback_query, чтобы убрать индикатор загрузки
    await callback.answer()

# Основная функция запуска бота
async def main():
    """
    Основная функция для запуска бота
    """
    # Инициализируем бота и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    
    # Регистрируем роутер в диспетчере
    dp.include_router(router)
    
    # Пропускаем накопившиеся апдейты и запускаем поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # Запускаем бота
    asyncio.run(main())