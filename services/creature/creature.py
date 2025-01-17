import uvicorn
from fastapi import FastAPI
from src.web import creature
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8003",
]

app = FastAPI(swagger_ui_parameters={"displayModelsExpandDepth": -1})
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(creature.router, tags=["Creature"])

if __name__ == "__main__":
    uvicorn.run("creature:app", reload=True, host="0.0.0.0", port=8001)