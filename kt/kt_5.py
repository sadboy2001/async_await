# Функция, которая запускает другую асинхронную функцию в отдельном потоке
async def run_in_thread(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func, *args)

# Асинхронная функция, которая имитирует длительную операцию
async def long_operation(x):
    await asyncio.sleep(5) # Имитация асинхронной операции
    return x * 2

# Тест, который проверяет, что функция корректно возвращает результат
@pytest.mark.asyncio
async def test_run_in_thread(event_loop):
    result = await run_in_thread(long_operation, 10) # Ждем выполнения функции в потоке
    assert result == 20 # Проверяем результат
