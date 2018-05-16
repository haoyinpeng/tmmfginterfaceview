# -*- coding: utf-8 -*-

import cx_Oracle
import CONFIG

class dbconnsingle():

    def __init__(self,user_name,passwd,env):
        self.user_name = user_name
        self.passwd = passwd
        self.env = env
        print(self.user_name,self.passwd)

    # tns info
    def db_tns(self,env):
        if env=='PERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'DERP':
            print('DERP..',CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'TERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        
    # db connection
    def db_conn(self):
        return cx_Oracle.connect(self.user_name,self.passwd,self.db_tns(self.env),encoding = 'UTF-8') 


class dbpool(cx_Oracle.SessionPool):
    def __init__(self,user_name,passwd,env):
        self.user_name = user_name
        self.passwd = passwd
        self.env = env
    
    # tns info
    def db_tns(self,env):
        if env=='PERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'DERP':
            print('DERP..',CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
        elif env == 'TERP':
            return cx_Oracle.makedsn(CONFIG.DB_IP,CONFIG.DB_PORT,CONFIG.DB_INSTANCE_NAME)
    
    def db_conn_pool(self):
        return cx_Oracle.SessionPool(user=self.user_name,password=self.passwd,dsn=self.db_tns(self.env),min=1,max=500,increment=1)



    
