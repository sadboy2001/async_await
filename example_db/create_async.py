import aiosqlite


# ����������� ������� ��� �������� �������
async def create_table():
    # ������� ����������� � ���� ������
    async with aiosqlite.connect("test.db") as db:
        # ��������� SQL-������ ��� �������� �������
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER
            )
            """
        )
        # ��������� ��������� � ���� ������
        await db.commit()
