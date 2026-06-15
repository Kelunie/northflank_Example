# Northflank Test

This repository is a small test project for deploying a simple calculator API to Northflank.

Main files

- [app.py](app.py): Flask application entry point.
- [endpoints.py](endpoints.py#L1-L80): defines the calculator endpoints.
- [calculator.py](calculator.py#L1-L200): calculator operation logic.

Run locally

1. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

2. Run the app:

```bash
python app.py
```

The app listens by default on `http://0.0.0.0:8080`.

Available endpoints

- GET `/` — Root
  - Returns: JSON with a message and the platform.
  - Example:
    ```bash
    curl http://localhost:8080/
    ```
    Expected response:
    ```json
    {
      "mensaje": "Proyecto integrador III, desarrollado por el equipo 1",
      "plataforma": "Northflank"
    }
    ```

- GET `/calc/add?a=<num>&b=<num>` — Add
  - Query parameters: `a`, `b` (numbers, required)
  - Response: `{ "result": <number>, "operation": "add" }`

- GET `/calc/subtract?a=<num>&b=<num>` — Subtract
  - Response: `{ "result": <number>, "operation": "subtract" }`

- GET `/calc/multiply?a=<num>&b=<num>` — Multiply
  - Response: `{ "result": <number>, "operation": "multiply" }`

- GET `/calc/divide?a=<num>&b=<num>` — Divide
  - If `b` is 0, returns HTTP 400 with `{"error": "No se puede dividir por cero"}`.
  - Response: `{ "result": <number>, "operation": "divide" }`

- GET `/calc/power?a=<num>&b=<num>` — Power (a^b)
  - Response: `{ "result": <number>, "operation": "power" }`

Common errors

- If `a` or `b` are missing or invalid, endpoints return HTTP 400 and a JSON `{ "error": "..." }`.

Usage example

```bash
curl "http://localhost:8080/calc/add?a=3&b=2"

# Response
# {"result":5.0,"operation":"add"}
```
