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
