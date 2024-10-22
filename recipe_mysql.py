import mysql.connector

def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty

def create_recipe(conn, cursor):
    name = input("\nEnter the recipe name: ")
    
    while True:
        try:
            cooking_time = int(input("Enter cooking time (in minutes): "))
            break
        except ValueError:
            print("Please enter a valid number for cooking time.")
    
    ingredients = []
    while True:
        ingredient = input("Enter an ingredient (or press enter to finish): ")
        if ingredient == "":
            if len(ingredients) == 0:
                print("Please enter at least one ingredient.")
                continue
            break
        ingredients.append(ingredient)
    
    difficulty = calculate_difficulty(cooking_time, ingredients)
    ingredients_str = ", ".join(ingredients)
    
    query = """INSERT INTO Recipes 
            (name, ingredients, cooking_time, difficulty) 
            VALUES (%s, %s, %s, %s)"""
    values = (name, ingredients_str, cooking_time, difficulty)
    
    cursor.execute(query, values)
    conn.commit()
    print("\nRecipe has been created successfully!")

def search_recipe(conn, cursor):
    cursor.execute("SELECT ingredients FROM Recipes")
    results = cursor.fetchall()
    
    all_ingredients = []
    for recipe_ingredients in results:
        ingredients_list = recipe_ingredients[0].split(", ")
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    print("\nAvailable ingredients:")
    for i, ingredient in enumerate(all_ingredients, 1):
        print(f"{i}. {ingredient}")
    
    while True:
        try:
            choice = int(input("\nEnter the number of the ingredient you want to search for: "))
            if 1 <= choice <= len(all_ingredients):
                search_ingredient = all_ingredients[choice - 1]
                break
            else:
                print("Please enter a valid number from the list.")
        except ValueError:
            print("Please enter a valid number.")
    
    search_pattern = f"%{search_ingredient}%"
    cursor.execute("""
        SELECT name, ingredients, cooking_time, difficulty 
        FROM Recipes 
        WHERE ingredients LIKE %s
    """, (search_pattern,))
    
    recipes = cursor.fetchall()
    
    if recipes:
        print(f"\nRecipes containing {search_ingredient}:")
        for recipe in recipes:
            print(f"\nName: {recipe[0]}")
            print(f"Ingredients: {recipe[1]}")
            print(f"Cooking Time: {recipe[2]} minutes")
            print(f"Difficulty: {recipe[3]}")
    else:
        print(f"\nNo recipes found containing {search_ingredient}")

def update_recipe(conn, cursor):
    cursor.execute("SELECT id, name, ingredients, cooking_time, difficulty FROM Recipes")
    results = cursor.fetchall()
    
    if not results:
        print("\nNo recipes found in the database.")
        return
    
    print("\nAvailable recipes:")
    for recipe in results:
        print(f"\nID: {recipe[0]}")
        print(f"Name: {recipe[1]}")
        print(f"Ingredients: {recipe[2]}")
        print(f"Cooking Time: {recipe[3]} minutes")
        print(f"Difficulty: {recipe[4]}")
    
    while True:
        try:
            recipe_id = int(input("\nEnter the ID of the recipe you want to update: "))
            cursor.execute("SELECT * FROM Recipes WHERE id = %s", (recipe_id,))
            recipe = cursor.fetchone()
            if recipe:
                break
            else:
                print("Recipe not found. Please enter a valid ID.")
        except ValueError:
            print("Please enter a valid number.")
    
    print("\nWhich field would you like to update?")
    print("1. Name")
    print("2. Cooking Time")
    print("3. Ingredients")
    
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please try again.")
    
    if choice == '1':
        new_value = input("Enter the new name: ")
        cursor.execute("UPDATE Recipes SET name = %s WHERE id = %s", 
                      (new_value, recipe_id))
    
    elif choice == '2':
        while True:
            try:
                new_value = int(input("Enter the new cooking time (in minutes): "))
                break
            except ValueError:
                print("Please enter a valid number.")
        
        cursor.execute("UPDATE Recipes SET cooking_time = %s WHERE id = %s", 
                      (new_value, recipe_id))
        
        cursor.execute("SELECT ingredients FROM Recipes WHERE id = %s", (recipe_id,))
        ingredients = cursor.fetchone()[0].split(", ")
        new_difficulty = calculate_difficulty(new_value, ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", 
                      (new_difficulty, recipe_id))
    
    elif choice == '3':
        ingredients = []
        while True:
            ingredient = input("Enter an ingredient (or press enter to finish): ")
            if ingredient == "":
                if len(ingredients) == 0:
                    print("Please enter at least one ingredient.")
                    continue
                break
            ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        cursor.execute("UPDATE Recipes SET ingredients = %s WHERE id = %s", 
                      (ingredients_str, recipe_id))
        
        cursor.execute("SELECT cooking_time FROM Recipes WHERE id = %s", (recipe_id,))
        cooking_time = cursor.fetchone()[0]
        new_difficulty = calculate_difficulty(cooking_time, ingredients)
        cursor.execute("UPDATE Recipes SET difficulty = %s WHERE id = %s", 
                      (new_difficulty, recipe_id))
    
    conn.commit()
    print("\nRecipe updated successfully!")

def delete_recipe(conn, cursor):
    print("Delete Recipe functionality to be implemented.")

def main_menu(conn, cursor):
    while True:
        print("\n===== Recipe Management System =====")
        print("1. Create a new recipe")
        print("2. Search for a recipe by ingredient")
        print("3. Update an existing recipe")
        print("4. Delete a recipe")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            create_recipe(conn, cursor)
        elif choice == '2':
            search_recipe(conn, cursor)
        elif choice == '3':
            update_recipe(conn, cursor)
        elif choice == '4':
            delete_recipe(conn, cursor)
        elif choice == '5':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")
    
    conn.commit()
    conn.close()
    print("Changes committed and connection closed.")

if __name__ == "__main__":
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="cf-python",
            password="cf-python"
        )
        
        cursor = conn.cursor()
        
        cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
        cursor.execute("USE task_database")
        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS Recipes (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(50),
            ingredients VARCHAR(255),
            cooking_time INT,
            difficulty VARCHAR(20)
        )
        """)

        print("Database and table created successfully.")
        
        main_menu(conn, cursor)

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
            print("MySQL connection is closed")
