import aiosqlite


# Асинхронная функция для вставки данных
async def insert_data():
    # Создаем подключение к базе данных
    async with aiosqlite.connect("test.db") as db:
        # Выполняем SQL-запрос для вставки данных
        await db.execute(
            """
            INSERT INTO users (name, age) VALUES (?, ?)
            """,
            ("Alice", 25),
        )
        # Сохраняем изменения в базе данных
        await db.commit()
