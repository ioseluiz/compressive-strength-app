from sqlalchemy.orm import Session
from app import models, schemas


def get_mix(db: Session, mix_id: int):
    return db.query(models.mix.Mix).filter(models.mix.Mix.id == mix_id).first()

def get_mixes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.mix.Mix).offset(skip).limit(limit).all()

def create_mix(db: Session, mix: schemas.mix.MixCreate):
    db_mix = models.mix.Mix(**mix.dict())
    db.add(db_mix)
    db.commit()
    db.refresh(db_mix)
    return db_mix

# TODO QUERY for samples included in emails