from copy import deepcopy


ageLabels = [
    "<0 - 5)",
    "<5 - 10)",
    "<10 - 15)",
    "<15 - 20)",
    "<20 - 25)",
    "<25 - 30)",
    "<30 - 35)",
    "<35 - 40)",
    "<40 - 45)",
    "<45 - 50)",
    "<50 - 55)",
    "<55 - 60)",
    "<60 - 65)",
    "<65 - 70)",
    "<70 - 75)",
    "<75 - 80)",
    "<80 - 85)",
    "<85 - N)",
]

ageCodes = [
    "400000600005000",
    "400005610010000",
    "410010610015000",
    "410015610020000",
    "410020610025000",
    "410025610030000",
    "410030610035000",
    "410035610040000",
    "410040610045000",
    "410045610050000",
    "410050610055000",
    "410055610060000",
    "410060610065000",
    "410065610070000",
    "410070610075000",
    "410075610080000",
    "410080610085000",
    "410085799999000",
]

genderCodes = ["1", "2"]

data = {
    "parameters": None,
    "totalCount": {"current": 0, "last": None, "change": ""},
    "ageChart": {"labels": ageLabels, "values": []},
    "pieData": {"labels": ["Muži", "Ženy"], "values": []},
    "chartData": {"display": True, "labels": [], "values": []},
    "subregionYearTable": {
        "display": False,
        "data": [[]],
        "headers": [],
        "first_col": [],
    },
    "nationalityYearTable": {
        "display": False,
        "data": [[]],
        "headers": [],
        "first_col": [],
    }
}


def create_data():
    return deepcopy(data)
