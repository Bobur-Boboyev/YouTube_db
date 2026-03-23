from db.models.base import Base
from db.session import engine


def create_tables():
    Base.metadata.create_all(bind=engine)

print(Base.metadata.tables.keys())

if __name__ == "__main__":
    create_tables()