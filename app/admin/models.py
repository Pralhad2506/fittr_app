from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field
from sqlalchemy import Table, MetaData
from pydantic import BaseModel
# Metadata instance to track existing tables
metadata = MetaData()

class Dietitian(SQLModel, table=True):
    __tablename__ = "dietitian"  # Ensure the table name is correct
    __table_args__ = {"extend_existing": True}  # Add this line to extend the existing table

    # dietitian_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False)
    name: str = Field(max_length=255, nullable=False)  # Added name
    email: str = Field(max_length=255, nullable=False)  # Added email
    qualification: str = Field(max_length=255, nullable=False)
    experience_years: int = Field(nullable=False)
