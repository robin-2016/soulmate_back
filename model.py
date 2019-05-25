#!/usr/bin/env python
# -*-coding:utf-8 -*-

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime,create_engine
from sqlalchemy.orm import sessionmaker

engine=create_engine('mysql+pymysql://root:31415926@localhost:3306/soulmate')
DBsession=sessionmaker(bind=engine)
db=DBsession()

Base = declarative_base()

class User(Base):
	__tablename__='user'
	id=Column(Integer,primary_key=True)
	openid=Column(String(256))
	name=Column(String(128))
	phone=Column(String(16))
	sex=Column(String(6))
	avater=Column(String(128))
	style=Column(String(6))
	pro=Column(String(6))
	dati=Column(String(6))
	message_flag=Column(String(6))
	create_time=Column(DateTime)

class Dati(Base):
	__tablename__='dati'
	id=Column(Integer,primary_key=True)
	openid=Column(String(256))
	result1=Column(String(32))
	result2=Column(String(32))
	result3=Column(String(32))

Base.metadata.create_all(engine)
