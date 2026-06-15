from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel, Field
app = FastAPI()

class CardLBX(BaseModel):
    player: str
    lbx: str
    level: int = Field(ge=500000, le=1000000)
class CardLBXID(CardLBX):
    id: int

db_players = []

id_players = 1

@app.get("/")
def register_in_nics(request: Request):
    docs_url = f"{request.base_url}docs"
    return {"Заявка": "Чтобы подать заявку для вступления в команду NICS, заполните карточку про себя на сайте по ссылке", "Сайт для заполнения карточки": docs_url}

@app.get("/db_card_players")
def db_card_players():
    return {"Состав игроков NICS": db_players}

@app.get("/rearch_card_players/{player_id}")
def search_card_players(player_id: int):
    for p in db_players:
        if p.id == player_id:
            return {f"Карточка игрока NICS c ID: {player_id}": p}
    raise HTTPException(status_code=404, detail=f"В составе NICS нету игрока с ID: {player_id}")

@app.post("/create_card_player")
def create_card_players(player: CardLBX):
    for p in db_players:
        if p.lbx == player.lbx:
            raise HTTPException(status_code=400, detail=f"LBX {p.lbx} уже занят игроком {p.player}, выберите себе другого LBX, иначе вашу заявку не рассмотрят")
    global id_players
    new_player = CardLBXID(
        id=id_players,
        player=player.player,
        lbx=player.lbx,
        level=player.level
    )

    id_players += 1

    db_players.append(new_player)

    return f"Карточка игрока {new_player.player} создана. Вашу заявку рассмотрели, вы приняты, и теперь вы числитесь в составе игроков NICS"

@app.delete("/delete_card_player/{player_id}")
def delete_card_player(player_id: int):
    global db_players
    for p in db_players:
        if p.id == player_id:
            db_players.remove(p)
            return f"Игрок {p.player} исключён из NICS, его карточка удалена"
    raise HTTPException(status_code=404, detail=f"В составе NICS нету игрока с ID: {player_id}")

@app.put("/update_card_player/{player_id}")
def update_card_player(player_id: int, player: CardLBX):
    global db_players
    for p in db_players:
        if p.lbx == player.lbx and p.id != player_id:
            raise HTTPException(status_code=400, detail=f"LBX {p.lbx} уже занят игроком {p.player}, выберите себе другого LBX, иначе вы не сможете обновить данные карточки")

    for p in db_players:
        if p.id == player_id:
            p.player=player.player
            p.lbx=player.lbx
            p.level=player.level
            return f"Данные карточки игрока {p.player} обновлены"
    raise HTTPException(status_code=404, detail=f"В составе NICS нету игрока с ID: {player_id}")