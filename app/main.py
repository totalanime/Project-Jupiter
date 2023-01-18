from fastapi import FastAPI
from .movies import Movie

app = FastAPI(title="FastAPI by TotalAnime")


@app.get('/')
def home():
    return {'Запуск':'Выполнен успешно'}


@app.get('/{me}')
def get_item(me: int, q: int = None):
    return {'key': me, 'q': q}

#/"Укажите целое число"?q= "Укажите в виде строки"

@app.get('/user/{me}/items/{item}')
def get_user_item(me: int, item: str):
    return {'user': me, 'item': item}


@app.post('/Movie')
def createmovie(item: Movie):
    return item