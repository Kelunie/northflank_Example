from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {
        "mensaje": "Proyecto integrador III, desarrollado por el equipo 1",
        "plataforma": "Northflank"
    }