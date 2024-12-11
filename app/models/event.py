from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Event(Base):
    __tablename__ = 'events'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(String())
    users = relationship('User', back_populates='events', secondary= 'UserEventAssociation')


class UserEventAssociation(Base):
    __tablename__ = 'users_events_association'
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'), primary_key= True)
    event_id: Mapped[int] = mapped_column(Integer, ForeignKey('events.id'), primary_key= True)






