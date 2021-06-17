from datetime import datetime 
from application.model.entity.medicao import medicao
from application.model.dao.medicaoDAO import medicaoDAO, medicao_list
from flask import request, redirect, jsonify



@app.route ("/medicao"):
def exibirmedicao():
    medicao_list

