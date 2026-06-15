from flask import Flask

from calculator import Calculator
from endpoints import CalculatorEndpoints

app = Flask(__name__)

CalculatorEndpoints(app, Calculator())

@app.route('/')
def home():
    return {
        "mensaje": "Proyecto integrador III, desarrollado por el equipo 1",
        "plataforma": "Northflank"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
