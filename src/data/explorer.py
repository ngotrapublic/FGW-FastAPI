# from .init import curs
from src.data.init import get_db
from src.model.explorer import Explorer
from error import Missing, Duplicate
from sqlalchemy import exc
from src.data.schemas import ExplorerBase


# curs.execute("""create table if not exists explorer(
#                 name text primary key,
#                 country text,
#                 description text)""")

def row_to_model(row: tuple) -> Explorer:
    name, country, description = row
    return Explorer(name=name,
        country=country, description=description)

def model_to_dict(explorer: Explorer) -> dict:
    return explorer.model_dump()

def get_all() -> list[ExplorerBase]:
    db = get_db()
    return db.query(Explorer).all()

# def get_one(name: str) -> Explorer:
#     qry = "select * from explorer where name=:name"
#     params = {"name": name}
#     curs.execute(qry, params)
#     row = curs.fetchone()
#     if row:
#         return row_to_model(row)
#     else:
#         raise Missing(msg=f"Explorer {name} not found")

# def get_all() -> list[Explorer]:
#     qry = "select * from explorer"
#     curs.execute(qry)
#     return [row_to_model(row) for row in curs.fetchall()]

# def create(explorer: Explorer) -> Explorer:
#     if not explorer: return None
#     qry = """insert into explorer (name, country, description) values
#              (:name, :country, :description)"""
#     params = model_to_dict(explorer)
#     try:
#         curs.execute(qry, params)
#         return get_one(explorer.name)
#     except exc.IntegrityError:
#         raise Duplicate(msg=
#             f"Explorer {explorer.name} already exists")

# def modify(name: str, explorer: Explorer) -> Explorer:
#     if not (name and explorer): return None
#     qry = """update explorer
#              set name=:name,
#              country=:country,
#              description=:description
#              where name=:name_orig"""
#     params = model_to_dict(explorer)
#     params["name_orig"] = explorer.name
#     curs.execute(qry, params)
#     if curs.rowcount == 1:
#         return get_one(explorer.name)
#     else:
#         raise Missing(msg=f"Explorer {name} not found")

# def delete(name: str):
#     if not name: return False
#     qry = "delete from explorer where name = :name"
#     params = {"name": name}
#     curs.execute(qry, params)
#     if curs.rowcount != 1:
#         raise Missing(msg=f"Explorer {name} not found")