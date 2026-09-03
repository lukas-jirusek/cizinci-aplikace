"""
Unified query logic - routes all queries through a single parameterized function
Replaces 12 individual query modules with one dynamic engine
"""

from copy import deepcopy
from functools import lru_cache
import sqlite3

from oblasti import oblasti
from narodnosti import narodnosti
from dataDictionary import create_data
from unified_queries import execute_unified_query


def getData(data, cur):
    """
    Main entry point for data queries.
    Delegates to the unified query engine which handles all query scenarios.
    """
    execute_unified_query(data, cur)


@lru_cache(maxsize=256)
def _get_cached_data(start_year, end_year, area_kod, obcanstvi_kod):
    data = create_data()
    data["parameters"] = {
        "start_year": start_year,
        "end_year": end_year,
        "area_kod": area_kod,
        "obcanstvi_kod": obcanstvi_kod,
        "area": oblasti[area_kod],
        "narodnost": narodnosti[obcanstvi_kod],
    }

    with sqlite3.connect("cizinci.db") as conn:
        execute_unified_query(data, conn.cursor())

    return data


def get_cached_data(parameters):
    data = _get_cached_data(
        parameters["start_year"],
        parameters["end_year"],
        parameters["area_kod"],
        parameters["obcanstvi_kod"],
    )
    return deepcopy(data)


