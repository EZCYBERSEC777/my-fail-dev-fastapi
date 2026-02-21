from fastapi import FastAPI 
from workout_api.routers import api_router 

app = FastAPI(title='WorkoutApi')
app.iclude_router(api_router)