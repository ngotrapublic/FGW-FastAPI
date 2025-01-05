import uvicorn
from fastapi import FastAPI
from src.data.init import create_tables
from src.web import explorer, creature

app = FastAPI()
create_tables()

app.include_router(explorer.router)
app.include_router(creature.router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)