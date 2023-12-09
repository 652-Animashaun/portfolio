from flask import Flask, render_template, request, redirect, url_for
from flask_admin import Admin
import json
import os
from dotenv import load_dotenv
from flask_admin.contrib.sqla import ModelView
from pymongo import MongoClient, ReturnDocument
import datetime as dt
from serializers import *
from wtforms import Form, fields, StringField, validators, BooleanField, TextAreaField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId
from flask_s3 import FlaskS3
import logging



# client = MongoClient('mongodb://user:pass@mongo_db')
# db = client.flask_db
# blogs_col = db.blogs
# portfolio_col = db.portfolio

# print(blogs_col)

# # Create models
# conn = pymongo.Connection()
# db = conn.test

app = Flask(__name__)
s3 = FlaskS3()
load_dotenv()
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
app.config['FLASKS3_BUCKET_NAME'] = os.getenv("FLASKS3_BUCKET_NAME")
# app.config['SECRET_KEY'] = '123456790'

# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


class BlogForm(Form):
    title = StringField('Title', [validators.Length(min=10, max=256)])
    description = StringField('Description', [validators.Length(min=10, max=256)])
    body = TextAreaField('Body', [validators.Length(min=256)])
    author = StringField('Author')


class BlogView(ModelView):
    column_list = ('title', 'description', 'body', 'author')
    column_sortable_list = ('title', 'description', 'body', 'author')

    form = BlogForm



@app.route("/")
def home():
    if request.args.get('command') == 'code':
        return redirect('https://github.com/652-Animashaun')
    if request.args.get('command') == 'cv':
        return redirect('https://docs.google.com/document/d/1UaL_FxfmxVfMiif2Q-CLepKQLI3rm61_eLT6ohaAzhs/edit?usp=sharing')
    else:
        return render_template('index.html')






@app.route("/<content_type>", methods=["GET"])
def blog(content_type):
    if content_type == 'blog':
        schema = BlogSchema(many=True)
        blogs = blogs_col.find()
        blogs = schema.dump(blogs)
        return blogs
    if content_type == 'portfolio':
        schema = PortfolioSchema(many=True)
        portfolio = portfolio_col.find()
        portfolio = schema.dump(blogs)
        return portfolio
    return redirect(url_for('home'))


@app.route("/admin/add_content", methods = ['POST'])
def insert_content():
    # if request.method=='POST':
    data = request.json
    if data.get('content_type') =='blog':
        print("blog")
        schema = BlogSchema()
        data.update({
            "published":str(dt.datetime.now()),
            "last_revision":str(dt.datetime.now()),
            })
        data = schema.load(data)
        # data_dict = json.loads(data)
        del data["content_type"]
        blogs_col.insert_one({**data})
        blogs = blogs_col.find()
        schema_list = BlogSchema(many=True)
        blogs = schema_list.dump(blogs)
        return (blogs)
    if data.get('content_type') == 'portfolio':
        schema = PortfolioSchema()
        data = schema.load(data)
        portfolio_col.insert_one({**data})
        schema_list = BlogSchema(many=True)
        portfolio = portfolio_col.find()
        portfolio = schema_list.dump(portfolio)
        return portfolio
    return ({"ERROR": "Invalid Content Type"})


@app.route("/admin/update_content/<content_type>/<content_id>", methods = ["GET", "POST"])
def update_content(content_type, content_id):


    obj_id = ObjectId(content_id)
    if request.method == "POST":
        if content_type == 'blog':
            schema = BlogSchema()
            revised_data = request.json
            
            revised_data.update({
            "last_revision":str(dt.datetime.now()),
            # "published":str(dt.datetime.now()),
            })
            revised_data = schema.load(revised_data)
            blog = blogs_col.find_one_and_update({"_id":obj_id}, {'$set':{**revised_data}}, return_document = ReturnDocument.AFTER)
            blog = schema.dump(blog)
            return blog

            blog = blogs_col.find_one({"_id":obj_id})
            blog = schema.dump(blog)
            print(blog)
            return blog
        elif content_type == 'portfolio':
            schema = PortfolioSchema()
            obj_id = ObjectId(content_id)

            revised_data = request.json
            revised_data = schema.load(revised_data)
            portfolio = portfolio_col.find_one_and_update({"_id":obj_id}, {'$set':{**revised_data}}, return_document = ReturnDocument.AFTER)
            portfolio = schema.dump(portfolio)
            return portfolio
        else:
            return ({"ERROR": "Invalid Content Type"})



if __name__ == '__main__':
    s3.init_app(app, bucket_name=app.config['FLASKS3_BUCKET_NAME'])
    app.run(port=5000,debug=True)
