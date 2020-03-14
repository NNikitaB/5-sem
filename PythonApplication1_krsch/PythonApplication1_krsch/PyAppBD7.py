import sqlite3
import sqlalchemy as db
import prettytable
import tornado
import socket
from class1 import Phone,Airpost,Airplane,Personal,Position,Flight,Stocks,Client,Ticket,Cargo
from class1 import Base,engine
from sqlalchemy import update,delete

from sqlalchemy import Column, Integer, String, create_engine,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,Date,CheckConstraint
import sqlalchemy as db

from PyQt5 import QtWidgets
from un import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys



class PSQL:
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    def __del__(self):
        session.close()
#aist=Airpost("YOU","HE","SHE","I")
#session.add(aist)

#for instance in session.query(Airpost).order_by(Airpost.id): 
#    print(instance.owner, instance.country,instance.city,instance.name,instance.id)
#session.commit()
#session.close()

class User(PSQL):

    def AddClient(self,date,fillname,pasport,happyb,exps):
        item_client=Client(date,fillname,pasport,happyb,exps)
        self.session.add(item_client)
        self.session.commit()
    def AddTicket(self,cost,dataaction,dataststement):
        item_ticket=Ticket(cost,dataaction,dataststement)
        self.session.add(item_ticket)
        self.session.commit()
    def AddCargo(self,cost,weiggt,Class):
        item_cargo=Cargo(cost,weiggt,Class)
        self.session.add(item_cargo)
        self.session.commit()
    def AddPhone(self,data,number):
        item_phone=Phone(data,number)
        self.session.add(item_phone)
        self.session.commit()   
    def UpdateClient(self,id,**kvargs):
        self.session.query(Client).filter(Client.id==id).update(kvargs)
        self.session.commit()
    def UpdateTicket(self,**kvargs):
        self.session.query(Ticket).filter(Ticket.id==id).update(kvargs)
        self.session.commit()
    def UpdateCargo(self,**kvargs):
        self.session.query(Cargo).filter(Cargo.id==id).update(kvargs)
        self.session.commit()
    def UpdatePhone(self,**kvargs):
        self.session.query(Phone).filter(Phone.id==id).update(kvargs)
        self.session.commit()
    def DeleteClient(self,id):
        self.session.query(Client).filter(Client.id==id).delete()
        self.session.commit()
    def DeleteTicket(self,id):
        self.session.query(Ticket).filter(Ticket.id==id).delete()
        self.session.commit()
    def DeleteCargo(self,id):
        self.session.query(Cargo).filter(Cargo.id==id).delete()
        self.session.commit()
    def DeletePhone(self,id):
        self.session.query(Phone).filter(Phone.id==id).delete()
        self.session.commit()

class Manager(PSQL):

    def AddStocks(self, date,dataaction ):
        stocks_client=Stocks(date,dataaction)
        self.session.add(stocks_client)
        self.session.commit()
    def AddFlight(self,whereto,wherefrom,time):
        flight_ticket=Flight(whereto,wherefrom,time)
        self.session.add(flight_ticket)
        self.session.commit()
    def AddPersonal(self,calary, name):
        personal_cargo=Personal(calary, name)
        self.session.add(personal_cargo)
        self.session.commit()
    def AddPosition(self,name):
        item_position=Position(name)
        self.session.add(item_position)
        self.session.commit()   
    def AddAirplaneAersonal(self):
        airplaneaersonal_cargo=AirplaneAersonal()
        self.session.add(airplaneaersonal_cargo)
        self.session.commit()
    def AddFlightPersonal(self):
        item_flightpersonal=FlightPersonal()
        self.session.add(item_flightpersonal)
        self.session.commit()   
    def UpdateStocks(self,id,**kvargs):
        self.session.query(Stocks).filter(Stocks.id==id).update(kvargs)
        self.session.commit()
    def UpdateFlight(self,**kvargs):
        self.session.query(Flight).filter(Flight.id==id).update(kvargs)
        self.session.commit()
    def UpdatePersonal(self,**kvargs):
        self.session.query(Personal).filter(Personal.id==id).update(kvargs)
        self.session.commit()
    def UpdatePosition(self,**kvargs):
        self.session.query(Position).filter(Position.id==id).update(kvargs)
        self.session.commit()
    def UpdateAirplaneAersonal(self,**kvargs):
        self.session.query(AirplaneAersonal).filter(AirplaneAersonal.id==id).update(kvargs)
        self.session.commit()
    def UpdateFlightPersonal(self,**kvargs):
        self.session.query(FlightPersonal).filter(FlightPersonal.id==id).update(kvargs)
        self.session.commit()
    def DeleteStocks(self,id):
        self.session.query(Stocks).filter(Stocks.id==id).delete()
        self.session.commit()
    def DeleteFlight(self,id):
        self.session.query(Flight).filter(Flight.id==id).delete()
        self.session.commit()
    def DeletePosition(self,id):
        self.session.query(Position).filter(Position.id==id).delete()
        self.session.commit()
    def DeletePersonal(self,id):
        self.session.query(Personal).filter(Personal.id==id).delete()
        self.session.commit()
