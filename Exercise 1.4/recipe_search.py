import pickle

def display_recipe(recipe):
    print(f"\nRecipe: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print(f"Ingredients: {', '.join(recipe['ingredients'])}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    print("\nAvailable ingredients:")
    for index, ingredient in enumerate(data['all_ingredients'], 1):
        print(f"{index}. {ingredient}")

    try:
        choice = int(input("\nEnter the number of the ingredient you want to search for: "))
        ingredient_searched = data['all_ingredients'][choice - 1]
        print(f"\nRecipes containing {ingredient_searched}:")
        for recipe in data['recipes_list']:
            if ingredient_searched in recipe['ingredients']:
                display_recipe(recipe)
    except (ValueError, IndexError):
        print("Invalid input. Please enter a number from the list.")
    else:
        if not any(ingredient_searched in recipe['ingredients'] for recipe in data['recipes_list']):
            print("No recipes found with this ingredient.")

# Main code
filename = input("Enter the filename containing your recipe data: ")

try:
    with open(filename, 'rb') as file:
        data = pickle.load(file)
except FileNotFoundError:
    print(f"File '{filename}' not found. Please make sure the file exists.")
else:
    search_ingredient(data)
