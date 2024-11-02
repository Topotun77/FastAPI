from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

print('='*70)
engine = create_engine('sqlite:///taskmanager.db', echo=True, pool_pre_ping=True)
# engine = create_engine('L:/Python/UU-kurs/Module17/taskmanager.db', echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(engine)

# connect = engine.connect()
# cursor = connect.execute("SELECT * FROM users")
# print(cursor.fetchall())
# # connect.execute(text("SELECT * FROM users"))
# connect.close()

class Base(DeclarativeBase):
    pass
