from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from models.member import Member
from utility_module.db_config import DatabaseConnection


class MemberOperations:
    def __init__(self):
        self.db_conn = DatabaseConnection()

    async def get_all_members(self) -> List[Member]:
        async with AsyncSession(self.db_conn.get_sql_engine()) as session:
            result = await session.execute(select(Member))
            return list(result.scalars().all())

    async def get_member_by_id(self, member_id: str) -> Optional[Member]:
        async with AsyncSession(self.db_conn.get_sql_engine()) as session:
            result = await session.execute(select(Member).where(Member.memberid == member_id))
            return result.scalars().first()