# Функция, которая возвращает промис
async def get_data():
    await asyncio.sleep(1) # Имитация асинхронной операции
    return "Hello"

# Тест, который проверяет, что функция разрешается с ожидаемым значением
@pytest.mark.asyncio
async def test_get_data(event_loop):
    result = await get_data() # Ждем разрешения промиса
    assert result == "Hello" # Проверяем значение
