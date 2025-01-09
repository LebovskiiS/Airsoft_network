from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Event(Base):
    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String())
    users = relationship('User', secondary= 'users_events_association', back_populates= 'events')


class UserEventAssociation(Base):
    __tablename__ = 'users_events_association'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey('events.id'))






