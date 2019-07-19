from flask import Blueprint

bp = Blueprint('graphs', __name__)

from app.graphs import bar_line
