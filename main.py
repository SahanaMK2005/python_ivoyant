from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


# pydantic Request model
class TodoCreate(BaseModel):
    title: str
    completed: bool = False


# Response model
class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool


# Temporary database
todos = []


# 1. GET - Home
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}


# 2. POST - Create Todo
@app.post("/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": todo.completed
    }

    todos.append(new_todo)
    return new_todo


# 3. GET - Get all Todos
@app.get("/todos", response_model=list[TodoResponse])
def get_todos():
    return todos


# 4. GET - Get Todo by ID
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(status_code=404, detail="Todo not found")


# 5. PUT - Update Todo
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, todo: TodoCreate):
    for item in todos:
        if item["id"] == todo_id:
            item["title"] = todo.title
            item["completed"] = todo.completed
            return item

    raise HTTPException(status_code=404, detail="Todo not found")


# 6. PATCH - Partially Update Todo
@app.patch("/todos/{todo_id}", response_model=TodoResponse)
def partial_update_todo(todo_id: int, todo: TodoCreate):
    for item in todos:
        if item["id"] == todo_id:
            item["title"] = todo.title
            item["completed"] = todo.completed
            return item

    raise HTTPException(status_code=404, detail="Todo not found")


# 7. DELETE - Delete Todo
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(index)
            return {
                "message": "Todo deleted successfully",
                "todo": deleted_todo
            }

    raise HTTPException(status_code=404, detail="Todo not found")