from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select, delete
from app.role.models import RoleCreate, RoleUpdate, RoleResponse,PermissionsBase
from app.role.service import create_role_service, get_roles_service, update_role_service, delete_role_service,create_permission_service,get_permissions_service,delete_permission_service,update_permission_service
from db import get_session
from models import Permissions
router = APIRouter()

# Route to create a new role
@router.post("/roles/", response_model=RoleResponse)
def create_role(role: RoleCreate, session: Session = Depends(get_session)):
    return create_role_service(session, role)

# Route to get all roles
@router.get("/roles/", response_model=list[RoleResponse])
def get_roles(session: Session = Depends(get_session)):
    return get_roles_service(session)

# Route to update a role
@router.put("/roles/{role_id}", response_model=RoleResponse)
def update_role(role_id: int, role_update: RoleUpdate, session: Session = Depends(get_session)):
    return update_role_service(session, role_id, role_update)

# Route to delete a role
@router.delete("/roles/{role_id}", response_model=dict)
def delete_role(role_id: int, session: Session = Depends(get_session)):
    delete_role_service(session, role_id)
    return {"message": "Role deleted successfully"}

@router.post("/permissions/", response_model=PermissionsBase)
def create_permission(permission: PermissionsBase, session: Session = Depends(get_session)):
    return create_permission_service(session, permission)

# Route to get all permissions
@router.get("/permissions/", response_model=list[PermissionsBase])
def get_permissions(session: Session = Depends(get_session)):
    return get_permissions_service(session)

# Route to update a permission
@router.put("/permissions/{permission_id}", response_model=PermissionsBase)
def update_permission(permission_id: int, permission_update: PermissionsBase, session: Session = Depends(get_session)):
    return update_permission_service(session, permission_id, permission_update)

# Route to delete a permission
@router.delete("/permissions/{permission_id}", response_model=dict)
def delete_permission(permission_id: int, session: Session = Depends(get_session)):
    delete_permission_service(session, permission_id)
    return {"message": "Permission deleted successfully"}
