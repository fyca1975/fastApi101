import os
from sqlalchemy import create_engine
#ORM son lib de conexion para python
from sqlalchemy.orm.session import sessionmaker 
# manipular las tablas de la bae de datos
from sqlalchemy.ext.declarative import declarative_base

# nombre de la base de datos
sqlite_file_name = "database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

#conexion base de datos
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#motor de la base de datos
engine = create_engine(database_url, echo=True)


#sesion de la base de datos

Session = sessionmaker(bind=engine) 

Base = declarative_base()