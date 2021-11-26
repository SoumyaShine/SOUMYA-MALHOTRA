from sqlalchemy import create_engine,Column,Integer,String,Float, engine 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import VARCHAR, DateTime


Base = declarative_base()

class Medicine(Base):

    __tablename__ = "medicines"
    id = Column(Integer,primary_key=True)   
    med_name = Column(String)
    sale = Column(Float)
    unit = Column(Float)
    quantity = Column(Integer)
    min_quantity = Column(Integer)
    comp_name = Column(String)
    #sup_id = Column(Integer)
    cost = Column(Float)
    purchased_medicines=Column(Integer)
    


class Customer(Base):

    __tablename__="customers"
    id = Column(Integer,primary_key=True)
    cust_name = Column(String)
    contact_number = Column(Integer)
    emailAddress = Column(VARCHAR)
    med_purchased = Column(Integer)
    total_cost = Column(Float)
    #custid = Column(Integer, ForeignKey('medicine.id'))


class Bill(Base):
    __tablename__ = "bill_details"
    bill_id = Column(Integer,primary_key=True)
    bill_date = Column(DateTime)
    paymentType = Column(String)
    totalAmount = Column(Float)
    discount = Column(Float)
    newPrice = Column(Float)
    remainingAmount = Column(Float)
    paidAmount = Column(Float)
    

    Medicine=Column(Integer,ForeignKey('medicines.id'))
    Customer=Column(Integer,ForeignKey('customers.id'))

    

    


if __name__ =="__main__":
    engine = create_engine('sqlite:///db.sqlite3')
    Base.metadata.create_all(engine)


