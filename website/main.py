from flask import Flask, render_template, Blueprint, request, redirect, url_for,flash
from flask_mysqldb import MySQL

mysql = MySQL()


available_bikes = [
    {"id": 1, "name": "Bike 1"},
    {"id": 2, "name": "Bike 2"},
    {"id": 3, "name": "Bike 3"}
]
# Define the blueprint and register it with the app
bikes_blueprint = Blueprint('bikes', __name__)

def create_app():
    app = Flask(__name__)
    app.secret_key = 'secret_key'

    # MySQL configurations
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'Curry4mvp'
    app.config['MYSQL_DB'] = 'save_my_wheelies'
    app.config['MYSQL_HOST'] = 'localhost'
    mysql.init_app(app)

    return app

app = create_app()

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM bikes")
    bikes = cur.fetchall()
    cur.close()
    return render_template('index.html', bikes=available_bikes)

''''
@app.route('/')
def index():
    bikes = [{'type': 'Mountain Bike', 'fee_minute': 5}, {'type': 'City Bike', 'fee_minute': 3}]
    return render_template('index.html', bikes=bikes)
'''

@app.route('/rent', methods=['GET', 'POST'])
def rent():
    if request.method == 'POST':
        user = request.form['user']
        bike = request.form['bike']
        lock = request.form['lock']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO rentals (User, Bike, Lock_id, start_time, end_time) VALUES (%s, %s, %s, %s, %s)", (user, bike, lock, start_time, end_time))
        mysql.connection.commit()
        cur.close()
        return render_template('rent.html', available_bikes=available_bikes)
        return redirect(url_for('index'))
    else:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bikes")
        bikes = cur.fetchall()
        cur.execute("SELECT * FROM locks WHERE is_locked = 0 AND is_admin_locked = 0")
        locks = cur.fetchall()
        cur.close()
        return render_template('bikes.html', bikes=bikes, locks=locks)



@app.route('/rent-bike', methods=['GET', 'POST'])

def rent_bike():
    if request.method == 'POST':
        # Handle form submission
        # Extract the form data
        bike_id = request.form['bike_id']
        lock_id = request.form['lock_id']
        # Do something with the data (e.g. update the database)
        # ...
        # Return a response to the user (e.g. a confirmation message)
        flash('You have successfully rented a bike!')
        return redirect(url_for('index'))
    else:
        # Render the rent bike form
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM bikes WHERE is_rented = 0")
        bikes = cur.fetchall()
        cur.execute("SELECT * FROM locks WHERE is_locked = 0 AND is_admin_locked = 0")
        locks = cur.fetchall()
        cur.close()
        return render_template('rent.html', bikes=bikes, locks=locks)

if __name__ == "__main__":
    app.run(debug=True)
