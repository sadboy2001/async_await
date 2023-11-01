import aiohttp
import asyncio
import os


async def download_file(url, folder):
    # ������� ��� ����� �� ��������� ����� URL
    filename = url.split("/")[-1]
    # ������� ���� � ����� � ��������� �����
    filepath = os.path.join(folder, filename)
    # ������� ����������� ������ ��� HTTP-��������
    async with aiohttp.ClientSession() as session:
        # ���������� GET-������ �� URL
        async with session.get(url) as response:
            # ��������� ������ ������
            if response.status == 200:
                # ������ ������ �� ������ �� ������
                with open(filepath, "wb") as file:
                    async for chunk in response.content.iter_chunked(1024):
                        # ���������� ������ � ����
                        file.write(chunk)
                print(f"���� {filename} ������� ������")
            else:
                print(f"������ ��� ���������� ����� {filename}: {response.status}")


# ������� ������ URL ��� ����������
urls = [
    "https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg",
    "https://upload.wikimedia.org/wikipedia/commons/d/dd/Big_%26_Small_Pumkins.JPG",
    "https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg"
]

# ������� ��� ����� ��� ���������� ������
folder = "downloads"

# ������� �����, ���� ��� �� ����������
if not os.path.exists(folder):
    os.mkdir(folder)

# ������� ������ ����� ��� ���������� ������
tasks = [download_file(url, folder) for url in urls]

# �������� ���� �������
loop = asyncio.get_event_loop()
# ��������� ��� ������ ����������� � ���� �� ����������
loop.run_until_complete(asyncio.gather(*tasks))