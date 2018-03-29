import flask
import flask_sqlalchemy
import flask_restless
from sqlalchemy import Column, Date, Integer, String
import os

# Create the Flask application and the Flask-SQLAlchemy object.
app = flask.Flask(__name__)

app.config['DEBUG'] = True

svc_name = os.environ.get('SVC_NAME', '')
if not svc_name:
    print('svc_name is null, use DB_HOST and DB_PORT...')
    host = os.environ.get('DB_HOST', 'localhost')
    port = os.environ.get('DB_PORT', '3306')
else:
    print('svc_name is not null: ', + svc_name + 'use SERVICE_HOST and SERVICE_PORT...')
    svc_name = svc_name.upper()
    host = os.environ.get(svc_name + '_SERVICE_HOST', 'localhost')
    port = os.environ.get(svc_name + '_SERVICE_PORT', '3306')

dbname = os.environ.get('DB_DBNAME','demo1')
username = os.environ.get('DB_USERNAME', 'root')
password = os.environ.get('DB_PASSWORD', 'secret')
uri = 'mysql://' + username + ':' + password + '@' + host + ':' + port + '/' + dbname
print(uri)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
#'mysql://root:secret@127.0.0.1/demo1'
db = flask_sqlalchemy.SQLAlchemy(app)


# Create your Flask-SQLALchemy models as usual but with the following
# restriction: they must have an __init__ method that accepts keyword
# arguments for all columns (the constructor in
# flask_sqlalchemy.SQLAlchemy.Model supplies such a method, so you
# don't need to declare a new one).
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(String(16))
    birth_date = db.Column(db.Date)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(String(16))
    published_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    author = db.relationship(Person, backref=db.backref('articles',
                                                        lazy='dynamic'))


# Create the database tables.
db.create_all()

# Create the Flask-Restless API manager.
manager = flask_restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Person, methods=['GET', 'POST', 'DELETE'])
manager.create_api(Article, methods=['GET'])

# start the flask loop
app.run(host='0.0.0.0', threaded=True, debug=True)
