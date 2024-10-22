# Learning Journal

## Date: 10/01/2024

- **What I learned today**:

  - How to define and store recipes using Python dictionaries.
  - How to combine multiple recipes into a list.
  - How to save data to a JSON file using Python.
  - How to run Python scripts from the command prompt.

- **Challenges faced**:

  - Understanding the correct way to run Python scripts from the command prompt.
  - Ensuring the JSON file is correctly formatted and saved.

- **How I overcame them**:
  - Clarified the distinction between running commands in the Python interactive shell and the command prompt.
  - Used Python's `json` module to serialize and save data to a JSON file.

## Date: 10/6/2024

## Operators & Functions In Python

- **What I learned today**:

  - How to create a more complex Python script that handles multiple recipes and ingredients.
  - Implementing a function (take_recipe()) to collect user input for recipes.
  - Using nested loops to process recipes and ingredients.
  - Implementing logic to determine recipe difficulty based on cooking time and number of ingredients.
  - How to create and update a list of unique ingredients across multiple recipes.
  - Sorting and displaying a list of ingredients alphabetically with numbering.

- **Challenges faced**:

  - Structuring a more complex script with multiple functionalities.
  - Implementing the logic to determine recipe difficulty based on multiple criteria.
  - Ensuring that ingredients are not duplicated in the ingredients list.
  - Sorting and displaying the ingredients list in a specific format.

- **How I overcame them**:

  - Broke down the problem into smaller, manageable steps and implemented them one at a time.
  - Used conditional statements (if-elif-else) to implement the difficulty determination logic.
  - Utilized the 'in' operator to check for ingredient existence before adding to the list.
  - Used Python's built-in sorted() function and enumerate() to sort and number the ingredients list.

- **New skills acquired**:

  - Creating more complex, multi-function Python scripts.
  - Handling and processing user input for multiple items.
  - Working with nested data structures (lists of dictionaries).
  - Implementing custom logic for data classification (recipe difficulty).
  - Sorting and formatting output for better readability.

  ## Date: 10/06/2024

### What I learned today:

### File Handling In Python

1. Creating and working with binary files using Python's pickle module:

   - Saving complex data structures (dictionaries, lists) to binary files
   - Loading data from binary files

2. Implementing more complex Python scripts with multiple functions:

   - Creating a recipe input system (recipe_input.py)
   - Developing a recipe search system (recipe_search.py)

3. Handling user input and output in a more interactive way:

   - Taking multiple inputs for recipes (name, cooking time, ingredients)
   - Displaying formatted recipe information

4. Working with nested data structures:

   - Using dictionaries to store recipe information
   - Managing lists of dictionaries for multiple recipes

5. Implementing search functionality:

   - Searching through a list of dictionaries based on specific criteria

6. Error handling and input validation:

   - Using try-except blocks to handle potential errors (e.g., file not found, invalid input)

7. File operations in Python:
   - Opening files in binary write and read modes
   - Using the 'with' statement for proper file handling

### Challenges faced:

1. Understanding the structure of pickle files and how to properly save and load data
2. Implementing a user-friendly interface for inputting and searching recipes
3. Managing the complexity of nested data structures (lists of dictionaries)
4. Ensuring proper error handling for various scenarios (file not found, invalid user input)

### How I overcame these challenges:

1. Carefully studied the pickle module documentation and examples
2. Broke down the problem into smaller, manageable functions
3. Used print statements to debug and understand the flow of data
4. Implemented try-except blocks to gracefully handle potential errors

### New skills acquired:

1. Working with binary files using pickle
2. Creating more complex, interactive command-line applications
3. Implementing search functionality in Python
4. Better understanding of nested data structures and how to manipulate them

## Date: 10/06/2024

### Object-Oriented Programming in Python: Recipe Management System

#### What I learned today:

1. Class Definition and Object Creation:

   - Defined a Recipe class with attributes like name, ingredients, cooking time, and difficulty.
   - Created multiple recipe objects (Pasta Carbonara, Simple Salad, Banana Smoothie, Cake).

2. Encapsulation:

   - Used private attributes and public methods to access and modify recipe data.
   - Implemented getter and setter methods for name and cooking time.

3. Methods Implementation:

   - Created methods like add_ingredients(), calculate_difficulty(), and search_ingredient().
   - Implemented a special method **str**() for string representation of recipes.

4. Class Variables:

   - Used a class variable all_ingredients to keep track of all unique ingredients across recipes.

5. Method Overloading:

   - Implemented add_ingredients() method to accept variable number of arguments.

6. Abstraction:

   - Created methods like calculate_difficulty() to hide complex logic from the user.

7. Search Functionality:
   - Implemented a recipe_search() function to search recipes based on ingredients.

#### Challenges faced:

1. Designing the class structure to efficiently represent recipes.
2. Implementing the logic for calculating recipe difficulty.
3. Ensuring that the all_ingredients list stays updated and avoids duplicates.

#### How I overcame these challenges:

1. Carefully planned the Recipe class attributes and methods before implementation.
2. Used conditional statements to implement the difficulty calculation logic.
3. Implemented a case-insensitive check for ingredients to avoid duplicates in all_ingredients.

#### New skills acquired:

1. Creating and working with classes and objects in Python.
2. Implementing various OOP concepts like encapsulation and abstraction.
3. Using class variables to store data shared across all instances.
4. Implementing search functionality within a collection of objects.

Date: 10/22/2024

What I've Learned:

- Successfully implemented a complete Recipe Management System using Python and MySQL
- Mastered CRUD operations (Create, Read, Update, Delete) in a MySQL database
- Learned to handle database connections and cursors effectively
- Implemented robust error handling for database operations
- Created a user-friendly command-line interface

Technical Concepts Mastered:

1. Database Connection:

   - Established MySQL connection using mysql.connector
   - Created database and tables programmatically
   - Managed connection states and proper closure

2. Data Management:

   - Structured SQL queries for CRUD operations
   - Handled data validation and type conversion
   - Implemented dynamic difficulty calculation based on recipe attributes

3. User Interface:
   - Created an intuitive menu-driven interface
   - Implemented input validation for all user interactions
   - Provided clear feedback for all operations

Challenges Faced:

1. Managing database connections and error handling
2. Implementing proper data validation for user inputs
3. Handling ingredient lists and string formatting
4. Ensuring proper transaction management with commits

Solutions Implemented:

1. Used try-except blocks for robust error handling
2. Implemented input validation loops
3. Used string manipulation for ingredient management
4. Added proper commit statements after database operations
