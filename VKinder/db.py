import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

# Создаём БД
Base = declarative_base()

# Таблица с информацией о пользователе
class User(Base):
    __tablename__ = 'user'
    user_id = sq.Column(sq.Integer, primary_key=True)
    id = sq.Column(sq.Integer, unique=True)

# Таблица с историей поиска пользователя
class User_search_data(Base):
    __tablename__ = 'user_search_data'
    id = sq.Column(sq.Integer, primary_key=True)
    vk_id = sq.Column(sq.Integer, unique=True)

# Таблица с избранным пользователя
class White_list(Base):
    __tablename__ = 'white_list'
    user_id = sq.Column(sq.Integer, primary_key=True)
    id = sq.Column(sq.Integer, unique=True)
    first_name = sq.Column(sq.String, nullable=False)
    last_name = sq.Column(sq.String, nullable=False)
    vk_link = sq.Column(sq.String, unique=True, nullable=False)

# Создание таблиц
def create_tables(engine):
    Base.metadata.create_all(engine)

# Удаление таблиц
def drop_tables(engine):
    Base.metadata.drop_all(engine)