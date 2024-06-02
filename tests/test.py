from lib.blender import Blender, Smoothie

def test_initialise_blender_class():
    blender = Blender()
    assert isinstance(blender, Blender) == True
    assert blender.ingredients == []

def test_blender_adds_one_ingredient():
    blender = Blender()

    oats = {
        "calories": 389,
        "carbohydrates": 66.3,
        "protein": 16.9,
        "fat": 6.9,
    }
    blender.add_ingredients([(50, oats)])
    assert blender.ingredients[0] == {
        "calories": 194.5,
        "carbohydrates": 33.15,
        "protein": 8.45,
        "fat": 3.45,
        "carbohydrates": 33.15,
    }
    
def test_blender_adds_multiple_ingredients():
    blender = Blender()
    oats = {
        "calories": 389,
        "carbohydrates": 66.3,
        "protein": 16.9,
        "fat": 6.9,
    }

    apple = {
        "calories": 95,
        "carbohydrates": 25,
        "protein": 0.5,
        "fat": 0.3,
    }
    blender.add_ingredients([
        (150, apple),
        (50, oats)
    ])

    assert blender.ingredients[1] == {
        "calories": 194.5,
        "carbohydrates": 33.15,
        "protein": 8.45,
        "fat": 3.45,
    }

def test_blender_blends_ingredients():
    # Arrange
    blender = Blender()
    oats = {
        "calories": 389,
        "carbohydrates": 66.3,
        "protein": 16.9,
        "fat": 6.9,
    }

    apple = {
        "calories": 95,
        "carbohydrates": 25,
        "protein": 0.5,
        "fat": 0.3,
    }

    # Act
    blender.add_ingredients([
        (150, apple),
        (50, oats)
    ])
    smoothie = blender.blend_ingredients()

    assert smoothie.macros == {
        "calories": 337.0,
        "carbohydrates": 70.65,
        "protein": 9.2,
        "fat": 3.9000000000000004
    }

def test_initialise_smoothie_class():
    smoothie = Smoothie(None)
    assert isinstance(smoothie, Smoothie) == True
    assert smoothie.macros == None

def test_smoothie_returns_healthy_successfully():
    health_pack = {
        "calories": 299,
        "carbohydrates": 49,
        "protein": 20,
        "fat": 15,
    }
    smoothie = Smoothie(health_pack)
    health_rating = smoothie.categorize()
    assert health_rating == "Healthy"

def test_smoothie_returns_normal_successfully():
    normal_pack = {
        "calories": 400,
        "carbohydrates": 80,
        "protein": 19,
        "fat": 10,
    }
    smoothie = Smoothie(normal_pack)
    health_rating = smoothie.categorize()
    assert health_rating == "Normal"

def test_smoothie_returns_unhealthy_successfully():
    unhealthy_pack = {
        "calories": 601,
        "carbohydrates": 181,
        "protein": 3,
        "fat": 100,
    }
    smoothie = Smoothie(unhealthy_pack)
    health_rating = smoothie.categorize()
    assert health_rating == "Unhealthy"
