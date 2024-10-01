import json

# Define the recipes
recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

recipe_2 = {
    "name": "Pancakes",
    "cooking_time": 20,
    "ingredients": ["Flour", "Milk", "Eggs", "Sugar", "Baking powder"]
}

recipe_3 = {
    "name": "Salad",
    "cooking_time": 10,
    "ingredients": ["Lettuce", "Tomato", "Cucumber", "Olive oil", "Salt"]
}

recipe_4 = {
    "name": "Grilled Cheese Sandwich",
    "cooking_time": 15,
    "ingredients": ["Bread", "Cheese", "Butter"]
}

recipe_5 = {
    "name": "Omelette",
    "cooking_time": 10,
    "ingredients": ["Eggs", "Salt", "Pepper", "Butter"]
}

# Combine all recipes into a list
all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

# Print all recipes
print(all_recipes)

# Save recipes to a JSON file
with open('recipes.json', 'w') as file:
    json.dump(all_recipes, file, indent=4)
