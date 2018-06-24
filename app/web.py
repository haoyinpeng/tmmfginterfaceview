# -*- coding: utf-8 -*-

from flask import Flask,render_template
import dbsession
import sql_set
from flask import current_app,request
from flask_sqlalchemy import SQLAlchemy,_EngineConnector
from sqlalchemy import create_engine
from CONFIG import config



db = SQLAlchemy()

app = Flask(__name__)
#使用flask扩展 ORM 模型来操作数据库 不过对于复杂sql语句不可行 因为必须要有对应模型
app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://apps:debs1apps@172.18.2.123:1541/DERP'
#app.config.from_object(config['development'])
#config['development'].init_app(app)

#db = SQLAlchemy(app)
db.init_app(app)


#启动数据库连接池
try:
    db_pool = dbsession.dbpool('B159212','github&flask-1','PERP').db_conn_pool()
except Exception as dberror:
    print('获取数据库连接池失败',dberror)

#app_ctx = app.app_context()

def sumtable_tuple(flag,rows):
    db_sum = db_pool.acquire()
    t = sql_set.ret_sql_res(db_sum,sql_set.sumtable_sql(),{'flag':flag},rows)
    db_pool.release(db_sum)
    return t

def get_sumtable_01():
    #eng = db.get_engine()
    print('before session ....')
    t = db.session.execute(sql_set.sumtable_sql(),{'flag':'E'})
    print('after session ....')
    re = t.fetchall()
    return re

@app.route('/')
def index():
    #return '<h1>hello </h1> <h2> %s </h2>',sumtable_tuple()[0][10]
    return render_template('index.html',table = sumtable_tuple('E',10))

@app.route('/005')
def index05():
    #return '<h1>hello </h1> <h2> %s </h2>',sumtable_tuple()[0][5]
    return render_template('index.html',table = sumtable_tuple('E',5))

@app.route('/indexs')
def indexs():
    #return '<h1>hello </h1> <h2> %s </h2>',get_sumtable_01
    print(get_sumtable_01())
    return render_template('sumtable.html',table = get_sumtable_01())

@app.route('/context')
def context():
    return ''+current_app.name+' '+request.url

if __name__ == '__main__':
    app.run(debug=True)

