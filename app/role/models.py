from pydantic import BaseModel, Field
from typing import Optional

# Pydantic model for creating a Role
class RoleCreate(BaseModel):
    role_name: str = Field(max_length=255)

# Pydantic model for updating a Role
class RoleUpdate(BaseModel):
    role_name: Optional[str] = Field(max_length=255)

# Pydantic model for returning a Role
class RoleResponse(BaseModel):
    role_id: int
    role_name: str

    class Config:
        from_attributes = True

# Pydantic model for UsersRoles (linking Users and Roles)
class UsersRolesBase(BaseModel):
    users_roles_id: Optional[int] = Field(default=None)
    user_id: int
    role_id: int

# Pydantic model for Permissions
class PermissionsBase(BaseModel):
    permission_name: str = Field(max_length=255)
    role_id: int
