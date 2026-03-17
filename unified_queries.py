"""
Unified query module - consolidates all 12 query modules into parameterized functions
Replaces: IrokInarCR, IrokXnarCR, IrokInarKraj, IrokXnarKraj, IrokInarOkres, IrokXnarOkres,
         XrokInarCR, XrokXnarCR, XrokInarKraj, XrokXnarKraj, XrokInarOkres, XrokXnarOkres
"""

from oblasti import oblasti
from narodnosti import narodnosti
import pandas as pd


def execute_unified_query(data, cur):
    """
    Unified query engine that handles all 12 query scenarios dynamically.
    Uses parameterized queries to prevent SQL injection.
    
    Parameters are extracted from data["parameters"]:
    - start_year, end_year: year range
    - obcanstvi_kod: nationality code ("0" = all nationalities)
    - area_kod: region code ("19" = whole CR, 4-digit = region, 5-digit = district)
    """
    params = data["parameters"]
    
    # Determine query type
    is_single_year = params["start_year"] == params["end_year"]
    is_single_nationality = params["obcanstvi_kod"] != "0"
    area_kod = params["area_kod"]
    
    if area_kod == "19":
        area_type = "CR"
    elif len(area_kod) == 4:
        area_type = "kraj"
    else:
        area_type = "okres"
    
    # Helper function to build parameterized WHERE clause
    def build_where_clause(include_year_range=False):
        """Build WHERE clause with parameters"""
        where_parts = []
        query_params = []
        
        if include_year_range and not is_single_year:
            where_parts.append("rok BETWEEN ? AND ?")
            query_params.extend([params['start_year'], params['end_year']])
        else:
            where_parts.append("rok = ?")
            query_params.append(params['end_year'])
        
        if is_single_nationality:
            where_parts.append("obcanstvi_kod = ?")
            query_params.append(params['obcanstvi_kod'])
        
        if area_type == "kraj":
            where_parts.append("kraj_kod = ?")
            query_params.append(params['area_kod'])
        elif area_type == "okres":
            where_parts.append("okres_kod = ?")
            query_params.append(params['area_kod'])
        
        where_clause = " AND ".join(where_parts)
        return where_clause, query_params
    
    # 1. TOTAL COUNT (current and previous year)
    current_where = "rok = ?"
    current_params = [params["end_year"]]
    
    if is_single_nationality:
        current_where += " AND obcanstvi_kod = ?"
        current_params.append(params['obcanstvi_kod'])
    
    if area_type == "kraj":
        current_where += " AND kraj_kod = ?"
        current_params.append(params['area_kod'])
    elif area_type == "okres":
        current_where += " AND okres_kod = ?"
        current_params.append(params['area_kod'])
    
    query_current = f"SELECT SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {current_where}"
    cur.execute(query_current, current_params)
    current = cur.fetchall()[0][0]
    
    prev = False
    change = False
    if params["end_year"] != "2004":
        prev_year = str(int(params["end_year"]) - 1)
        prev_where = "rok = ?"
        prev_params = [prev_year]
        
        if is_single_nationality:
            prev_where += " AND obcanstvi_kod = ?"
            prev_params.append(params['obcanstvi_kod'])
        
        if area_type == "kraj":
            prev_where += " AND kraj_kod = ?"
            prev_params.append(params['area_kod'])
        elif area_type == "okres":
            prev_where += " AND okres_kod = ?"
            prev_params.append(params['area_kod'])
        
        query_prev = f"SELECT SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {prev_where}"
        cur.execute(query_prev, prev_params)
        prev = cur.fetchall()[0][0]
        if current > prev:
            change = f"+ {current - prev}"
        else:
            change = f"- {prev - current}"
    
    data["totalCount"]["current"] = current
    data["totalCount"]["last"] = prev
    data["totalCount"]["change"] = change
    
    # 2. AGE DISTRIBUTION
    where_clause, where_params = build_where_clause(include_year_range=True)
    age_query = f"SELECT SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY vek_kod ORDER BY vek_kod"
    cur.execute(age_query, where_params)
    result = cur.fetchall()
    data["ageChart"]["values"] = [x[0] for x in result]
    
    # 3. GENDER SPLIT
    gender_query = f"SELECT SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY pohlavi_kod ORDER BY pohlavi_kod"
    cur.execute(gender_query, where_params)
    result = cur.fetchall()
    data["pieData"]["values"] = [x[0] for x in result]
    
    # 4. TIME SERIES (only for multi-year queries)
    data["chartData"]["display"] = not is_single_year
    if not is_single_year:
        time_series_query = f"SELECT rok AS year, SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY rok ORDER BY rok"
        cur.execute(time_series_query, where_params)
        result = cur.fetchall()
        data["chartData"]["labels"] = [x[0] for x in result]
        data["chartData"]["values"] = [x[1] for x in result]
    
    # 5. REGIONAL/DISTRICT BREAKDOWN
    if area_type == "CR":
        # Show breakdown by region (kraj)
        regional_query = f"SELECT rok AS year, kraj_kod AS region, SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY rok, kraj_kod ORDER BY rok, kraj_kod"
    elif area_type == "kraj":
        # Show breakdown by district (okres)
        regional_query = f"SELECT rok AS year, okres_kod AS region, SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY rok, okres_kod ORDER BY rok, okres_kod"
    else:
        # okres - no further subregions to show
        regional_query = None
    
    if regional_query:
        cur.execute(regional_query, where_params)
        subregions = cur.fetchall()
        subregions = sorted([(x[0], oblasti[x[1]], x[2]) for x in subregions], key=lambda x: x[1])
        
        df = pd.DataFrame(subregions, columns=['Year', 'Nationality', 'Count'])
        pivot_table = df.pivot(index='Nationality', columns='Year', values='Count').fillna(0).convert_dtypes(convert_integer=True)
        
        # Add total row
        area_name = oblasti[params["area_kod"]]
        if area_type == "CR":
            total_label = "Celá ČR"
        else:
            total_label = f"Celý {area_name}"
        pivot_table.loc[total_label] = pivot_table.sum(axis=0)
        
        headers = pivot_table.columns.tolist()
        index = pivot_table.index.tolist()
        values = pivot_table.values.tolist()
        
        data["subregionYearTable"]["display"] = True
        data["subregionYearTable"]["headers"] = headers
        data["subregionYearTable"]["first_col"] = index
        data["subregionYearTable"]["data"] = values
    else:
        data["subregionYearTable"]["display"] = False
    
    # 6. NATIONALITY BREAKDOWN (only for all-nationality + region/district queries)
    if not is_single_nationality and area_type in ["kraj", "CR"]:
        nationality_query = f"SELECT rok AS year, obcanstvi_kod, SUM(hodnota) AS total_foreigners FROM zaznam_denormalised WHERE {where_clause} GROUP BY rok, obcanstvi_kod ORDER BY rok, obcanstvi_kod"
        cur.execute(nationality_query, where_params)
        nationalities_data = cur.fetchall()
        nationalities_data = sorted([(x[0], narodnosti[x[1]], x[2]) for x in nationalities_data], key=lambda x: x[1])
        
        df = pd.DataFrame(nationalities_data, columns=['Year', 'Nationality', 'Count'])
        pivot_table = df.pivot(index='Nationality', columns='Year', values='Count').fillna(0).convert_dtypes(convert_integer=True)
        pivot_table = pivot_table.sort_values(by=pivot_table.columns[-1], ascending=False)
        
        headers = pivot_table.columns.tolist()
        index = pivot_table.index.tolist()
        values = pivot_table.values.tolist()
        
        data["nationalityYearTable"]["display"] = True
        data["nationalityYearTable"]["headers"] = headers
        data["nationalityYearTable"]["first_col"] = index
        data["nationalityYearTable"]["data"] = values
    else:
        data["nationalityYearTable"]["display"] = False
