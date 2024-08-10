import os
from datetime import datetime
from backend.database import db
from backend.models.user import User
from backend.models.cookinghacks import CookingHacks
from backend.models.cookingtips import CookingTips
from backend.models.images import Image
from backend.models.ingredients import Ingredient
from backend.models.recipes import Recipe
from backend.models.replies import Replies
from backend.models.review import Review
from backend.app import app
from backend.config import config

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

with app.app_context():
    db.drop_all()
    db.create_all()

    users = [User(id=1), User(id=2), User(id=3), User(id=4), User(id=5)]
    db.session.add_all(users)
    db.session.commit()

    reviews = [Review(id=1), Review(id=2), Review(id=3), Review(id=4)]
    db.session.add_all(reviews)
    db.session.commit()
    
    recipes = [
        Recipe(
            user_id=1,
            title='Pilau',
            description='A classic Kenyan dish made with rice.',
            instructions='1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.',
            country='Kenya',
            prep_time=15,
            cook_time=20,
            servings=4,
            diet='Vegetarian',
            banner_image='http://example.com/spaghetti.jpg',
            skill_level='Medium',
            created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')  
        ),
        Recipe(
            user_id=2,
            title='Chicken Curry',
            description='A spicy and flavorful chicken curry with coconut milk and aromatic spices.',
            instructions='1. Cook chicken with spices. 2. Add coconut milk and simmer. 3. Serve with rice.',
            country='India',
            prep_time=20,
            cook_time=40,
            servings=4,
            diet='Non-Vegetarian',
            banner_image='http://example.com/curry.jpg',
            skill_level='Hard',
            created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')  
        ),
    ]
    db.session.add_all(recipes)
    db.session.commit()

    cooking_hacks = [
        CookingHacks(content='To prevent pasta from sticking, add a little oil to the water.'),
        CookingHacks(content='To keep herbs fresh, store them in a jar with a bit of water and cover with a plastic bag.'),
    ]
    db.session.add_all(cooking_hacks)
    db.session.commit()
    print("Cooking hacks seeded successfully.")

    cooking_tips = [
        CookingTips(
            title='How to cook perfect rice',
            content='Rinse rice before cooking. Use a 1:2 rice-to-water ratio.',
            created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S'),  
            updated_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')  
        ),
        CookingTips(
            title='Tips for baking bread',
            content='Use room temperature ingredients. Don\'t overmix the dough.',
            created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S'),  
            updated_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')  
        ),
    ]
    db.session.add_all(cooking_tips)
    db.session.commit()
    print("Cooking tips seeded successfully.")

    images = [
        Image(recipe_id=1, image_url='http://example.com/spaghetti1.jpg'),
        Image(recipe_id=1, image_url='http://example.com/spaghetti2.jpg'),
        Image(recipe_id=2, image_url='http://example.com/curry1.jpg'),
        Image(recipe_id=2, image_url='http://example.com/curry2.jpg'),
    ]
    db.session.add_all(images)
    db.session.commit()
    print("Images seeded successfully.")

    ingredients = [
        Ingredient(recipe_id=1, name='Spaghetti', image='http://example.com/spaghetti.jpg'),
        Ingredient(recipe_id=1, name='Pancetta', image='http://example.com/pancetta.jpg'),
        Ingredient(recipe_id=2, name='Chicken', image='http://example.com/chicken.jpg'),
        Ingredient(recipe_id=2, name='Coconut Milk', image='http://example.com/coconut_milk.jpg'),
    ]
    db.session.add_all(ingredients)
    db.session.commit()
    print("Ingredients seeded successfully.")

    replies = [
        Replies(review_id=1, reply='Thanks for your review! We\'re glad you enjoyed the recipe.'),
        Replies(review_id=2, reply='We\'re sorry to hear that. We will work on improving it.'),
    ]
    db.session.add_all(replies)
    db.session.commit()
    print("Replies seeded successfully.")
