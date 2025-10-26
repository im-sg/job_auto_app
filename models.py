from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    profile_name = Column(String, index=True)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    fields = relationship("ProfileField", back_populates="profile", cascade="all, delete-orphan")

class ProfileField(Base):
    __tablename__ = "profile_fields"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    field_name = Column(String)
    field_value = Column(String)

    profile = relationship("Profile", back_populates="fields")