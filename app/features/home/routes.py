from flask import render_template

from app.features.home import home_bp

import os


@home_bp.route("/")
def index():
    return render_template("home/index.html")
