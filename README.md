# Bellissimo - A recipe book API

This projects holds a REST API built with fastapi for the recipe book app.

## Local Development

1. Install docker
2. Run `docker compose up`
3. Go to http://localhost:8000/docs
## Local Development (without docker)

1. Create a new .env file and add the following tokens

```
DATABASE_URL=postgresql://admin:admin@localhost:5432/bellissimo
SECRET_KEY=546a7c2ea25f65b9aabcac39c72c4c42cd01869f4d30eec1f2820bfdbaceb796
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
APP=app
```

2. Run docker-compose up db

3. (If not installed) - pip3 install poetry
   1. Validate correct Python version (3.9.0)

4. (If not installed) - Install VsCode Python extension

5. Poetry install 

6. Poetry shell 

7. Copy returned path from the terminal and on the bottom right select the Python version.
   1. Change to Interpreter Path
   2. Paste the returned url (without `/activate`)


8. Create a launch file for Python - Module
   Ex:
   ```json
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Module",
                "type": "python",
                "request": "launch",
                "module": "uvicorn",
                "args": [
                    "main:app"
                ],
                "jinja": true
            }
        ]
    }
```

9. Go to http://127.0.0.1:8000/docs#/ to edit data
