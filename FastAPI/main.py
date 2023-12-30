# Write your code here :-)
from fastapi import FastAPI
from models import Todo
app= FastAPI()

# whatever method is below this decorator is responsible for handling any requests going into the '/'
@app.get('/')
async def root():
    return {'message': 'To-Do list implementation'}

todos= []

# create a todo
@app.post('/todos')
async def create_todos(todo: Todo):
    todos.append(todo)
    return {'message': 'Task has been added'}

# get all todos
@app.get('/todos')
async def get_todos():
    return {'todos': todos}

# get single todo
@app.get('/todos/{todo_id}')
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id== todo_id:
            return {'todo': todo}
    return {'message': 'No such task found'}

# update a todo
@app.put('/todos/{todo_id}')
async def update_todo(todo_id: int, todo_data: Todo):
    for todo in todos:
        if todo.id== todo_id:
            todo.id= todo_id
            todo.item= todo_data.item
            return {'todo': todo}
    return {'message': 'No such task found to update'}

# delete a todo
@app.delete('/todos/{todo_id}')
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id== todo_id:
            todos.remove(todo)
            return {'message': 'Task successfully deleted'}
    return {'message': 'No such task found'}
