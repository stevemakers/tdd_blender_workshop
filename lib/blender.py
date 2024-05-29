"""
1 A blender should have the ability to create smoothies from food
2 Smoothies should store information about macronutrients and calories
"""

class Blender():
    def __init__(self):
        self.ingredients = []

    def add_ingredients(self, ingredient):
        self.ingredients.append(ingredient)

    def blend_ingredients(self):
        smoothie = {
            "calories": 0,
            "carbohydrates": 0,
            "protein": 0,
            "fat": 0
        }

        for ingredient in self.ingredients:
            macros = ingredient.keys()

            for macro in macros:
                smoothie[macro] += ingredient[macro]

        return smoothie

class Food():
    def __init__(self, macros):
        self.macros = macros

# Inputs and outputs -- Blender outputs