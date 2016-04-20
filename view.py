# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 14:39:48 2016

@author: EKish
"""

from model import InputForm
from flask import Flask, render_template, request
from compute import phasePlot

app = Flask(__name__)

@app.route('/dyn', methods=['GET', 'POST'])
def index():
    form = InputForm(request.form)
    if request.method == 'POST' and form.validate():
        result = phasePlot(form.XPrime.data, form.YPrime.data)
    else:
        result = None
        
    return render_template('new_view.html', form=form,result=result)
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')