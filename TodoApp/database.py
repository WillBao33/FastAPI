from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db' # if use sqlite
# SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:test1234!@localhost/TodoApplicationDatabase' # if use Postgresql
# SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:test1234!@127.0.0.1:3306/TodoApplicationDatabase'  # if use mysql
# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}) for sqlite only
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base() # create a base, which is an object of the database
