import aiosqlite


# Асинхронная функция для создания таблицы
async def create_table():
    # Создаем подключение к базе данных
    async with aiosqlite.connect("test.db") as db:
        # Выполняем SQL-запрос для создания таблицы
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
            """
        )
        # Сохраняем изменения в базе данных
        await db.commit()
