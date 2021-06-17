from application import app
from datetime import datetime
import json
from application.model.entity.medicao import Medicao
from application.model.dao.medicaoDAO import MedicaoDAO, medicao_list
from flask import jsonify, request


@app.route("/metricas", methods=["GET"])
def exibirmedicao():
    medicao_list_dict = []
    for i in medicao_list.listarMedicoes():
        medicao_list_dict.append(i.toDict())  
    return jsonify(medicao_list_dict)


@app.route("/metricas", methods=["POST"])
def addmedicao():
    id = int(request.json.get("id", None))
    matparticulado = float(request.json.get("matparticulado", None))
    ozonio = float(request.json.get("ozonio", None))
    mono_carbono = float(request.json.get("mono_carbono", None))
    oxi_nitroso = float(request.json.get("oxi_nitroso", None))
    data = request.json.get("data", None)
    medicao = Medicao(id, matparticulado, ozonio, mono_carbono, oxi_nitroso, data)
    medicao_list.adicionarMedicoes(medicao)
    return medicao.toDict(), 201


@app.route("/metricas/id/<id>", methods=["GET"])
def buscamedicaoid(id):
    medicao_list_dict = []
    for i in medicao_list.listarMedicoes():
        if int(i.get_id()) == int(id):
            medicao_list_dict.append(i.toDict())  
    return jsonify(medicao_list_dict)


@app.route("/metricas/data/<data>", methods=["GET"])
def buscamedicaodata(data):
    medicao_list_dict = []
    for i in medicao_list.listarMedicoes():
        datasembarra = i.get_data().replace("/", "")
        if datasembarra == data:
            medicao_list_dict.append(i.toDict())  
    return jsonify(medicao_list_dict)


