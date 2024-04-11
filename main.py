from fastapi import FastAPI, Request, HTTPException, Form
from fastapi.responses import HTMLResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi_htmx import htmx, htmx_init

app = FastAPI()


# Definicja modelu Todo
class Todo(BaseModel):
    id: int
    title: str
    completed: bool


# Model Pydantic do tworzenia nowego zadania
class TodoCreate(BaseModel):
    title: str


# Baza danych w pamięci
db = []

# Ładowanie szablonów HTML i HTMX
templates = Jinja2Templates(directory="templates")
htmx_init(templates=templates, file_extension="html")


# Endpoint API do dodawania nowego zadania
@app.post("/todos", response_class=HTMLResponse)
@htmx("record")
async def create_todo(request: Request, title: dict[str, str]):
    new_todo = Todo(id=max(t.id for t in db) + 1 if db else 1, title=title["title"], completed=False)
    db.append(new_todo)
    return {"todo": new_todo}


# Endpoint API do aktualizacji zadania
@app.put("/todos/{todo_id}", response_class=HTMLResponse)
@htmx("record")
async def update_todo(request: Request, todo_id: int, completed: dict[str, str] = {}):
    for t in db:
        if t.id == todo_id:
            t.completed = bool(completed)
            return {"todo": t}
    raise HTTPException(status_code=404, detail="Todo not found")


# Endpoint API do usuwania zadania
@app.delete("/todos/{todo_id}", response_class=Response)
@htmx("nothing")
async def delete_todo(request: Request, todo_id: int):
    for i, t in enumerate(db):
        if t.id == todo_id:
            del db[i]
            return Response(status_code=200)
    raise HTTPException(status_code=404, detail="Todo not found")


# Główny endpoint serwujący plik index.html
@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "todos": db})
