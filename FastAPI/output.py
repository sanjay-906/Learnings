import requests

#print("Display all todos:")
#print("Create a todo:")
#print("Update a todo:")
#print("Display single todo:")
#print("Delete a todo:")
#print(
    #requests.post(
    #    "http://127.0.0.1:8000/",
    #    json={"name": "Screwdriver", "price": 3.99, "count": 10, "id": 4, "category": "tools"},
    #).json()
#)

print("Root")
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("1. Create a todo")
print(
    requests.post(
        "http://127.0.0.1:8000/todos",
        json= { "id": 0,
                "item": "Apple Juice"}).json())
print(
    requests.post(
        "http://127.0.0.1:8000/todos",
        json= { "id": 1,
                "item": "Orange Juice"}).json())
print(
    requests.post(
        "http://127.0.0.1:8000/todos",
        json= { "id": 2,
                "item": "Watermelon Juice"}).json())
print()

print("2. Get all todos")
print(requests.get("http://127.0.0.1:8000/todos").json())
print()

print("3. Get a single todo")
print(requests.get("http://127.0.0.1:8000/todos/2").json())
print()


print("4. Update a todo:")
print(requests.put("http://127.0.0.1:8000/todos/1",
                    json= { "id": 1,
                "item": "I dont like Orange Juice"}).json())
#?item=orange juice").json())
print()

print("5. Get all todos")
print(requests.get("http://127.0.0.1:8000/todos").json())
print()

print("6. Deleting an item:")
print(requests.delete("http://127.0.0.1:8000/todos/1").json())
print()

print("7. Get all todos")
print(requests.get("http://127.0.0.1:8000/todos").json())
print()
