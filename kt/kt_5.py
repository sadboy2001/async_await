# �������, ������� ��������� ������ ����������� ������� � ��������� ������
async def run_in_thread(func, *args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, func, *args)

# ����������� �������, ������� ��������� ���������� ��������
async def long_operation(x):
    await asyncio.sleep(5) # �������� ����������� ��������
    return x * 2

# ����, ������� ���������, ��� ������� ��������� ���������� ���������
@pytest.mark.asyncio
async def test_run_in_thread(event_loop):
    result = await run_in_thread(long_operation, 10) # ���� ���������� ������� � ������
    assert result == 20 # ��������� ���������
