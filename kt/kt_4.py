# �������, ������� �������� � ����� ������
async def add_user(name, age):
    conn = await aiopg.connect("dbname=test user=postgres")
    cur = await conn.cursor()
    await cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    await cur.execute("SELECT id FROM users WHERE name = %s", (name,))
    id = await cur.fetchone()
    await cur.close()
    await conn.close()
    return id

# ����, ������� ���������, ��� ������� ��������� ��������� ����� ������
@pytest.mark.asyncio
async def test_add_user(event_loop):
    id = await add_user("Alice", 25) # ���� ���������� ������
    assert isinstance(id, int) # ��������� ��� ��������������
    conn = await aiopg.connect("dbname=test user=postgres")
    cur = await conn.cursor()
    await cur.execute("SELECT name, age FROM users WHERE id = %s", (id,))
    name, age = await cur.fetchone()
    await cur.close()
    await conn.close()
    assert name == "Alice" # ��������� ���
    assert age == 25 # ��������� �������
