from oblasti import oblasti
from narodnosti import narodnosti

import pandas as pd


def IrokInarOkres(data, cur):
    params = data["parameters"]


    # soucet 
    query = f"""SELECT 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok = '{params["end_year"]}' AND  
        obcanstvi_kod = '{params["narodnost_kod"]}' AND
        okres_kod = '{params["area_kod"]}';
    """
    cur.execute(query)
    current = cur.fetchall()[0][0]
    
    if params["end_year"] != "2004":
        # soucet 
        query = f"""SELECT 
            SUM(hodnota) AS total_foreigners
        FROM 
            zaznam_denormalised
        WHERE 
            rok = '{int(params["end_year"]) - 1}' AND  
            obcanstvi_kod = '{params["narodnost_kod"]}' AND
            okres_kod = '{params["area_kod"]}';
        """
        cur.execute(query)
        prev = cur.fetchall()[0][0]
        if current > prev:
            change = f"+ {current - prev}"
        else:
            change = f"- {prev - current}"
    else:
        prev = False
        change = False
    
    data["totalCount"]["current"] = current
    data["totalCount"]["last"] = prev
    data["totalCount"]["change"] = change

    # vekova
    ageQuery = f"""SELECT 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok = '{params["end_year"]}' AND  
        obcanstvi_kod = '{params["narodnost_kod"]}' AND
        okres_kod = '{params["area_kod"]}'
    GROUP BY 
        vek_kod
    ORDER BY 
        vek_kod;
    """

    cur.execute(ageQuery)
    result = cur.fetchall()
    data["ageChart"]["values"] = [x[0] for x in result]

    # pohlavi
    genderQuery = f"""SELECT 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok = '{params["end_year"]}' AND  
        obcanstvi_kod = '{params["narodnost_kod"]}' AND
        okres_kod = '{params["area_kod"]}'
    GROUP BY 
        pohlavi_kod
    ORDER BY 
        pohlavi_kod;
    """

    cur.execute(genderQuery)
    result = cur.fetchall()
    data["pieData"]["values"] = [x[0] for x in result]

    # vyvoj
    data["chartData"]["display"] = False

    # areas / year
    data["subregionYearTable"]["display"] = False

    # narodnost / rok
    data["nationalityYearTable"]["display"] = False