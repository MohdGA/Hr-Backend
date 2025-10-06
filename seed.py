from sqlalchemy.orm import sessionmaker, Session
from data.hr_data import hr_list, leave_list, performance_list
from data.user_data import user_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base
from models.hr import hrModel


engine = create_engine(db_URI)
SessionsLocal = sessionmaker(bind=engine)


try:
    print('Reacreating database...')

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = SessionsLocal()
    
    db.add_all(user_list)
    db.commit()

    db.add_all(hr_list)
    db.commit()
    
    db.add_all(leave_list)
    db.commit()
    
    db.add_all(performance_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as error:
    print('An error occurred', error)

