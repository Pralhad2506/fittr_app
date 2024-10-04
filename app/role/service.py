from sqlmodel import Session, select, delete
from app.role.models import RoleCreate, RoleUpdate, RoleResponse, UsersRolesBase
from models import Role  # Ensure this imports the SQLModel class
from models import Permissions
from app.role.models import PermissionsBase
def create_role_service(session: Session, role: RoleCreate) -> RoleResponse:
    db_role = Role(role_name=role.role_name)
    session.add(db_role)
    session.commit()
    session.refresh(db_role)
    return RoleResponse.from_orm(db_role)

def get_roles_service(session: Session) -> list[RoleResponse]:
    roles = session.exec(select(Role)).all()
    return [RoleResponse.from_orm(role) for role in roles]

def update_role_service(session: Session, role_id: int, role_update: RoleUpdate) -> RoleResponse:
    role = session.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    if role_update.role_name:
        role.role_name = role_update.role_name
    
    session.add(role)
    session.commit()
    session.refresh(role)
    return RoleResponse.from_orm(role)

def delete_role_service(session: Session, role_id: int):
    role = session.get(Role, role_id)
    if not role:
        raise HTTPException(status_code=404, detail="Role not found")
    
    session.delete(role)
    session.commit()
def create_permission_service(session: Session, permission: PermissionsBase) -> Permissions:
    db_permission = Permissions(permission_name=permission.permission_name, role_id=permission.role_id)
    session.add(db_permission)
    session.commit()
    session.refresh(db_permission)
    return db_permission

def get_permissions_service(session: Session) -> list[Permissions]:
    permissions = session.exec(select(Permissions)).all()
    return permissions

def update_permission_service(session: Session, permission_id: int, permission_update: PermissionsBase) -> Permissions:
    permission = session.get(Permissions, permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    
    if permission_update.permission_name:
        permission.permission_name = permission_update.permission_name
    
    session.add(permission)
    session.commit()
    session.refresh(permission)
    return permission
def delete_permission_service(session: Session, permission_id: int):
    permission = session.get(Permissions, permission_id)
    if not permission:
        raise HTTPException(status_code=404, detail="Permission not found")
    
    session.delete(permission)
    session.commit()