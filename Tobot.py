from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

class CardTobot(BaseModel):
    pilot: str
    tobot: str
    level: int = Field(ge=1, le=10)
class CardTobotID(CardTobot):
    id: int

db_tobot = []

id_tobot = 1

@app.get("/")
def register_card_tobot(request: Request):
    docs_url = f"{request.base_url}docs"
    return {"Регистрация карточки Тобота": "Чтобы зарегистрировать карточку Тобота, необходимо заполнить карточку на сайте по ссылке", "Сайт": docs_url}

@app.get("/data_card_tobot")
def data_card_tobot():
    return {"Команда Тоботов": db_tobot}

@app.get("/search_card_tobot/{tobot_id")
def search_card_tobot(tobot_id: int):
    for t in db_tobot:
        if t.id == tobot_id:
            return f"ID: {tobot_id} - Пилот {t.pilot}и его Тобот {t.tobot}"
    raise HTTPException(status_code=404, detail=f"Не существует Пилота и его Тобота с ID: {tobot_id}")

@app.post("/create_card_tobot")
def create_card_tobot(tobot: CardTobot):
    global id_tobot

    for t in db_tobot:
        if t.tobot == tobot.tobot:
            raise HTTPException(status_code=400, detail=f"У Тобота {t.tobot} уже есть Пилот {t.pilot}")

    new_tobot = CardTobotID(
        id=id_tobot,
        pilot=tobot.pilot,
        tobot=tobot.tobot,
        level=tobot.level
    )

    id_tobot += 1

    db_tobot.append(new_tobot)

    return f"Пилот {new_tobot.pilot} и его Тобот {new_tobot.tobot} теперь в команде Тоботов!"

@app.delete("/delete_card_tobot/{tobot_id}")
def delete_card_tobot(tobot_id: int):
    global db_tobot
    for t in db_tobot:
        if t.id == tobot_id:
            db_tobot.remove(t)
            return f"Пилот {t.pilot} и его Тобот {t.tobot} выгнаны из команды Тоботов"
    raise HTTPException(status_code=404, detail=f"Не существует Пилота и его Тобота с ID: {tobot_id}")

@app.put("/update_card_tobot/{tobot_id}")
def update_card_tobot(tobot_id: int, tobot: CardTobot):
    for t in db_tobot:
        if t.tobot == tobot.tobot and t.id != tobot_id:
            raise HTTPException(status_code=400, detail=f"У Тобота {t.tobot} уже есть Пилот {t.pilot}")

    for t in db_tobot:
        if t.id == tobot_id:
            t.pilot=tobot.pilot
            t.tobot=tobot.tobot
            t.level=tobot.level
            return f"Данные Пилота {t.pilot} и его Тобота {t.tobot} обновлены"
    raise HTTPException(status_code=404, detail=f"Не существует Пилота и его Тобота с ID: {tobot_id}"-