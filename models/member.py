# models/member.py
from datetime import date
from typing import List

from sqlmodel import SQLModel, Field
from sqlalchemy import Column, ARRAY, Text


class Member(SQLModel, table=True):
    __tablename__ = "member"

    objecttype: str = Field(default="Member")
    memberid: str = Field(primary_key=True)
    dob: date
    plantype: str
    pcp: str
    umrequests: List[str] = Field(sa_column=Column(ARRAY(Text)))
    careplans: List[str] = Field(sa_column=Column(ARRAY(Text)))