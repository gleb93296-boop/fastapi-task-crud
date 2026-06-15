from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import engine, get_db
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def link():
    return RedirectResponse(url="/docs")

@app.get("/player")
def db_card_players(db: Session = Depends(get_db)):
    query = select(models.PlayerDB)
    result = db.execute(query)
    player = result.scalars().all()
    return {"status": "success", "message": "Карточки игроков NICS", "cards": player}

@app.get("/player/{player_id}")
def search_card_player(player_id: int, db: Session = Depends(get_db)):
    query = select(models.PlayerDB).where(models.PlayerDB.id == player_id)
    result = db.execute(query)
    player = result.scalar_one_or_none()

    if player is None:
        raise HTTPException(status_code=404, detail="Игрок не найден")
    return {"status": "success", "message": f"Карточка игрока с ID: {player_id}", "card": player}

@app.post("/player")
def create_card_player(player: str, lbx: str, level: int, db: Session = Depends(get_db)):
    new_player = models.PlayerDB(player=player, lbx=lbx, level=level)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return {"status": "success", "message": f"Карточка игрока {player}", "card": new_player}

@app.delete("/player/{player_id}")
def delete_card_player(player_id: int, db: Session = Depends(get_db)):
    query = select(models.PlayerDB).where(models.PlayerDB.id == player_id)
    result = db.execute(query)
    player = result.scalar_one_or_none()

    if player is None:
        raise HTTPException(status_code=404, detail="Игрок не найден")

    db.delete(player)
    db.commit()
    return {"status": "success", "message": f"Игрок с ID: {player_id} удалён", "card": player}

@app.put("/player/{player_id}")
def update_card_player(player_id: int, player: str, lbx: str, level: int, db: Session = Depends(get_db)):
    query = select(models.PlayerDB).where(models.PlayerDB.id == player_id)
    result = db.execute(query)
    players = result.scalar_one_or_none()

    if players is None:
        raise HTTPException(status_code=404, detail="Игрок не найден")

    players.player = player
    players.lbx = lbx
    players.level = level
    db.commit()
    db.refresh(player)
    return {"status": "success", "message": f"Данные карточки игрока с ID: {player_id} обновлены", "card": players}