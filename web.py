# -*- coding: utf-8 -*-

from flask import Flask,render_template
import dbsession
import db_data
from flask import current_app,request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

#启动数据库连接池
try:
    db_pool = dbsession.dbpool('apps','debs1apps','DERP').db_conn_pool()
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
    t = res01.exec_sql(db_pool.acquire(),sumtable_sql(),{'flag':'E'},3)
    db_pool.release()
    return t

@app.route('/domain')
def index():
    #return '<h1>hello </h1> <h2> %s </h2>',sumtable_tuple()[0][5]
    return render_template('index.html',table = sumtable_tuple())

@app.route('/context')
def context():
    return ''+current_app.name+' '+request.url

if __name__ == '__main__':
    app.run(debug=True)

