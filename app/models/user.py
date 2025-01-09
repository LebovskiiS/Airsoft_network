from . import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30),unique=True, nullable= False)
    email: Mapped[str] = mapped_column(String(30),unique=True, nullable= False)
    password: Mapped[str] = mapped_column(String(255), nullable= False)
    events = relationship('Event', secondary= 'users_events_association', back_populates= 'users')







