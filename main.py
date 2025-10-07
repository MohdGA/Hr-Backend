
from fastapi import FastAPI
from controllers.hr import router as HrRouter
from controllers.user import router as UserRouter
from controllers.leave import router as LeaveRouter
from controllers.performance import router as PerformanceRouter
from fastapi.middleware.cors import CORSMiddleware
from config.environment import os

app = FastAPI()

origins = [
    'http://localhost:5173'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

app.include_router(HrRouter, prefix='/api')
app.include_router(UserRouter, prefix='/api')
app.include_router(LeaveRouter, prefix='/api')
app.include_router(PerformanceRouter, prefix='/api')

@app.get('/')
def home():
    return {'message': "Hello World!"}


if os.getenv("APP_ENV", "development") != "production":
    # load .env only locally
    from dotenv import load_dotenv
    load_dotenv()
