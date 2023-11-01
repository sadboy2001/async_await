import aiosqlite


# Асинхронная функция для выборки данных
async def select_data():
    # Создаем подключение к базе данных
    async with aiosqlite.connect("test.db") as db:
        # Выполняем SQL-запрос для выборки данных
        async with db.execute(
            """
            SELECT * FROM users WHERE age > ?
            """,
            (20,),
        ) as cursor:
            # Проходим по результатам выборки с помощью асинхронного цикла
            async for row in cursor:
                # Выводим данные из каждой строки
                print(row["id"], row["name"], row["age"])
