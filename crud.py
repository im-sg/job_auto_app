from sqlalchemy.orm import Session
import models, schemas

def create_profile(db: Session, profile: schemas.ProfileCreate):
    db_profile = models.Profile(profile_name=profile.profile_name, description=profile.description)
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile

def get_profiles(db: Session):
    return db.query(models.Profile).all()

def get_profile(db: Session, profile_id: int):
    return db.query(models.Profile).filter(models.Profile.id == profile_id).first()

def add_field_to_profile(db: Session, profile_id: int, field: schemas.ProfileFieldCreate):
    db_field = models.ProfileField(profile_id=profile_id, field_name=field.field_name, field_value=field.field_value)
    db.add(db_field)
    db.commit()
    db.refresh(db_field)
    return db_field

def get_fields_for_profile(db: Session, profile_id: int):
    return db.query(models.ProfileField).filter(models.ProfileField.profile_id == profile_id).all()