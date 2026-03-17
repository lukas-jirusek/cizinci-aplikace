#!/usr/bin/env python3
"""
Create database indexes for optimal query performance
Run this once to add indexes to the SQLite database
"""

import sqlite3
import time

def create_indexes():
    """Create indexes on frequently filtered columns"""
    
    conn = sqlite3.connect("cizinci.db")
    cursor = conn.cursor()
    
    indexes = [
        # Single column indexes
        ("idx_rok", "CREATE INDEX IF NOT EXISTS idx_rok ON zaznam_denormalised(rok)"),
        ("idx_obcanstvi_kod", "CREATE INDEX IF NOT EXISTS idx_obcanstvi_kod ON zaznam_denormalised(obcanstvi_kod)"),
        ("idx_kraj_kod", "CREATE INDEX IF NOT EXISTS idx_kraj_kod ON zaznam_denormalised(kraj_kod)"),
        ("idx_okres_kod", "CREATE INDEX IF NOT EXISTS idx_okres_kod ON zaznam_denormalised(okres_kod)"),
        
        # Composite indexes for common WHERE + GROUP BY combinations
        ("idx_rok_obcanstvi", "CREATE INDEX IF NOT EXISTS idx_rok_obcanstvi ON zaznam_denormalised(rok, obcanstvi_kod)"),
        ("idx_rok_kraj", "CREATE INDEX IF NOT EXISTS idx_rok_kraj ON zaznam_denormalised(rok, kraj_kod)"),
        ("idx_rok_okres", "CREATE INDEX IF NOT EXISTS idx_rok_okres ON zaznam_denormalised(rok, okres_kod)"),
        ("idx_rok_vek", "CREATE INDEX IF NOT EXISTS idx_rok_vek ON zaznam_denormalised(rok, vek_kod)"),
    ]
    
    print("Creating database indexes...")
    print("-" * 50)
    
    start_time = time.time()
    
    for index_name, sql in indexes:
        try:
            print(f"Creating {index_name}...", end=" ")
            cursor.execute(sql)
            conn.commit()
            print("Done")
        except sqlite3.OperationalError as e:
            print(f"Already exists or error: {e}")
    
    # Run ANALYZE to help query planner optimize index usage
    print("\nRunning ANALYZE for query planner statistics...", end=" ")
    cursor.execute("ANALYZE")
    conn.commit()
    print("✓ Done")
    
    elapsed = time.time() - start_time
    
    print("-" * 50)
    print(f"Index creation and analysis completed in {elapsed:.2f} seconds")
    
    # Show existing indexes
    print("\nExisting indexes on zaznam_denormalised:")
    cursor.execute("SELECT name FROM sqlite_master WHERE type='index' AND tbl_name='zaznam_denormalised'")
    for row in cursor.fetchall():
        print(f"  - {row[0]}")
    
    conn.close()

if __name__ == "__main__":
    create_indexes()
