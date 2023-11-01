import aiosqlite


# ����������� ������� ��� ������� ������
async def insert_data():
    # ������� ����������� � ���� ������
    async with aiosqlite.connect("test.db") as db:
        # ��������� SQL-������ ��� ������� ������
        await db.execute(
            """
            INSERT INTO users (name, age) VALUES (?, ?)
            """,
            ("Alice", 25),
        )
        # ��������� ��������� � ���� ������
        await db.commit()
