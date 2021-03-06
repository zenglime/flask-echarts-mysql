from flask import Flask,render_template,url_for, jsonify
import pymysql

import json

#生成Flask实例
app = Flask(__name__)

@app.route('/')
def my_echart():

    return render_template('sample3.html')

# //data路由接收前端的ajax请求
@app.route('/data',methods=['GET'])
def my_echart_data():
    # 连接数据库，从数据库中获取数据
    conn = pymysql.connect(host='127.0.0.1',user='root',password='123456',db='flask')
    cursor = conn.cursor()
    cursor.execute('select * from test')
    values = cursor.fetchall()
    # 创建一个空数组，将sql返回的数据进行逐个存到这个数组里面
    jsondata = {}
    xd = []
    yd = []
    for i in values:
        xd.append(i[0])
        yd.append(i[1])

    jsondata['categories'] = xd
    jsondata['data'] = yd
    # 将结果转化为json格式
    j = jsonify(jsondata)
    cursor.close()
    conn.close()
    return j


if __name__ == "__main__":
    # 运行项目
   app.run(debug = True,port=5000)