from flask import Flask, render_template, request, jsonify

from narodnosti import narodnosti
from oblasti import oblasti

from query_logic import getData
from dataDictionary import data as templateData
from response import apiResponse

import sqlite3

import json

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


def processParameters(params, req):
    if req.method == "POST":
        if "start_year" in req.form:
            params["start_year"] = req.form["start_year"]
        if "end_year" in req.form:
            params["end_year"] = req.form["end_year"]
        if "okres-dropdown" in req.form:
            params["area_kod"] = req.form["okres-dropdown"]
        if "narodnostRadio" in req.form:
            params["narodnost_kod"] = req.form["narodnostRadio"]
        
        return True

    elif req.args:
        for key, value in req.args.items():
            if key in params:
                params[key] = value
            else:
                return key
    
    return True

def checkParameters(parameters):
    validYears = [str(y) for y in range(2004, 2023)]
    start = parameters["start_year"]
    end = parameters["end_year"]
    
    if start not in validYears:
        return "Neplatná hodnota pro parametr start_year: " + start
    
    if end not in validYears:
        return "Neplatná hodnota pro parametr end_year: " + end

    if start > end:
        return "Hodnota parametru start_year nesmí být větší než hodnota end_year."

    narodnost = parameters["narodnost_kod"]
    oblast = parameters["area_kod"]
    
    if narodnost not in narodnosti:
        return "Neplatná hodnota pro parametr narodnost_kod: " + narodnost
    
    if oblast not in oblasti:
        return "Neplatná hodnota pro parametr area_kod: " + oblast
    
    return True
    
    
@app.route("/api")
def api():
    
    #zpracovani parametru
    parametry = {
        "start_year": "2014",
        "end_year": "2022",
        "area_kod": "19",
        "narodnost_kod": "0"
    }

    res = processParameters(parametry, request)
    if res != True:
        templateData["parameters"] = parametry
        
        parametry["area"] = ""
        parametry["narodnost"] = ""
        
        apiResult = apiResponse(templateData)
        del apiResult["data"]
        apiResult["status"]["valid"] = False
        apiResult["status"]["error_message"] = "Neplatný URL paremetr: " + res
        
        return jsonify(apiResult)
    
    res = checkParameters(parametry)
    if res != True:
        templateData["parameters"] = parametry
        parametry["area"] = ""
        parametry["narodnost"] = ""
        
        apiResult = apiResponse(templateData)
        del apiResult["data"]
        apiResult["status"]["valid"] = False
        apiResult["status"]["error_message"] = res
        
        return jsonify(apiResult)
    

    #mapovaní národností a oblasti
    parametry["area"] = oblasti[parametry["area_kod"]]
    parametry["narodnost"] = narodnosti[parametry["narodnost_kod"]]

    #provedení dotazu
    templateData["parameters"] = parametry
    with sqlite3.connect("cizinci.db") as conn:
        getData(templateData, conn.cursor())

    apiResult = apiResponse(templateData)

    return jsonify(apiResult)


@app.route("/", methods=["GET", "POST"])
def index():
    
    #zpracovani parametru
    parametry = {
        "start_year": "2014",
        "end_year": "2022",
        "area_kod": "19",
        "narodnost_kod": "0"
    }

    res = processParameters(parametry, request)
    if res != True:
        templateData["parameters"] = parametry
        res = "Neplatný URL paremetr: " + res
        return render_template("index.jinja", data=templateData, error=True, message=res)
    
    res = checkParameters(parametry)
    if res != True:
        templateData["parameters"] = parametry
        return render_template("index.jinja", data=templateData, error=True, message=res)
    
    #vytvoreni URL adres
    urls = {
        "this": "",
        "api": ""
    }
    
    urls["this"] = request.base_url + "?" + "&".join(f"{key}={value}" for key, value in parametry.items())
    urls["api"] = request.base_url + "api?" + "&".join(f"{key}={value}" for key, value in parametry.items())
    
    

    #mapovaní národností a oblasti
    parametry["area"] = oblasti[parametry["area_kod"]]
    parametry["narodnost"] = narodnosti[parametry["narodnost_kod"]]


    #provedení dotazu
    templateData["parameters"] = parametry
    with sqlite3.connect("cizinci.db") as conn:
        getData(templateData, conn.cursor())


    return render_template("index.jinja", data=templateData, urls=urls, error=False)


if __name__ == "__main__":
    app.run(debug=True)
