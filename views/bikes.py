from flask import Blueprint, render_template
from app.models import Bike

bikes_blueprint = Blueprint('bikes', __name__)

@bikes_blueprint.route('/bikes')
def bikes():
    bikes = Bike.query.all()
    return render_template('bikes.html', bikes=bikes)
