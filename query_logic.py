"""
Unified query logic - routes all queries through a single parameterized function
Replaces 12 individual query modules with one dynamic engine
"""

from unified_queries import execute_unified_query


def getData(data, cur):
    """
    Main entry point for data queries.
    Delegates to the unified query engine which handles all query scenarios.
    """
    execute_unified_query(data, cur)


