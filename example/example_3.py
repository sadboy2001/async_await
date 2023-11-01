import asyncio
import time
import functools


def measure_time(func):
    # ��������� ��� ��������� ������� ���������� ����������� �������

    # ���������� functools.wraps ��� ���������� ���������� �������
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        # ���������� ����� ������ ���������� �������
        start = time.time()
        # �������� ������������ ������� � �������� ���������
        result = await func(*args, **kwargs)
        # ���������� ����� ��������� ���������� �������
        end = time.time()
        # ��������� ������� �� ������� � ������� �� �����
        duration = end - start
        print(f"������� {func.__name__} ����������� {duration} ������")
        # ���������� ��������� ������������ �������
        return result

    return wrapper


@measure_time
async def say_hello():
    # ������ ����������� �������, ������� ���� 1 ������� � ������� �����������

    await asyncio.sleep(1)
    print("Hello")


# ��������� ��������� � ����������� ������� � �������� ��
asyncio.run(say_hello())