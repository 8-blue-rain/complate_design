from flask import Flask,request,render_template,redirect,jsonify,session
import pymongo
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import requests
import psycopg2
import parsel
import json
import re
from PIL import Image
import io
import copy
import os, sys,time


app  = Flask(__name__)
conn = psycopg2.connect(dbname="biye_db",
    user="postgres",
    password="889012ex",
    host="127.0.0.1",
    port="5432")
cur = conn.cursor()

@app.route('/fish_input_list_view')
def fish_input_list_view():
    return render_template('进货list.html')


@app.route('/fish_input_form_view',methods=['POST','GET'])
def fish_input_form_view():

    return render_template('进货form.html')

@app.route('/fish_input_create',methods=['POST','GET'])
def fish_input_create():
    return render_template('进货_create.html')

@app.route('/fish_product_product_list',methods=['POST','GET'])
def fish_product_product_list():
    if request.method == 'GET':
       cur.execute("select * from product")
       row = cur.fetchall()
       print(row)
       return render_template('产品_list.html',row=row)

@app.route('/fish_product_product_form',methods=['POST','GET'])
def fish_product_product_form():
    if request.method == 'GET':
       pro_form_id = request.args.get('pro_form_id')
       cur.execute("select * from product where id=(%s);",(pro_form_id,))
       row = cur.fetchall()
       cur.execute("select * from uom;")
       row_1 = cur.fetchall()
       cur.execute("select * from work_location")
       row_2 = cur.fetchall()
       prodcut_form_img = 'static/product_imgae_store/' + row[0][1] + '.png'
       return render_template('产品_form.html',row=row,row_1=row_1,row_2=row_2,prodcut_form_img=prodcut_form_img)

    if request.method == 'POST':
        new_product_img = request.files['file']
        used_img_name = request.form.get('used_img_name')
        product_name = request.form.get('product_name')
        product_uom = request.form.get('product_uom')
        product_stock_location = request.form.get('product_stock_location')
        product_type = request.form.get('product_type')
        product_id = request.form.get('product_id')

        cur.execute("update product set product_name=(%s),stock_location=(%s),product_uom=(%s),product_type=(%s) where id=(%s);",
                    (product_name,product_stock_location,product_uom,product_type,product_id,) )

        conn.commit()

        if new_product_img:
            new_product_img.filename = product_name + '.png'


        return redirect('fish_product_product_list')
        #难点：当图片不更换，而产品名要更换时，图片的名称也要和新产品名称一样

@app.route('/fish_product_create',methods=['POST','GET'])
def fish_product_create():
    if request.method == 'GET':
       cur.execute("select uom.uom_name from uom;")
       row = cur.fetchall()
       cur.execute("select work_location_name from work_location;")
       row_1 = cur.fetchall()
       print(row)
       print(row_1)
       return render_template('产品_create.html',row=row,row_1=row_1)

    if request.method == 'POST':
        product_img = request.files['file']

        product_create_name = request.form.get('product_create_name')
        product_stock_qty = request.form.get('product_stock_qty')
        product_stock_location = request.form.get('product_stock_location')
        product_stock_uom = request.form.get('product_stock_uom')
        product_type = request.form.get('product_type')

        cur.execute("insert into product(product_name,product_qty,stock_location,product_uom,product_type) values((%s),(%s),(%s),(%s),(%s));",
                    (product_create_name,product_stock_qty,product_stock_location,product_stock_uom,product_type,))
        conn.commit()

        product_img.filename = product_create_name + '.png'

        img_path = 'static/product_imgae_store/' + product_img.filename
        product_img.save(img_path)

        return redirect('fish_product_product_list')




@app.route('/fish_partner_list')
def partner_list():
    username = '苍铭'
    imag = username + str('.png')
    return render_template('联系人_list.html',imag=imag)

@app.route('/fish_product_product_delete',methods=['POST','GET'])
def fish_product_product_delete():
    pass

@app.route('/fish_partner_form',methods=['POST','GET'])
def partner_form():
        return render_template('联系人_form.html')

@app.route('/fish_partner_create',methods=['POST','GET'])
def fish_partner_create():
    return render_template('联系人_create.html')


@app.route('/fish_uom_list',methods=['POST','GET'])
def fish_uom_list():
    if request.method == 'GET':
        cur.execute("select * from uom;")
        row = cur.fetchall()
        u_li =[]
        for i in row:
            u_li += [i]

        return render_template('计量单位_list.html',u_li=u_li)

