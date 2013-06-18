# -*- coding: utf-8 *-*

from flask import Flask
from pymyadmin.admin import setup_admin_for


app = Flask(__name__)
setup_admin_for(app)


app.run(debug=True)
