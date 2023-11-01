import asyncio


async def read_from_queue(queue):
    # Пока очередь не пуста
    while not queue.empty():
        # Извлекаем элемент из очереди
        item = await queue.get()
        # Возвращаем элемент как результат генератора
        yield item

# Создаем очередь asyncio
queue = asyncio.Queue()
# Добавляем несколько элементов в очередь
queue.put_nowait("Hello")
queue.put_nowait("World")
queue.put_nowait("!")

# Создаем асинхронный генератор из очереди
generator = read_from_queue(queue)
# Проходим по элементам генератора с помощью цикла for
async for item in generator:
    print(item)
