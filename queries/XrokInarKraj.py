from oblasti import oblasti
from narodnosti import narodnosti

import pandas as pd


def XrokInarKraj(data, cur):
    params = data["parameters"]


    # soucet 
    query = f"""SELECT 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok = '{params["end_year"]}' AND
        obcanstvi_kod = '{params["narodnost_kod"]}' AND
        kraj_kod = '{params["area_kod"]}';
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
            kraj_kod = '{params["area_kod"]}';
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
        kraj_kod = '{params["area_kod"]}'
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
        kraj_kod = '{params["area_kod"]}'
    GROUP BY 
        pohlavi_kod
    ORDER BY 
        pohlavi_kod;
    """

    cur.execute(genderQuery)
    result = cur.fetchall()
    data["pieData"]["values"] = [x[0] for x in result]

    # vyvoj
    
    query = f"""SELECT 
    rok AS year, 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok BETWEEN '{params["start_year"]}' AND '{params["end_year"]}' AND
        kraj_kod = '{params["area_kod"]}' AND
        obcanstvi_kod = '{params["narodnost_kod"]}'
    GROUP BY 
        rok
    ORDER BY 
        rok;
    """

    data["chartData"]["display"] = True
    cur.execute(query)
    result = cur.fetchall()
    data["chartData"]["labels"] = [x[0] for x in result]
    data["chartData"]["values"] = [x[1] for x in result]

    # areas / year
    query = f"""
    SELECT 
        rok AS year, 
        okres_kod AS region, 
        SUM(hodnota) AS total_foreigners
    FROM 
        zaznam_denormalised
    WHERE 
        rok BETWEEN '{params["start_year"]}' AND '{params["end_year"]}' AND
        obcanstvi_kod = '{params["narodnost_kod"]}' AND
        kraj_kod = '{params["area_kod"]}'
    GROUP BY 
        rok, okres_kod
    ORDER BY 
        rok, okres_kod;
    """
    cur.execute(query)
    subregions = cur.fetchall()
    
    subregions = sorted([(x[0], oblasti[x[1]], x[2]) for x in subregions], key=lambda x: x[1])
    
    df = pd.DataFrame(subregions, columns=['Year', 'Nationality', 'Count'])
    
    pivot_table = df.pivot(index='Nationality', columns='Year', values='Count').fillna(0).convert_dtypes(convert_integer=True)
    pivot_table.loc[f'Celý {oblasti[params["area_kod"]]}'] = pivot_table.sum(axis=0)
    
    headers = pivot_table.columns.tolist()
    index = pivot_table.index.tolist()
    values = pivot_table.values.tolist()
    
    
    data["subregionYearTable"]["display"] = True
    data["subregionYearTable"]["headers"] = headers
    data["subregionYearTable"]["first_col"] = index
    data["subregionYearTable"]["data"] = values

    # narodnost / rok
    data["nationalityYearTable"]["display"] = False
