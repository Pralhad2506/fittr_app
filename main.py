from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.user.routes import router as user_router
from app.auth.routes import router as auth_router
from app.admin.routes import router as admin_router
from app.dietitian.routes import router as dietitian_router
from app.role.routes import router as role_router
import uvicorn


app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    return {"message": "server working!!"}

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(dietitian_router, prefix="/dietitian", tags=["dietitian"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(role_router, prefix="/role", tags=["role"])



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)