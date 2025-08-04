# db_connection.py
from sqlalchemy.ext.asyncio import create_async_engine

# Database connection class
class DatabaseConnection:
    def __init__(self):
        self.database_url = "postgresql+asyncpg://root:root@localhost:5432/zyter"
        self.engine = create_async_engine(self.database_url)

    def get_sql_engine(self):
        return self.engine

    async def close(self):
        await self.engine.dispose()