# Функция, которая возвращает промис
async def divide(x, y):
    await asyncio.sleep(1) # Имитация асинхронной операции
    return x / y # Может вызвать ZeroDivisionError

# Тест, который проверяет, что функция отклоняется с ожидаемым исключением
@pytest.mark.asyncio
async def test_divide(event_loop):
    with pytest.raises(ZeroDivisionError): # Ожидаем исключение
        result = await divide(10, 0) # Ждем разрешения или отклонения промиса
