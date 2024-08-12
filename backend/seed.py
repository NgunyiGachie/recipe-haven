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
from backend.models.bookmark import Bookmark
from backend.models.news import News
from backend.models.rating import Rating  
from backend.app import app
from backend.config import config
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

config_name = os.getenv('FLASK_CONFIG', 'default')
app.config.from_object(config[config_name])

with app.app_context():
    db.drop_all()
    db.create_all()

    # Seed users
    users = [
        User(username='user1', first_name='Anthony', last_name='Gachie', email='user1@example.com', country='Kenya'),
        User(username='user2', first_name='Ben', last_name='Gitau', email='user2@example.com', country='Uganda'),
        User(username='user3', first_name='Audrey', last_name='Cherop', email='user3@example.com', country='Congo'),
        User(username='user4', first_name='Bryan', last_name='Odongo', email='user4@example.com', country='Tanzania'),
        User(username='user5', first_name='Brian', last_name='Kipkirui', email='user5@example.com', country='Rwanda'),
    ]
    
    for user, password in zip(users, ['password1', 'password2', 'password3', 'password4', 'password5']):
        user.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
  
    db.session.add_all(users)
    db.session.commit()

    # Seed recipes
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

    # Seed reviews
    reviews = [
        Review(user_id=1, recipe_id=1, review='Great recipe!', created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')),
        Review(user_id=2, recipe_id=1, review='Tasty, but could use more spices.', created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')),
        Review(user_id=3, recipe_id=2, review='Delicious and easy to make!', created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')),
        Review(user_id=4, recipe_id=2, review='Too spicy for my taste.', created_at=datetime.strptime('2024-08-07T00:00:00', '%Y-%m-%dT%H:%M:%S')),
    ]
    db.session.add_all(reviews)
    db.session.commit()

    # Seed images
    images = [
        Image(recipe_id=1, image_url='http://example.com/spaghetti1.jpg'),
        Image(recipe_id=1, image_url='http://example.com/spaghetti2.jpg'),
        Image(recipe_id=2, image_url='http://example.com/curry1.jpg'),
        Image(recipe_id=2, image_url='http://example.com/curry2.jpg'),
    ]
    db.session.add_all(images)
    db.session.commit()

    # Seed ingredients
    ingredients = [
        Ingredient(recipe_id=1, name='Spaghetti', image='http://example.com/spaghetti.jpg'),
        Ingredient(recipe_id=1, name='Pancetta', image='http://example.com/pancetta.jpg'),
        Ingredient(recipe_id=2, name='Chicken', image='http://example.com/chicken.jpg'),
        Ingredient(recipe_id=2, name='Coconut Milk', image='http://example.com/coconut_milk.jpg'),
    ]
    db.session.add_all(ingredients)
    db.session.commit()

    # Seed replies
    replies = [
        Replies(review_id=1, reply='Thanks for your review! We\'re glad you enjoyed the recipe.'),
        Replies(review_id=2, reply='We\'re sorry to hear that. We will work on improving it.'),
    ]
    db.session.add_all(replies)
    db.session.commit()

    # Seed bookmarks
    bookmarks = [
        Bookmark(user_id=1, recipe_id=1),
        Bookmark(user_id=2, recipe_id=2),
    ]
    db.session.add_all(bookmarks)
    db.session.commit()

    # Seed cooking hacks
    cooking_hacks = [
        CookingHacks(content='To prevent pasta from sticking, add a little oil to the water.'),
        CookingHacks(content='To keep herbs fresh, store them in a jar with a bit of water and cover with a plastic bag.'),
    ]
    db.session.add_all(cooking_hacks)
    db.session.commit()

    # Seed cooking tips
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

    # Seed news
    news_items = [
        News(image_url='http://example.com/news1.jpg', content='Breaking: New recipe trends for 2024!', link='http://example.com/news1'),
        News(image_url='http://example.com/news2.jpg', content='Top 10 kitchen gadgets you need to try.', link='http://example.com/news2'),
    ]
    db.session.add_all(news_items)
    db.session.commit()

    # Seed ratings
    ratings = [
        Rating(user_id=1, recipe_id=1, rating=4),
        Rating(user_id=2, recipe_id=1, rating=3),
        Rating(user_id=3, recipe_id=2, rating=5),
        Rating(user_id=4, recipe_id=2, rating=2),
    ]
    db.session.add_all(ratings)
    db.session.commit()
