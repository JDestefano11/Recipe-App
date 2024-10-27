# Import necessary packages
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Database credentials
username = 'cf-python'  
password = 'cf-python'  
hostname = 'localhost'      
database_name = 'recipe'  

# Create an engine object
engine = create_engine(f'mysql+mysqlconnector://{username}:{password}@{hostname}/{database_name}')

# Create Base class
Base = declarative_base()

# Define Recipe class
class Recipe(Base):
    __tablename__ = 'final_recipes'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))
    
    def __repr__(self):
        return f"Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})"
    
    def __str__(self):
        return f"\n{'-'*50}\n" \
               f"\tRecipe: {self.name}\n" \
               f"\tCooking Time: {self.cooking_time} minutes\n" \
               f"\tDifficulty: {self.difficulty}\n" \
               f"\tIngredients: {self.ingredients}\n" \
               f"{'-'*50}\n"
    
    def calculate_difficulty(self):
        ingredients_list = self.return_ingredients_as_list()
        if self.cooking_time < 10 and len(ingredients_list) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(ingredients_list) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients_list) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients_list) >= 4:
            self.difficulty = "Hard"
    
    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return self.ingredients.split(', ')

def create_recipe():
    name = input("\nEnter the recipe name: ")
    if len(name) > 50:
        print("Name must be under 50 characters!")
        return None
    
    cooking_time = input("Enter cooking time (in minutes): ")
    if not cooking_time.isnumeric():
        print("Cooking time must be a number!")
        return None
    cooking_time = int(cooking_time)
    
    ingredients_num = input("How many ingredients would you like to enter? ")
    if not ingredients_num.isnumeric():
        print("Number of ingredients must be a number!")
        return None
    
    ingredients = []
    for i in range(int(ingredients_num)):
        ingredient = input(f"Enter ingredient {i+1}: ")
        if not ingredient.replace(' ', '').isalpha():
            print("Ingredients must contain only letters!")
            return None
        ingredients.append(ingredient)
    
    ingredients_str = ", ".join(ingredients)
    if len(ingredients_str) > 255:
        print("Total ingredients string too long!")
        return None
    
    recipe_entry = Recipe(
        name=name,
        cooking_time=cooking_time,
        ingredients=ingredients_str
    )
    recipe_entry.calculate_difficulty()
    
    session.add(recipe_entry)
    session.commit()
    print("\nRecipe has been created successfully!")

def view_all_recipes():
    recipes = session.query(Recipe).all()
    if not recipes:
        print("\nNo recipes found in the database.")
        return None
    
    print("\nAll Recipes:")
    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
    
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    
    for result in results:
        ingredients_list = result[0].split(', ')
        for ingredient in ingredients_list:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)
    
    print("\nAvailable ingredients:")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(f"{index}. {ingredient}")
    
    search_input = input("\nEnter the numbers of ingredients to search for (separated by spaces): ")
    search_numbers = search_input.split()
    
    try:
        search_numbers = [int(num) for num in search_numbers]
    except ValueError:
        print("Please enter valid numbers!")
        return None
    
    if not all(1 <= num <= len(all_ingredients) for num in search_numbers):
        print("Please enter valid ingredient numbers!")
        return None
    
    search_ingredients = [all_ingredients[num-1] for num in search_numbers]
    conditions = []
    
    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))
    
    matching_recipes = session.query(Recipe).filter(*conditions).all()
    
    if matching_recipes:
        print("\nMatching Recipes:")
        for recipe in matching_recipes:
            print(recipe)
    else:
        print("\nNo recipes found with those ingredients.")

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
    
    results = session.query(Recipe.id, Recipe.name).all()
    
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")
    
    recipe_id = input("\nEnter the ID of the recipe you want to edit: ")
    if not recipe_id.isnumeric():
        print("Invalid ID!")
        return None
    
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == int(recipe_id)).first()
    if not recipe_to_edit:
        print("Recipe not found!")
        return None
    
    print("\nWhat would you like to edit?")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")
    
    choice = input("\nEnter your choice (1-3): ")
    if choice not in ['1', '2', '3']:
        print("Invalid choice!")
        return None
    
    if choice == '1':
        new_name = input("\nEnter new name: ")
        if len(new_name) > 50:
            print("Name must be under 50 characters!")
            return None
        recipe_to_edit.name = new_name
        
    elif choice == '2':
        ingredients_num = input("\nHow many ingredients would you like to enter? ")
        if not ingredients_num.isnumeric():
            print("Invalid number!")
            return None
        
        ingredients = []
        for i in range(int(ingredients_num)):
            ingredient = input(f"Enter ingredient {i+1}: ")
            if not ingredient.replace(' ', '').isalpha():
                print("Ingredients must contain only letters!")
                return None
            ingredients.append(ingredient)
        
        ingredients_str = ", ".join(ingredients)
        if len(ingredients_str) > 255:
            print("Total ingredients string too long!")
            return None
        recipe_to_edit.ingredients = ingredients_str
        
    elif choice == '3':
        new_cooking_time = input("\nEnter new cooking time (in minutes): ")
        if not new_cooking_time.isnumeric():
            print("Cooking time must be a number!")
            return None
        recipe_to_edit.cooking_time = int(new_cooking_time)
    
    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("\nRecipe updated successfully!")

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("\nNo recipes found in the database.")
        return None
    
    results = session.query(Recipe.id, Recipe.name).all()
    
    print("\nAvailable recipes:")
    for recipe_id, recipe_name in results:
        print(f"{recipe_id}. {recipe_name}")
    
    recipe_id = input("\nEnter the ID of the recipe you want to delete: ")
    if not recipe_id.isnumeric():
        print("Invalid ID!")
        return None
    
    recipe_to_delete = session.query(Recipe).filter(Recipe.id == int(recipe_id)).first()
    if not recipe_to_delete:
        print("Recipe not found!")
        return None
    
    confirmation = input(f"\nAre you sure you want to delete '{recipe_to_delete.name}'? (yes/no): ")
    if confirmation.lower() == 'yes':
        session.delete(recipe_to_delete)
        session.commit()
        print("\nRecipe deleted successfully!")
    else:
        print("\nDeletion cancelled.")

# Create a Session class
Session = sessionmaker(bind=engine)

# Initialize the session object
session = Session()

# Create all tables
Base.metadata.create_all(engine)


def main_menu():
    choice = ''
    while choice != 'quit':
        print("\nMain Menu")
        print("-" * 50)
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for recipes by ingredients")
        print("4. Edit a recipe")
        print("5. Delete a recipe")
        print("\nType 'quit' to exit the program")
        
        choice = input("\nEnter your choice: ").lower()
        
        if choice == '1':
            create_recipe()
        elif choice == '2':
            view_all_recipes()
        elif choice == '3':
            search_by_ingredients()
        elif choice == '4':
            edit_recipe()
        elif choice == '5':
            delete_recipe()
        elif choice == 'quit':
            print("\nThanks for using the Recipe Manager!")
        else:
            print("\nInvalid choice. Please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()
    session.close()
    engine.dispose()

