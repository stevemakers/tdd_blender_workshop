from openai import OpenAI
import json


"""
1 A blender should have the ability to create smoothies from food
2 Smoothies should store information about macronutrients and calories
"""

class Blender():
    def __init__(self):
        self.ingredients = []
        self.capacity = 10000
        
    """
 
    """
    def add_ingredients(self, ingredients):
        if not isinstance(ingredients, list):
            raise ValueError("Ingredients is not a list")

        for ingredient in ingredients:
            self.ingredients.append(ingredient)

    """
    Blends all the ingredients that have been passed into the blender
    Returns a Smoothie with the combined macronutrients
    """
    def blend_ingredients(self):
        # total_grams = sum([ingredient.grams for ingredient in self.ingredients])
        # if total_grams > self.capacity:
        #     raise ValueError("Exceeded blender capacity")
        
        foodAPI = FoodAPI()
        ingredient_macros = foodAPI.get_macros(self.ingredients)

        print("ingredient_macros =>", ingredient_macros)

        return Smoothie(ingredient_macros)


    """
    Prints the values of the ingredients
    [Ingredient(50, 'oats'), Ingredient(100, 'blueberries'), Ingredient(25, "Protein Powder")]
    e.g. 50 grams of oats + 100 grams of blueberries + 25 grams of Protein Powder
    """
    def print_ingredients(self):
        string = ""
        for index, ingredient in enumerate(self.ingredients):
            if index is len(self.ingredients) - 1:
                string += f'{ingredient.get_key_info()}'
            else:
                string += f'{ingredient.get_key_info()} + '
                

        return string

class Ingredient():
    def __init__(self, grams, name):
        self.grams = grams
        self.name = name
    
    """
    Prints the key information about the ingredients
    e.g. 50g oats
    """
    def get_key_info(self):
        return f'{self.grams}g {self.name}'


class Smoothie():
    def __init__(self, macros):
        self.macros = macros

class FoodAPI():
    def __init__(self):
        self.client = OpenAI(
            api_key=""
        )

    '''
    Takes in an array of ingredients where the 1st index of the ingredient is the grams, 2nd is the name of the ingredient
    e.g. [[50, 'oats'], [100, 'blueberries']]

    Returns the combined macronutrient profile as a dictionary
    e.g {
          "calories": 389,
          "carbohydrates": 66.3,
          "protein": 16.9,
          "fat": 6.9,
        }
    '''
    def get_macros(self, ingredients):
        macros = self.get_macro_string(ingredients)
        print("WE ACTUALLY GOT THE MACROS")
        chat_completion = self.client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f'Return a single json-like object of the combined macros (carbs, protein, fats, calories) of the following ingredients. {macros}, ensure the output can be used by json.load() to output a python dict'
                }
            ],
            model="gpt-3.5-turbo",
        )

        message = chat_completion.choices[0].message.content
        json_acceptable_string = message.replace("'", "\"")
        return json.loads(json_acceptable_string)


    '''
    Takes in an array of ingredients where the 1st index of the ingredient is the grams, 2nd is the name of the ingredient
    e.g. [[50, 'oats'], [100, 'blueberries']]

    Returns a string that combines these for GPT 
    e.g 50g oats + 100g blueberries
    '''
    def get_macro_string(self, ingredients):
        string = ""
        for index, ingredient in enumerate(ingredients):
            grams = ingredient.grams
            name = ingredient.name

            if index is not len(ingredients) - 1:
                string += f'{grams}g {name} + '
            else:
                string += f'{grams}g {name}'

        return string
    

# blender = Blender()
# blender.add_ingredients([(50, "oats"), (100, "Nutella"), (55, "Bourbon")])

# smoothie = blender.blend_ingredients()
# print(smoothie)
# print(smoothie.macros)