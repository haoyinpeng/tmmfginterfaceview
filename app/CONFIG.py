# -*- coding:utf-8 -*-

import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.AL32UTF8'

# DERP
DB_IP = '172.18.2.123'
DB_PORT = '1541'
DB_INSTANCE_NAME = 'derp'

#TERP
T_DB_IP = '172.18.2.152'
T_DB_PORT = '1531'
T_DB_INSTANCE_NAME = 'terp'

#PERP
P_DB_IP = '172.18.2.52'
P_DB_PORT = '1521'
P_DB_INSTANCE_NAME = 'perp'

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string' 
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True 
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]' 
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>' 
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') 

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'oracle://apps:debs1apps@172.18.2.123:1541/DERP?'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_NATIVE_UNICODE = False

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'oracle://B159212:github&flask-1@172.18.2.52:1521/TERP?charset=utf-8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_NATIVE_UNICODE = False

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'oracle://B159212:github&flask-1@172.18.2.52:1521/PERP?charset=utf-8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #SQLALCHEMY_NATIVE_UNICODE = False

config = {'development': DevelopmentConfig,
          'testing': TestingConfig,
          'production': ProductionConfig,

          'default': ProductionConfig
          }