###########???????????????????????????????????????/
    def DeleteAirplaneAersonal(self,id):
        self.session.query(AirplaneAersonal).filter(AirplaneAersonal.id==id).delete()
        self.session.commit()
    def DeleteFlightPersonal(self,id):
        self.session.query(FlightPersonal).filter(FlightPersonal.id==id).delete()
        self.session.commit()

class Admin(Manager,User):
    
    def AddAirpost(self,  owner, country, city,name ):
        airpost_client=Airpost( owner, country, city,name)
        self.session.add(airpost_client)
        self.session.commit()
    def AddAirplane(self, countplases, Class, firm,yearreliase):
        airplane_ticket=Airplane(countplases, Class, firm,yearreliase)
        self.session.add(airplane_ticket)
        self.session.commit()
    def UpdateAirpost(self,**kvargs):
        self.session.query(Airpost).filter(Airpost.id==id).update(kvargs)
        self.session.commit()
    def UpdateAirplane(self,**kvargs):
        self.session.query(Airplane).filter(Airplane.id==id).update(kvargs)
        self.session.commit()
    def DeleteAirpost(self,id):
        self.session.query(Airpost).filter(Airpost.id==id).delete()
        self.session.commit()
    def DeleteAirplane(self,id):
        self.session.query(Airplane).filter(Airplane.id==id).delete()
        self.session.commit()

########################################################################
class mywindow(QtWidgets.QMainWindow,PSQL):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # подключение клик-сигнал к слоту
        self.ui.pushButton_5.clicked.connect(self.btnClicked)
        self.ui.pushButton.clicked.connect(self.btnClicked1)
        self.ui.pushButton_2.clicked.connect(self.btnClicked2)
        self.ui.pushButton_3.clicked.connect(self.btnClicked3)
        self.ui.pushButton_4.clicked.connect(self.btnClicked4)
       
    def btnClicked1(self):  
        r=self.ui.textEdit.toPlainText()
        s=r.split(",",6)
        if len(s) >= 5:
            a=Airpost
            self.session.add(a)
            self.session.commit()
            self.ui.textEdit.setText('success')
        else:
            self.ui.textEdit.setText('error'+r)

    def btnClicked2(self):
        #airpost delete
        s=self.ui.textEdit.toPlainText()
        if s.isnumeric():
            self.Deletepost(int(s))
            self.ui.textEdit.setText('delete success')
        else:
            self.ui.textEdit.setText('delete err')
        
    def btnClicked3(self): 
        #airpost update
        r=self.ui.textEdit.toPlainText()
        s=r.split(",",6)
        if len(s) >= 5:
            self.Updatepost(int(s[0]),owner= s[1],country=s[2],city=s[3],name=s[4])
            self.ui.textEdit.setText('update success')
        else:
            self.ui.textEdit.setText('update err')

    def btnClicked4(self):
        #airpost viev
        self.ui.textEdit.clear()
        q = self.session.query(Airpost).all()
        d=''
        for x in q:
        #self.ui.textEdit.setText(self,)
            d += str(x.id)+'|' +x.owner +'|' + x.country +'|'+ x.city +'|'+ x.name +'\n'
        self.ui.textEdit.setText(d)
        
    def btnClicked(self):
        if self.ui.lineEdit =="" or (not str(self.ui.lineEdit).isnumeric()):
            self.ui.textEdit.clear()
            q = self.session.query(Client).all()
            d=''
            for x in q:
            #self.ui.textEdit.setText(self,)
                d += str(x.id)+'|'  +str(x.date)+'|' +str(x.fillname) +'|'+str(x.pasport) +'|'+str( x.happyb) +'|'+str(x.exps)+'\n'
            self.ui.textEdit.setText(d)
        else:
            self.ui.textEdit.clear()
            q = self.session.query(Client).filter(Client.id == int(self.ui.lineEdit.isdigit))
            d=''
            for x in q:
                d += str(x.id)+'|'  +str(x.date)+'|' +str(x.fillname) +'|'+str(x.pasport) +'|'+str( x.happyb) +'|'+str(x.exps)+'\n'
            self.ui.textEdit.setText(d)

    def Updatepost(self,id,**kvargs):
        self.session.query(Airpost).filter(Airpost.id==id).update(kvargs)
        self.session.commit()

    def Deletepost(self,id):
        self.session.query(Airpost).filter(Airpost.id==id).delete()
        self.session.commit()

#for instance in session.query(Airpost).order_by(Airpost.id): 
#    print(instance.owner, instance.country,instance.city,instance.name,instance.id)

app = QtWidgets.QApplication([])
application = mywindow()
application.show()
 
sys.exit(app.exec())
##########################################################################