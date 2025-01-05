import uvicorn
from fastapi import FastAPI
from src.data.init import create_tables
from src.web import explorer, creature, user

app = FastAPI()
create_tables()

app.include_router(explorer.router, tags=["Explorer"])
app.include_router(creature.router, tags=["Creature"])
app.include_router(user.router, tags=["User"])

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)