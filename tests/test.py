from lib.blender import Blender, Food

def test_initialise_blender_class():
    blender = Blender()
    assert isinstance(blender, Blender) == True
    assert blender.ingredients == []

def test_blender_adds_ingredients():
    blender = Blender()
    blender.add_ingredients("Apple")
    assert blender.ingredients == ["Apple"]

def test_blender_blends_ingredients():
    # Arrange
    blender = Blender()
    peanut_butter = {
        "calories": 188,
        "carbohydrates": 6.9,
        "protein": 8,
        "fat": 16,
    }
    apple = {
        "calories": 95,
        "carbohydrates": 25,
        "protein": 0.5,
        "fat": 0.3,
    }

    # Act
    blender.add_ingredients(apple)
    blender.add_ingredients(peanut_butter)
    smoothie = blender.blend_ingredients()
   
    # Assertions
    assert smoothie == {
        "calories": 283,
        "carbohydrates": 31.9,
        "protein": 8.5,
        "fat": 16.3
    }

def test_initialise_food_class():
    food = Food(None)
    assert isinstance(food, Food) == True
    assert food.macros == None