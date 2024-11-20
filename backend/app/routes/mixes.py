from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.auth.auth import get_db, get_current_user
from app.mixes import mixes


router = APIRouter()

@router.post("/mixes/", response_model=schemas.mix.Mix)
def create_mix(mix: schemas.mix.MixCreate, db: Session = Depends(get_db), current_user: schemas.user.User = Depends(get_current_user)):
    return mixes.create_mix(db=db, mix=mix)

@router.get("/mixes/{mix_id}", response_model= schemas.mix.Mix)
def read_mix(mix_id: int, db: Session = Depends(get_db), current_user: schemas.user.User = Depends(get_current_user)):
    db_mix = mixes.get_mix(db, mix_id=mix_id)
    if db_mix is None:
        raise HTTPException(status_code=404, detail="Mix not found")
    return db_mix

@router.get("/mixes/", response_model=list[schemas.mix.Mix])
def read_mixes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: schemas.user.User = Depends(get_current_user)):
    all_mixes = mixes.get_mixes(db, skip=skip, limit=limit)
    return all_mixes