# �������, ������� ��������� HTTP-������ � �������� API
async def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return data["main"]["temp"]

# ����, ������� ���������, ��� ������� ���������� ���������� �����
@pytest.mark.asyncio
async def test_get_weather(event_loop):
    temp = await get_weather("Moscow") # ���� ������ �� API
    assert isinstance(temp, float) # ��������� ��� ������
    assert temp > -50 and temp < 50 # ��������� �������� ������
