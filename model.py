# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:37:14 2016

@author: EKish
"""

from wtforms import Form, StringField, validators

class InputForm(Form):
    XPrime = StringField(label='dx/dt = ', default='y', validators=[validators.InputRequired()])
    YPrime = StringField(label='dy/dt = ', default='-x', validators=[validators.InputRequired()])
    