from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.config import Configuration
import os
from database.Models import *

def getProducerId(companyName: str):
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        producers = session.query(Producer).all()
        print(producers)
        result = []
        # for x in producers:
        #     if str(x.name).lower() == companyName.lower():
        #         print('sasasasasasas')
            # if companyName.lower() in x.name.lower():
            #     print(f"ssadasdksd  {x}")

def getAllProducers():
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        colors = session.query(Producer).all()
        return colors

def getAllColor():
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        colors = session.query(Color).all()
        return colors

def createColor(model: ReceivedModel):
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        print(f"asklasklask  {type(model)}")
        paintType = session.query(PaintType).filter_by(name=model.paintType).first()
        finishType = session.query(FinishType).filter_by(name=model.finishType).first()
        producer = session.query(Producer).filter_by(name=model.producer).first()
        print(f"sklakaskas  {producer}")
        new_color = Color(
            productName=model.productName,
            seriesInfo=model.seriesInfo,
            producer_id = producer.id,
            finish_type_id=finishType.id,
            paint_type_id=paintType.id,
            color=model.color
        )
        session.add(new_color)

        session.commit()


def database_exists():
    # Проверяем существование файла базы данных SQLite
    print(Configuration.SQLALCHEMY_DATABASE_URI)
    if os.path.exists(Configuration.SQLALCHEMY_DATABASE_URI):
        return False
    else:
        return True

def createDatabase():
    if database_exists():
        db_path = Configuration.SQLALCHEMY_DATABASE_URI.replace("sqlite:///", "")
        if os.path.exists(db_path):
            os.remove(db_path)
            print('DB REMOVED')
    engine = create_engine(Configuration.SQLALCHEMY_DATABASE_URI, echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(PaintType(name = PaintEnum.VALUE1.value))
    session.add(PaintType(name = PaintEnum.VALUE2.value))
    session.add(FinishType(name = FinishTypeEnum.VALUE1.value))
    session.add(FinishType(name = FinishTypeEnum.VALUE2.value))
    session.add(Producer(name=ProducerEnum.VALUE1.value))
    session.add(Producer(name=ProducerEnum.VALUE2.value))
    session.add(Producer(name=ProducerEnum.VALUE3.value))
    session.commit()

# createDatabase()
