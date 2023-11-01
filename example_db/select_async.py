import aiosqlite


# ����������� ������� ��� ������� ������
async def select_data():
    # ������� ����������� � ���� ������
    async with aiosqlite.connect("test.db") as db:
        # ��������� SQL-������ ��� ������� ������
        async with db.execute(
            """
            SELECT * FROM users WHERE age > ?
            """,
            (20,),
        ) as cursor:
            # �������� �� ����������� ������� � ������� ������������ �����
            async for row in cursor:
                # ������� ������ �� ������ ������
                print(row["id"], row["name"], row["age"])
