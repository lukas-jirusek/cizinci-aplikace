
def apiResponse(templateData):
    response = {
        "input_parameters": {
            "start_year": "2014",
            "end_year": "2022",
            "area_kod": "19",
            "narodnost_kod": "0"
        },
        "status": {
            "valid" : True,
            "error_message": ""
        },
        "data": {
            "nationality_string" : "",
            "area_string" : "",
            "total_foreigners": 0,
            "age_pyramid" : {
                
            },
            "gender_split" : {
                
            }
        }
    }
    
    if templateData["chartData"]["display"]:
        response["data"]["time_data"] = {}
    
    if templateData["subregionYearTable"]["display"]:
        response["data"]["subregion_year_table"] = {
            "columns" : templateData["subregionYearTable"]["headers"],
            "rows": templateData["subregionYearTable"]["first_col"],
            "data": templateData["subregionYearTable"]["data"]
        }
    
    if templateData["nationalityYearTable"]["display"]:
        response["data"]["nationality_year_table"] = {
            "columns" : templateData["nationalityYearTable"]["headers"],
            "rows": templateData["nationalityYearTable"]["first_col"],
            "data": templateData["nationalityYearTable"]["data"]
        }






    for key in response["input_parameters"]:
        response["input_parameters"][key] = templateData["parameters"][key]
    
    response["data"]["nationality_string"] = templateData["parameters"]["narodnost"]
    response["data"]["area_string"] = templateData["parameters"]["area"]
    response["data"]["total_foreigners"] = templateData["totalCount"]["current"]
    
    for label, value in zip(templateData["ageChart"]["labels"], templateData["ageChart"]["values"]):
        response["data"]["age_pyramid"][label] = value
        
    for label, value in zip(templateData["pieData"]["labels"], templateData["pieData"]["values"]):
        response["data"]["gender_split"][label] = value
        
    if templateData["chartData"]["display"]:
        for label, value in zip(templateData["chartData"]["labels"], templateData["chartData"]["values"]):
            response["data"]["time_data"][label] = value
    
    return response
        
        
        
        


