# TodoFastAPI

A simple RESTful To-Do API built using **Python and FastAPI**.

This project demonstrates CRUD operations, path parameters, query parameters, asynchronous endpoints, Pydantic data validation, Swagger/OpenAPI documentation, and API testing using Postman.

## Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Swagger UI
- OpenAPI
- Postman

## Features

- Create a Todo
- Get all Todos
- Get a Todo by ID
- Filter Todos using query parameters
- Update a Todo using PUT
- Partially update a Todo using PATCH
- Delete a Todo
- Async endpoint using `async` and `await`
- Automatic API documentation using Swagger/OpenAPI
- API testing using Postman

Installation
pip install -r requirements.txt

How to run
uvicorn main:app --reload
API: http://127.0.0.1:8000

Swagger / OpenAPI
Swagger UI:
http://127.0.0.1:8000/docs

OpenAPI:
http://127.0.0.1:8000/openapi.json

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/todos` | Create a new Todo |
| GET | `/todos` | Get all Todos |
| GET | `/todos/{todo_id}` | Get Todo by ID |
| GET | `/todos/search` | Filter Todos using query parameter |
| PUT | `/todos/{todo_id}` | Update a Todo |
| PATCH | `/todos/{todo_id}` | Partially update a Todo |
| DELETE | `/todos/{todo_id}` | Delete a Todo |
| GET | `/async-todos` | Async Todo endpoint |


## Path Parameter

The API uses a path parameter to retrieve a specific Todo by its ID.

Example:

GET /todos/1

Here, `1` is the `todo_id` path parameter.




## Query Parameter

The API supports filtering Todos based on their completion status.

Example:

GET /todos/search?completed=true

This returns Todos where `completed` is `true`.

Another example:

GET /todos/search?completed=false

This returns Todos where `completed` is `false`.




## Async Endpoint

The project includes an asynchronous endpoint using Python's `async` and `await` keywords.

Example:

GET /async-todos

This endpoint demonstrates asynchronous request handling in FastAPI.


## Data Validation

Pydantic models are used to validate request and response data.

Example request:

```json
{
  "title": "Learning FastAPI",
  "completed": true
}

## Project Structure

```text
TodoFastAPI/
│
├── main.py
├── requirements.txt
├── README.md
│
├── screenshots/
│   ├── swagger.png
│   └── ...
│
└── postman/
    └── TodoFastAPI.postman_collection.json


