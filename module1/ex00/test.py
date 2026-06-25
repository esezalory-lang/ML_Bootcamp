from book import Book
from recipe import Recipe
import datetime

if __name__ == "__main__":
    tourte = Recipe("Tourte", 4, 50,
                    ["eggs", "plums", "milk", "flour", "vanilla"],
                    "Great recipe to eat for dessert",
                    "dessert")
    bolognese = Recipe("Bolognese", 1, 15,
                       ["pasta", "tomatoes", "parmesan", "groundbeef"],
                       "quick meal to do for students",
                       "lunch")
    pea_soup = Recipe("Pea soup", 2, 30,
                      ["peas", "cream", "butter", "salt"],
                      "warm starter for if you are cold",
                      "starter")

    chicken_soup = Recipe("Chicken soup", 3, 40,
                          ["chicken", "noodles", "celeri", "carrots"],
                          "perfect starter for kids who dont want to eat soup",
                          "starter")

    starter = [pea_soup, chicken_soup]
    lunches = [bolognese]
    dessert = []
    recipe_list = {"starter": starter, "lunch": lunches, "dessert": dessert}
    cookbook = Book("Elliots Cookbook",
                    datetime.datetime.now(),
                    datetime.datetime(2025, 6, 23),
                    recipe_list)
    recipe_name = cookbook.get_recipe_by_name("Chicken soup")
    all_recipes = cookbook.get_recipes_by_types("lunch")
    cookbook.add_recipe(tourte)
    for i in dessert:
        print(i)

    print("Attributes:")
    print(tourte.__dict__)