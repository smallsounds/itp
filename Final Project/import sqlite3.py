import sqlite3
import os

def query_new_foods_for_safe_food(safe_food_name, database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT n.FOODNAME, n.FOODTEXTURE, n.FOODTASTE, n.FOODFUNCTION
        FROM SAFE s
        JOIN NEW n ON s.FOODTEXTURE = n.FOODTEXTURE AND s.FOODFUNCTION = n.FOODFUNCTION
        WHERE s.FOODNAME = ?
    ''', (safe_food_name,))
    
    results = cursor.fetchall()

    conn.close()

    return results

safe_food_name = input("Enter the safe food name: ")

current_directory = os.path.dirname(os.path.abspath(__file__))
database_path = os.path.join(current_directory, 'fooddatabase.db')

new_foods = query_new_foods_for_safe_food(safe_food_name, database_path)

if new_foods:
    print("New foods with similar characteristics:")
    for food in new_foods:
        print(food)
else:
    print("No new foods found with similar characteristics to", safe_food_name)
