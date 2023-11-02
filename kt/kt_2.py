# �������, ������� ���������� ������
async def divide(x, y):
    await asyncio.sleep(1) # �������� ����������� ��������
    return x / y # ����� ������� ZeroDivisionError

# ����, ������� ���������, ��� ������� ����������� � ��������� �����������
@pytest.mark.asyncio
async def test_divide(event_loop):
    with pytest.raises(ZeroDivisionError): # ������� ����������
        result = await divide(10, 0) # ���� ���������� ��� ���������� �������
