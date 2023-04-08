from flask import Blueprint, render_template
from flask_mysqldb import MySQL
from flask import Flask

app = Flask(__name__)
@app.route('/')
def index():
    return "Hello, world!"


rentals_bp = Blueprint('rentals', __name__)

@rentals_bp.route('/rentals')
def rentals():
    # connect to MySQL database
    mysql = MySQL()
    mysql.init_app(app)

    # execute a SELECT statement to get rental data from the database
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM rentals")
    rental_data = cur.fetchall()

    # render the rentals.html template and pass in the rental data as a variable
    return render_template('rentals.html', rental_data=rental_data)
