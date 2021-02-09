    # import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#################################################
# Database Setup
#################################################

from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
# N.B. external config.py file should be formatted like:
# login = 'postgres:password' where password is set to whatever your database password is. Default username is 
# postgres, but change this if you use a different username.
import psycopg2
# postgres_str = ('postgresql://{username}:{password}@{ipaddress}:{port}/{dbname}'
#                 .format(username='postgres',
#                         password='postgres',
#                         ipaddress='localhost',
#                         port=5432,
#                         dbname='flask_deploy'))


app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = postgres_str
    # Create the connection
engine = create_engine(postgres_str)
connection = engine.connect()
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
    # app.debug = False




db = SQLAlchemy(app)

Base = automap_base()
Base.prepare(engine, reflect=True)
Pets = Base.classes.pets

from sqlalchemy import select, insert
select_stmt = select([Pets])

data = connection.execute(select_stmt).fetchall()


# create route that renders index.html template
@app.route("/")
def home():


    return render_template("index.html", data=data)


@app.route('/addition')

def additon():
    select_stmt2 = select([Pets])
    data1 = connection.execute(select_stmt2).fetchall()
    return render_template("index.html", data=data1)






if __name__ == "__main__":
    app.run()


