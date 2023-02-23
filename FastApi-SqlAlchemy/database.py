from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings  import settings
# user = merndev
# pswrd = merndev123
SQLALCHEMY_DATABASE_URL = f'mongodb+srv://$merndev:$merndev123@cluster0.p6xod.mongodb.net/Student?retryWrites=true&w=majority'
print("settings.database_username", settings.database_username)
print("settings.database_password", settings.database_password)
print("settings.database_hostname", settings.database_hostname)
print("settings.database_port", settings.database_port)
print("settings.database_name", settings.database_name)

# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL,pool_size=10)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()