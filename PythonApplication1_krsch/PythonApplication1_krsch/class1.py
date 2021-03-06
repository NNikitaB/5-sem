from sqlalchemy import Column, Integer, String, create_engine,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,Date,CheckConstraint
import sqlalchemy as db

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('postgresql://postgres:1999@localhost/alhimic',echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

FlightPersonal = db.Table('flightpersonal',Base.metadata,
    db.Column('flight_id', db.Integer, db.ForeignKey('flight.id'),nullable=False),
    db.Column('personal_id', db.Integer, db.ForeignKey('personal.id'),nullable=False)
)
AirplanePersonal = db.Table('airplanepersonal',Base.metadata,
    db.Column('airplane_id', db.Integer, db.ForeignKey('airplane.id',ondelete="CASCADE"),nullable=False),
    db.Column('personal_id', db.Integer, db.ForeignKey('personal.id',ondelete="CASCADE"),nullable=False)
)

class Airpost(Base):
    __tablename__ = 'airpost'
    id = Column(Integer, primary_key=True)
    owner = Column(String,nullable=False)
    country = Column(String,nullable=False)
    city = Column(String,nullable=False)
    name=Column( String,nullable=False)

    def __init__(self, owner, country, city,name):
        self.owner = owner
        self.country = country
        self.city = city
        self.name = name
    def __repr__(self):
        return "<airpost('%s','%s', '%s', '%s')>" % (self.owner, self.country, self.city, self.name)

class Airplane(Base):
    __tablename__ = 'airplane'
    id = Column(Integer, primary_key=True)
    countplases = Column(Integer,nullable=False)
    Class = Column(Integer,nullable=False)
    firm = Column(String,nullable=False)
    yearreliase=Column( Integer,nullable=False)
    airpost_id=Column( Integer,ForeignKey('airpost.id'))
    airplanepersonal = relationship('Personal', secondary=AirplanePersonal)

    def __init__(self, countplases, Class, firm,yearreliase):
        self.countplases = countplases
        self.Class = Class
        self.firm = firm
        self.yearreliase = yearreliase
    def __repr__(self):
        return "<airplane('%i','%i', '%s', '%i')>" % (self.countplases, self.Class, self.firm, self.yearreliase)

class Personal(Base):
    __tablename__ = 'personal'
    id = Column(Integer, primary_key=True)
    calary = Column(Integer,nullable=False)
    name = Column(String,nullable=False)
    airpost_id=Column( Integer,ForeignKey('airpost.id',ondelete="CASCADE"),nullable=False)
    flightpersonal = relationship('Flight', secondary=FlightPersonal)

    def __init__(self, calary, name):
        self.calary = calary
        self.name = name

class Position(Base):
    __tablename__ = 'position'
    id = Column(Integer, primary_key=True)
    name = Column(String,nullable=False)
    personal_id=Column( Integer,ForeignKey('personal.id',ondelete="CASCADE"),nullable=False)

    def __init__(self, name):
        self.name = name

class Flight(Base):
    __tablename__ = 'flight'
    id = Column(Integer, primary_key=True)
    whereto = Column(String,nullable=False)
    wherefrom = Column(String,nullable=False)
    time = Column(Date,nullable=False)
    airplane_id=Column(Integer,ForeignKey('airplane.id',ondelete="CASCADE"),nullable=False)


    def __init__(self, whereto,wherefrom,time ):
        self.whereto = whereto
        self.wherefrom = wherefrom
        self.time = time


class Stocks(Base):
    __tablename__ = 'stocks'
    id = Column(Integer, primary_key=True)
    date = Column(Date,nullable=False)
    dataaction = Column(Date,nullable=False)

    def __init__(self, date,dataaction ):
        self.date = date
        self.dataaction = dataaction

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    date = Column(Date,nullable=False)
    fillname = Column(String,nullable=False)
    pasport = Column(Integer,nullable=False)
    happyb = Column(Date,nullable=False)
    exps = Column(Integer,nullable=False)

    def __init__(self, date,fillname,pasport,happyb,exps ):
        self.date = date
        self.fillname = fillname
        self.pasport = pasport
        self.happyb = happyb
        self.exps = exps


class Phone(Base):
    __tablename__ = 'phone'
    id = Column(Integer, primary_key=True)
    client_id =  Column(Integer,ForeignKey('client.id',ondelete="CASCADE"),nullable=False)
    date = Column(Date,nullable=False)
    number = Column(Integer,nullable=False)

    def __init__(self, date,number ):
        self.date = date
        self.number = number


class Ticket(Base):
    __tablename__ = 'ticket'
    id = Column(Integer, primary_key=True)
    cost = Column(Integer,nullable=False)
    dataaction = Column(Integer,nullable=False)
    datastatement = Column(Date,nullable=False)
    client_id =  Column( Integer,ForeignKey('client.id',ondelete="CASCADE"),nullable=False)
    flight_id =  Column( Integer,ForeignKey('flight.id',ondelete="CASCADE"),nullable=False)
    stocks_id =  Column( Integer,ForeignKey('stocks.id',ondelete="CASCADE"),nullable=False)

    def __init__(self, cost,dataaction,datastatement ):
        self.cost = cost
        self.dataaction = dataaction
        self.datastatement = datastatement

        

class Cargo(Base):
    __tablename__ = 'cargo'
    id = Column(Integer, primary_key=True)
    cost = Column(Integer,nullable=False)
    weight = Column(Integer,nullable=False)
    Class = Column(Integer,nullable=False)
    ticket_id =  Column( Integer,ForeignKey('ticket.id',ondelete="CASCADE"),nullable=False)

    def __init__(self, cost,weight,Class ):
        self.cost = cost
        self.weight = weight
        self.Class = Class


#Base.metadata.create_all(engine)