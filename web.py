# -*- coding: utf-8 -*-

from flask import Flask
import dbsession
import db_data
from flask import current_app,request


app = Flask(__name__)

#启动数据库连接池
try:
    db_conn = dbsession.dbconnsingle('apps','debs1apps','DERP').db_conn()
except Exception as dberror:
    print('获取数据库连接失败',dberror)


#app_ctx = app.app_context()

def sumtable_sql():
    str_sql = ''' select * 
                      from apps.meserpprodsum m 
                     where process_flag = :flag '''
    return str_sql

def sumtable_tuple():
    res01 = db_data.get_result('666')
    return res01.exec_sql(db_conn,sumtable_sql(),{'flag':'E'},3) 

@app.route('/domain')
def index():
    return '<h1>hello </h1> <h2> %s </h2>',sumtable_tuple()[0][5]

@app.route('/context')
def context():
    return ''+current_app.name+' '+request.url

if __name__ == '__main__':
    app.run(debug=True)

