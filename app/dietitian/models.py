from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

# Diet Plan model
class DietPlan(SQLModel, table=True):
    __tablename__ = "dietplan"
    __table_args__ = {"extend_existing": True}  # Allow redefinition if already exists
    diet_plan_id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.user_id", nullable=False)
    dietitian_id: int = Field(foreign_key="user.user_id", nullable=False)  # Links to the dietitian
    proteins: float = Field(nullable=False)
    carbs: float = Field(nullable=False)
    fats: float = Field(nullable=False)
    plan_status: str = Field(default="active", max_length=20)
