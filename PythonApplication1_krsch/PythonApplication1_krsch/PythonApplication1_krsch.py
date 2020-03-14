import asyncio
import websockets
import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web
import os.path
import tornado.websocket

import uuid
import sqlite3
import sqlalchemy as db
import prettytable
import tornado
import socket
from class1 import Phone,Airpost,Airplane,Personal,Position,Flight,Stocks,Client,Ticket,Cargo
from class1 import Base,engine
from sqlalchemy import update,delete


from tornado.options import define, options, parse_command_line

from sqlalchemy import Column, Integer, String, create_engine,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey,Date,CheckConstraint
import sqlalchemy as db

from PyQt5 import QtWidgets
from un import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys

from tornado.web import Application

class PSQL:
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    def __del__(self):
        session.close()

class User(PSQL):

    def Show(self):
        t=[]
        s='<body><table><tr><th>id</th><th>date</th><th>fillname</th><th>pasport</th><th>happyb</th><th>exps</th></tr>'
        for i in self.session.query(Client).order_by(Client.id):
            s+= ('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>').format(i.id,i.date,i.fillname,i.pasport,i.happyb,i.exps)
        s+='</table></body>'
        t.append(s)     
        return t

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
    
    def Show(self):
        t=[]
        s='<body><table><tr><th>id</th><th>date</th><th>fillname</th><th>pasport</th><th>happyb</th><th>exps</th></tr>'
        for i in self.session.query(Client).order_by(Client.id):
            s+= ('<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>').format(i.id,i.date,i.fillname,i.pasport,i.happyb,i.exps)
        s+='</table></body>'
        t.append(s)     
        return t
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


from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")



class BaseHandler(tornado.websocket.WebSocketHandler):#tornado.web.RequestHandler):
    def get_current_user(self):
        
        return self.get_secure_cookie("user")


class MainHandler(BaseHandler):
    def get(self):
        if not self.current_user:
            self.redirect("/login")
            return
        name = tornado.escape.xhtml_escape(self.current_user)

        self.write("Hello, " + name)

class LoginHandler(BaseHandler):
    def get(self):
        self.write('<html><body><form action="/login" method="post">'
                   'Name: <input type="text" name="name">'
                   '<input type="submit" value="Sign in">'
                   '</form></body></html>')

    def post(self):
        self.set_secure_cookie("user", self.get_argument("name"))
        self.redirect("/")




clients = []
us=User()
ad=Admin()
def send_to_all_clients():
        #for client in clients:
    z=us.Show()
    return z
class MainHandler1( tornado.websocket.WebSocketHandler):

    def open( self): 
        print( "WebSocket opened")
        clients.append(self)        

    def on_message( self,  message='11111111'): 
#        self.write_message('<html><body><h2>{}:</h2></body></html>'.format(self.get_body_argument('message')) ) 

        fj='<title>Тег table</title><style> table { width: 100%; background: white;color: white;border-spacing: 1px;} td, th {  background: maroon;padding: 5px; }</style>'
        hf=send_to_all_clients()
        for client in clients:
            client.write_message('<html><body><h2>{}</h2>{}</body>{}</html>'.format(message,fj,hf))
        
    def on_close(self): 
        clients.remove(self)
        print("WebSocket closed")

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        #self.get_body_argument('name')

  #  def post(self):
 #       self.set_header("Content-Type", "text/plain")
#        self.write("You wrote " + self.get_body_argument('name'))

def main():
#    us=User()
#    us.AddClient('14.02.1999','nnm',1514545,'14.02.1999',422)
#    us.Show()
    #return
    application = tornado.web.Application([
    #(r"/login", LoginHandler),
    (r'/', IndexHandler),
    (r'/ws/', MainHandler1)
], cookie_secret="61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=")
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
    #app=Application()

if __name__ == "__main__":
    main()
