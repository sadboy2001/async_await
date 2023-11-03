import aiohttp
import asyncio
import os


async def download_file(url, folder):
    # Создаем имя файла из последней части URL
    filename = url.split("/")[-1]
    # Создаем путь к файлу в локальной папке
    filepath = os.path.join(folder, filename)
    # Создаем асинхронный клиент для HTTP-запросов
    async with aiohttp.ClientSession() as session:
        # Отправляем GET-запрос по URL
        async with session.get(url) as response:
            # Проверяем статус ответа
            if response.status == 200:
                # Читаем данные из ответа по частям
                with open(filepath, "wb") as file:
                    async for chunk in response.content.iter_chunked(1024):
                        # Записываем данные в файл
                        file.write(chunk)
                print(f"Файл {filename} успешно скачан")
            else:
                print(f"Ошибка при скачивании файла {filename}: {response.status}")


# Создаем список URL для скачивания
urls = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/dd/Big_%26_Small_Pumkins.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"
]

# Создаем имя папки для сохранения файлов
folder = "downloads"

# Создаем папку, если она не существует
if not os.path.exists(folder):
    os.mkdir(folder)

# Создаем список задач для скачивания файлов
tasks = [download_file(url, folder) for url in urls]

# Получаем цикл событий
loop = asyncio.get_event_loop()
# Запускаем все задачи параллельно и ждем их завершения
loop.run_until_complete(asyncio.gather(*tasks))