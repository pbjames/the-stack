from __future__ import annotations

import sqlite3
from fastapi import FastAPI
from pydantic import BaseModel
from const import DATABASE_FILE, MIGRATION_FILE
from typer import Typer

app = FastAPI()
cli = Typer()
conn = sqlite3.connect(DATABASE_FILE)


class Todo(BaseModel):
    id: int | None
    creation_timestamp: int
    completion_timestamp: int
    content: str
    user_id: User


class User(BaseModel):
    id: int | None
    username: str
    password: str
    email: str


@cli.command()
def remake():
    with open(MIGRATION_FILE, "r") as fp:
        migration_commands = fp.read()
    with open(DATABASE_FILE, "w") as fp:
        fp.write("")
    conn = sqlite3.connect(DATABASE_FILE)
    conn.executescript(migration_commands)
    conn.commit()
    print("Database remade")


@app.get("/todos/{item_id}")
def read_todo(item_id: int) -> list[Todo]:
    cursor = conn.execute(f"SELECT * FROM todos WHERE id={item_id}")
    return cursor.fetchall()


@app.post("/todos/")
def create_todo(todo: Todo):
    values = f"VALUES ({todo.creation_timestamp},\
    {todo.completion_timestamp}, {todo.content}, {todo.user_id})"
    target = "todos(creation_timestamp, completion_timestamp, content, user_id)"
    conn.execute(f"INSERT {values} INTO {target}")


@app.get("/users/{user_id}")
def read_user(user_id: int) -> list[User]:
    cursor = conn.execute(f"SELECT * FROM users WHERE id={user_id}")
    return cursor.fetchall()


@app.post("/users")
def create_user(user: User):
    values = f"VALUES ({user.username}, {user.email})"
    target = "users(username, email)"
    conn.execute(f"INSERT {values} INTO {target}")


@app.get("users/{user_id}/todos")
def read_user_todos(user_id: int) -> list[Todo]:
    cursor = conn.execute(f"SELECT * FROM todos WHERE user_id={user_id}")
    return cursor.fetchall()


if __name__ == "__main__":
    cli()
