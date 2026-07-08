import aiosqlite

DB_NAME = "data/rose.db"

async def init_db():
    async with aiosqlite.connect(DB_NAME) as db:
        await db.execute("""
        CREATE TABLE IF NOT EXISTS warns (
            user_id INTEGER,
            chat_id INTEGER,
            warns INTEGER DEFAULT 0,
            PRIMARY KEY (user_id, chat_id)
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            chat_id INTEGER PRIMARY KEY,
            welcome INTEGER DEFAULT 1,
            antilink INTEGER DEFAULT 0
        )
        """)

        await db.commit()