@app.route('/fish_uom_form',methods=['POST','GET'])
def fish_uom_form():
    if request.method == 'GET':
            uom_form = request.args.get('uom_form')
            cur.execute("select uom.uom_name from uom where id = (%s)", uom_form)
            row = cur.fetchall()
            cur.execute("select uom.id from uom where id = (%s)", uom_form)
            row_1 = cur.fetchall()
            print(row)
            print(row_1)
            return render_template('计量单位_form.html',row_1=row_1[0][0],row=row[0][0])

    if request.method == 'POST':
       u_form_name = request.form.get('u_form_name')
       id_uom_f = int(request.form.get('id_uom_f'))
       cur.execute("update uom set uom_name = (%s) where id=(%s)",(u_form_name,id_uom_f,))
       conn.commit()
       return redirect('fish_uom_list')


@app.route('/fish_uom_create',methods=['POST','GET'])
def fish_uom_create():
    if request.method == 'GET':
        return render_template('计量单位_create.html')

    if request.method == 'POST':
        input_number = request.form.get('input_number')
        cur.execute("""insert into uom(uom_name) values(%s);""", (input_number,))
        conn.commit()
        return redirect('fish_uom_list')

@app.route('/fish_uom_delete',methods=['POST','GET'])
def fish_uom_delete():
    uom_del = request.args.get("uom_del")
    cur.execute("delete from uom where id = (%s) ",(uom_del,))
    conn.commit()
    return redirect('fish_uom_list')



@app.route('/fish_warehouse_form')
def fish_warehouse_form():
    return render_template('仓库_form.html')

@app.route('/fish_warehouse_list')
def fish_warehouse_list():
    return render_template('仓库_list.html')

@app.route('/fish_warehouse_create')
def fish_warehouse_create():
    return render_template('仓库_create.html')


@app.route('/fish_output_create')
def fish_output_create():
    return render_template('出货_create.html')


@app.route('/fish_output_form')
def fish_output_form():
    return render_template('出货_form.html')


@app.route('/fish_output_list')
def fish_output_list():
    return render_template('出货_list.html')


@app.route('/work_location_list',methods=['POST','GET'])
def work_location_list():
    if request.method == 'GET':
       cur.execute('select * from work_location;')
       wl_row = cur.fetchall()
       return render_template('作业地址_list.html',wl_row_li=wl_row)

@app.route('/work_location_form',methods=['POST','GET'])
def work_location_form():
    if request.method == 'GET':
       al_id = request.args.get('al_id')
       cur.execute("select * from work_location where id=(%s);",al_id)
       row = cur.fetchall()
       print(row)
       return render_template('作业地址_form.html',row=row)

    if request.method == 'POST':
       id_work_location_f =  request.form.get('id_work_location_f')
       work_location_form_name =  request.form.get('work_location_form_name')
       work_location_form_type =  request.form.get('work_location_form_type')

       cur.execute("update work_location set work_location_name=(%s),work_location_type=(%s) where id=(%s);",
                   (work_location_form_name,work_location_form_type,id_work_location_f))
       conn.commit()
       return redirect('work_location_list')

@app.route('/work_location_create',methods=['POST','GET'])
def work_location_create():
    if request.method == 'GET':

       return render_template('作业地址_create.html')

    if request.method == 'POST':
        work_location_name = request.form.get('work_location_form_name')
        work_location_type = request.form.get('work_location_form_type')
        cur.execute("insert into work_location(work_location_name,work_location_type) values(%s,%s);",(work_location_name,work_location_type))
        conn.commit()
        return redirect('work_location_list')


@app.route('/work_location_delete',methods=['POST','GET'])
def work_location_delete():
    al_id= request.args.get('al_id')
    cur.execute("delete from work_location where id=(%s);",al_id)
    conn.commit()
    return redirect('work_location_list')


@app.route('/img',methods=['POST','GET'])
def img():
    if request.method == 'GET':
     return render_template('hel.html')

     if request.method == 'POST':
         iag = request.form.get('file')

@app.route('/dt_log',methods=['POST','GET'])
def dt_l():
    usesa = [1,2,3,4,5]
    uom = ['斤','量']
    id = 1
    u_u = [usesa,uom,id]
    return jsonify(u_u)

@app.route('/dro',methods=['POST','GET'])
def dat():

    if request.method == 'GET':
        ids = request.args.get("rec_id")
        print(ids)

    return render_template('登录.html')

if __name__ == '__main__':
    app.run()