import asyncio
import time
import functools


def measure_time(func):
    # Декоратор для измерения времени выполнения асинхронной функции

    # Используем functools.wraps для сохранения метаданных функции
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # Запоминаем время начала выполнения функции
        start = time.time()
        # Вызываем оригинальную функцию и получаем результат
        result = await func(*args, **kwargs)
        # Запоминаем время окончания выполнения функции
        end = time.time()
        # Вычисляем разницу во времени и выводим на экран
        duration = end - start
        print(f"Функция {func.__name__} выполнялась {duration} секунд")
        # Возвращаем результат оригинальной функции
        return result

    return wrapper


@measure_time
async def say_hello():
    # Пример асинхронной функции, которая ждет 1 секунду и выводит приветствие

    await asyncio.sleep(1)
    print("Hello")


# Применяем декоратор к асинхронной функции и вызываем ее
asyncio.run(say_hello())