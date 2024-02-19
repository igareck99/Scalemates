from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Enum
from sqlalchemy.ext.declarative import declarative_base
from database.Enums import *


db = SQLAlchemy()
Base = declarative_base()

class ReceivedModel:

    def __init__(self, productName, seriesInfo, finishType, paintType, color):
        self.productName = productName
        self.seriesInfo = seriesInfo
        self.finishType = finishType
        self.paintType = paintType
        self.color = color


class PaintType(Base):
    __tablename__ = 'paint_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    colors = db.relationship('Color', back_populates='paint_type')

class FinishType(Base):
    __tablename__ = 'finish_type'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    colors = db.relationship('Color', back_populates='finish_type')

class Producer(Base):
    __tablename__ = 'producer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    colors = db.relationship('Color', back_populates='producer_type')

class Color(Base):
    __tablename__ = 'color'
    id = db.Column(db.Integer, primary_key=True)
    productName = db.Column(db.String(50), nullable=False)
    seriesInfo = db.Column(db.String(100), nullable=False)
    producer_id =  db.Column(db.Integer, db.ForeignKey('producer.id'))
    finish_type_id = db.Column(db.Integer, db.ForeignKey('finish_type.id'))
    paint_type_id = db.Column(db.Integer, db.ForeignKey('paint_type.id'))
    color = db.Column(db.String(10), nullable=False)

    finish_type = db.relationship('FinishType', back_populates='colors')
    producer_type = db.relationship('Producer', back_populates='colors')
    paint_type = db.relationship('PaintType', back_populates='colors')