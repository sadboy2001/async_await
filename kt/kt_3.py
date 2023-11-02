# Функция, которая выполняет HTTP-запрос к внешнему API
async def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["main"]["temp"]

# Тест, который проверяет, что функция возвращает корректный ответ
@pytest.mark.asyncio
async def test_get_weather(event_loop):
    temp = await get_weather("Moscow") # Ждем ответа от API
    assert isinstance(temp, float) # Проверяем тип ответа
    assert temp > -50 and temp < 50 # Проверяем диапазон ответа
