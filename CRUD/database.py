import sqlalchemy as sql
import sqlalchemy.ext.declarative as declarative
import sqlalchemy.orm as orm

SQLALCHEMY_DATABASE_URL= 'sqlite:///./database.db'

engine= sql.create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

sessionlocal= orm.sessionmaker(autocommit= False, autoflush= False, bind= engine)

base= declarative.declarative_base()