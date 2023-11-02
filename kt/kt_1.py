# �������, ������� ���������� ������
async def get_data():
    await asyncio.sleep(1) # �������� ����������� ��������
    return "Hello"

# ����, ������� ���������, ��� ������� ����������� � ��������� ���������
@pytest.mark.asyncio
async def test_get_data(event_loop):
    result = await get_data() # ���� ���������� �������
    assert result == "Hello" # ��������� ��������
