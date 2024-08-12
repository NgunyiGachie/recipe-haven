# API Documentation

## Overview
This API allows users to manage recipes, ingredients, cooking hacks, cooking tips, images, and replies.

## Endpoints

### Recipes

#### GET /recipes
- **Description**: Retrieve a list of all recipes.
- **Response**:
    ```json
   [
        {
        "Images": [
        {
        "id": 1,
        "image_url": "http://example.com/spaghetti1.jpg",
        "recipe_id": 1
        },
        {
        "id": 2,
        "image_url": "http://example.com/spaghetti2.jpg",
        "recipe_id": 1
        }
        ],
        "banner_image": "http://example.com/spaghetti.jpg",
        "cook_time": 20,
        "country": "Kenya",
        "created_at": "2024-08-07T00:00:00",
        "description": "A classic Kenyan dish made with rice.",
        "diet": "Vegetarian",
        "id": 1,
        "ingredients": [
        {
        "id": 1,
        "image": "http://example.com/spaghetti.jpg",
        "name": "Spaghetti",
        "recipe_id": 1
        },
        {
        "id": 2,
        "image": "http://example.com/pancetta.jpg",
        "name": "Pancetta",
        "recipe_id": 1
        }
        ],
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Pilau",
        "user_id": 1
        },
        {
        "Images": [
        {
        "id": 3,
        "image_url": "http://example.com/curry1.jpg",
        "recipe_id": 2
        },
        {
        "id": 4,
        "image_url": "http://example.com/curry2.jpg",
        "recipe_id": 2
        }
        ],
        "banner_image": "http://example.com/curry.jpg",
        "cook_time": 40,
        "country": "India",
        "created_at": "2024-08-07T00:00:00",
        "description": "A spicy and flavorful chicken curry with coconut milk and aromatic spices.",
        "diet": "Non-Vegetarian",
        "id": 2,
        "ingredients": [
        {
        "id": 3,
        "image": "http://example.com/chicken.jpg",
        "name": "Chicken",
        "recipe_id": 2
        },
        {
        "id": 4,
        "image": "http://example.com/coconut_milk.jpg",
        "name": "Coconut Milk",
        "recipe_id": 2
        }
        ],
        "instructions": "1. Cook chicken with spices. 2. Add coconut milk and simmer. 3. Serve with rice.",
        "prep_time": 20,
        "servings": 4,
        "skill_level": "Hard",
        "title": "Chicken Curry",
        "user_id": 2
        },
        {
        "Images": [],
        "banner_image": "http://example.com/spaghetti.jpg",
        "cook_time": 30,
        "country": "Italy",
        "created_at": "2024-07-10T12:00:00",
        "description": "Classic italian meal made of",
        "diet": "Vegetarian",
        "id": 3,
        "ingredients": [],
        "instructions": "Cook pasta. Make Sauce",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Spaghetti ",
        "user_id": 1
        },
        {
        "Images": [
        {
        "id": 5,
        "image_url": "http://example.com/image1.jpg",
        "recipe_id": 4
        }
        ],
        "banner_image": "http://example.com/spaghetti.jpg",
        "cook_time": 30,
        "country": "Italy",
        "created_at": "2024-07-10T12:00:00",
        "description": "Classic italian meal made of",
        "diet": "Vegetarian",
        "id": 4,
        "ingredients": [
        {
        "id": 5,
        "image": "http://example.com/flour.jpg",
        "name": "Flour",
        "recipe_id": 4
        },
        {
        "id": 6,
        "image": "http://example.com/beef.jpg",
        "name": "beef",
        "recipe_id": 4
        },
        {
        "id": 7,
        "image": "http://example.com/tomato.jpg",
        "name": "pork",
        "recipe_id": 4
        }
        ],
        "instructions": "Cook pasta. Make Sauce",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Spaghetti ",
        "user_id": 1
        }
    ]
    ```

#### POST /recipes
- **Description**: Create a new recipe.
- **Request**:
    ```json
    {
        "title": "Pilau",
        "description": "A classic Kenyan dish made with rice.",
        "prep_time": 15,
        "cook_time": 20,
        "servings": 4,
        "skill_level": "Medium",
        "country": "Kenya",
        "diet": "Vegetarian",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "image_url": "http://example.com/spaghetti.jpg",
        "user_id": 1
    }
    ```
- **Response**:
    ```json
    {
        "Images": [
            {
                "id": 5,
                "image_url": "http://example.com/image1.jpg",
                "recipe_id": 4
            }
        ],
        "banner_image": "http://example.com/spaghetti.jpg",
        "cook_time": 30,
        "country": "Italy",
        "created_at": "2024-07-10T12:00:00",
        "description": "Classic italian meal made of",
        "diet": "Vegetarian",
        "id": 4,
        "ingredients": [
            {
                "id": 5,
                "image": "http://example.com/flour.jpg",
                "name": "Flour",
                "recipe_id": 4
            },
            {
                "id": 6,
                "image": "http://example.com/beef.jpg",
                "name": "beef",
                "recipe_id": 4
            },
            {
                "id": 7,
                "image": "http://example.com/tomato.jpg",
                "name": "pork",
                "recipe_id": 4
            }
        ],
        "instructions": "Cook pasta. Make Sauce",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Spaghetti ",
        "user_id": 1
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create recipe.


#### GET /recipes/{id}
- **Description**: Get an existing recipe.
- **Response**:
    ```json
    {
        "Images": [
            {
            "id": 1,
            "image_url": "http://example.com/spaghetti1.jpg",
            "recipe_id": 1
            },
            {
            "id": 2,
            "image_url": "http://example.com/spaghetti2.jpg",
            "recipe_id": 1
            }
        ],
        "banner_image": "http://example.com/spaghetti.jpg",
        "cook_time": 20,
        "country": "Kenya",
        "created_at": "2024-08-07T00:00:00",
        "description": "A classic Kenyan dish made with rice.",
        "diet": "Vegetarian",
        "id": 1,
        "ingredients": [
            {
            "id": 1,
            "image": "http://example.com/spaghetti.jpg",
            "name": "Spaghetti",
            "recipe_id": 1
            },
            {
            "id": 2,
            "image": "http://example.com/pancetta.jpg",
            "name": "Pancetta",
            "recipe_id": 1
            }
        ],
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "prep_time": 15,
        "servings": 4,
        "skill_level": "Medium",
        "title": "Pilau",
        "user_id": 1
    }
    ```

#### PATCH /recipes/{id}
- **Description**: Update an existing recipe.
- **Request**:
    ```json
    {
        "cook_time": 25,
        "description": "An updated description of the recipe."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "title": "Pilau",
        "description": "An updated description of the recipe.",
        "prep_time": 15,
        "cook_time": 25,
        "servings": 4,
        "skill_level": "Medium",
        "country": "Kenya",
        "diet": "Vegetarian",
        "instructions": "1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.",
        "image_url": "http://example.com/spaghetti.jpg",
        "user_id": 1,
        "created_at": "2024-08-07T00:00:00"
    }
    ```
- **Errors**:
    - `404 Not Found`: Recipe not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update recipe.

#### DELETE /recipes/{id}
- **Description**: Delete an existing recipe.
- **Response**:
    ```json
    {
        "message": "Recipe successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Recipe not found.
    - `500 Internal Server Error`: Unable to delete recipe due to database constraints.

### Ingredients

#### GET /ingredients
- **Description**: Retrieve a list of all ingredients.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "image": "http://example.com/spaghetti.jpg",
            "name": "Spaghetti",
            "recipe_id": 1
        },
        {
            "id": 2,
            "image": "http://example.com/pancetta.jpg",
            "name": "Pancetta",
            "recipe_id": 1
        },
        {
            "id": 3,
            "image": "http://example.com/chicken.jpg",
            "name": "Chicken",
            "recipe_id": 2
        },
        {
            "id": 4,
            "image": "http://example.com/coconut_milk.jpg",
            "name": "Coconut Milk",
            "recipe_id": 2
        },
        {
            "id": 5,
            "image": "http://example.com/flour.jpg",
            "name": "Flour",
            "recipe_id": 4
        },
        {
            "id": 6,
            "image": "http://example.com/beef.jpg",
            "name": "beef",
            "recipe_id": 4
        },
        {
            "id": 7,
            "image": "http://example.com/tomato.jpg",
            "name": "pork",
            "recipe_id": 4
        }
    ]
    ```

#### POST /ingredients
- **Description**: Create a new ingredient.
- **Request**:
    ```json
    {
        "recipe_id": 1,
        "name": "Spaghetti",
        "image": "http://example.com/spaghetti.jpg"
    }
    ```
- **Response**:
    ```json
    {
        "id": 8,
        "image": "http://example.com/images/tomato.jpg",
        "name": "Kachumbari",
        "recipe_id": 1
    }
      
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `404 Not Found`: Recipe not found.
    - `500 Internal Server Error`: Unable to create ingredient.

#### GET /ingredients/{id}
- **Description**: Get an existing ingredient.
- **Response**:
    ```json
    {
        "id": 8,
        "image": "http://example.com/images/tomato.jpg",
        "name": "Kachumbari",
        "recipe_id": 1
    }
   
    ```

#### PATCH /ingredients/{id}
- **Description**: Update an existing ingredient.
- **Request**:
    ```json
    {
        "name": "Updated Ingredient Name",
        "image": "http://example.com/updated_image.jpg"
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "image": "http://example.com/updated_image.jpg",
        "name": "Updated Ingredient Name",
        "recipe_id": 1
    }
     
    ```
- **Errors**:
    - `404 Not Found`: Ingredient not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update ingredient.

#### DELETE /ingredients/{id}
- **Description**: Delete an existing ingredient.
- **Response**:
    ```json
    {
        "message": "Ingredient successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Ingredient not found.
    - `500 Internal Server Error`: Unable to delete ingredient due to database constraints.

### Cooking Hacks

#### GET /cookinghacks
- **Description**: Retrieve a list of all cooking hacks.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "content": "Use a spoon to peel ginger.",
            "created_at": "2024-08-07T00:00:00"
        }
    ]
    ```

#### POST /cookinghacks
- **Description**: Create a new cooking hack.
- **Request**:
    ```json
    {
        "content": "Use a spoon to peel ginger."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "content": "Use a spoon to peel ginger."
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create cooking hack.

#### GET /cookinghacks/{id}
- **Description**: Get an existing cooking hack.
- **Response**:
    ```json
    {
        "content": "To prevent pasta from sticking, add a little oil to the water.",
        "id": 1
    }
    ```

#### PATCH /cookinghacks/{id}
- **Description**: Update an existing cooking hack.
- **Request**:
    ```json
    {
        "content": "Updated cooking hack content."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "content": "Updated cooking hack content."
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking hack not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update cooking hack.

#### DELETE /cookinghacks/{id}
- **Description**: Delete an existing cooking hack.
- **Response**:
    ```json
    {
        "message": "Cooking hack successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking hack not found.
    - `500 Internal Server Error`: Unable to delete cooking hack due to database constraints.

### Cooking Tips

#### GET /cookingtips
- **Description**: Retrieve a list of all cooking tips.
- **Response**:
    ```json
    [
        {
            "content": "Rinse rice before cooking. Use a 1:2 rice-to-water ratio.",
            "created_at": "Wed, 07 Aug 2024 00:00:00 GMT",
            "id": 1,
            "title": "How to cook perfect rice",
            "updated_at": "Wed, 07 Aug 2024 00:00:00 GMT"
        }
    ]
    ```

#### POST /cookingtips
- **Description**: Create a new cooking tip.
- **Request**:
    ```json
    {
        "content": "Add a pinch of salt to enhance sweetness.",
        "title": "How to cook perfect chapatis",
        "created_at": "2024-06-07T00:00:00",
        "updated_at": "2024-07-07T00:00:00"
    }
    ```
- **Response**:
    ```json
    {
        "content": "Add a pinch of salt to enhance sweetness",
        "created_at": "Fri, 07 Jun 2024 00:00:00 GMT",
        "id": 3,
        "title": "How to cook perfect chapatis",
        "updated_at": "Sun, 07 Jul 2024 00:00:00 GMT"
    }
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create cooking tip.

#### GET /cookingtips/{id}
- **Description**: Get an existing cooking tip.
- **Request**:
    ```json
    {
        "content": "Rinse rice before cooking. Use a 1:2 rice-to-water ratio.",
        "created_at": "Wed, 07 Aug 2024 00:00:00 GMT",
        "id": 1,
        "title": "How to cook perfect rice",
        "updated_at": "Wed, 07 Aug 2024 00:00:00 GMT"
    }
    ```
#### PATCH /cookingtips/{id}
- **Description**: Update an existing cooking tip.
- **Request**:
    ```json
    
    {
        "content": "Add my salt to enhance sweetness",
        "created_at": "2024-07-07T00:00:00",
        "id": 1,
        "title": "How to cook perfect chapatis",
        "updated_at": "2024-07-07T00:00:00"
    }
    ```
- **Response**:
    ```json
    {
        "content": "Add my salt to enhance sweetness",
        "created_at": "Sun, 07 Jul 2024 00:00:00 GMT",
        "id": 1,
        "title": "How to cook perfect chapatis",
        "updated_at": "Sun, 07 Jul 2024 00:00:00 GMT"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking tip not found.
    - `400 Bad Request`: Invalid data format.
    - `400 Bad Request`: Invalid date format.
    - `500 Internal Server Error`: Unable to update cooking tip.

#### DELETE /cookingtips/{id}
- **Description**: Delete an existing cooking tip.
- **Response**:
    ```json
    {
        "message": "Cooking tip successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Cooking tip not found.
    - `500 Internal Server Error`: Unable to delete cooking tip due to database constraints.

### Images

#### GET /images
- **Description**: Retrieve a list of all images.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "image_url": "http://example.com/spaghetti1.jpg",
            "recipe_id": 1
        },
        {
            "id": 2,
            "image_url": "http://example.com/spaghetti2.jpg",
            "recipe_id": 1
        },
        {
            "id": 3,
            "image_url": "http://example.com/curry1.jpg",
            "recipe_id": 2
        },
        {
            "id": 4,
            "image_url": "http://example.com/curry2.jpg",
            "recipe_id": 2
        },
        {
            "id": 5,
            "image_url": "http://example.com/image1.jpg",
            "recipe_id": 4
        }
    ]
    ```

#### POST /images
- **Description**: Create a new image.
- **Request**:
    ```json
    {
        "url": "http://example.com/spaghetti5.jpg",
        "recipe_id": "2"
    }
    ```
- **Response**:
    ```json
    {
        "id": 6,
        "image_url": "http://example.com/spaghetti5.jpg",
        "recipe_id": 2
    }
        
    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `500 Internal Server Error`: Unable to create image.


#### GET /images/{id}
- **Description**: Get an existing image.
- **Response**:
    ```json
    {
        "id": 1,
        "image_url": "http://example.com/spaghetti1.jpg",
        "recipe_id": 1
    }
     
    ```

#### PATCH /images/{id}
- **Description**: Update an existing image.
- **Request**:
    ```json
    {
        "image_url": "http://example.com/updated_image.jpg",
        "recipe_id": "1."
    }
    ```
- **Response**:
    ```json
    {
        "id": 1,
        "image_url": "http://example.com/updated_image.jpg",
        "recipe_id": 1
    }
    
    ```
- **Errors**:
    - `404 Not Found`: Image not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update image.

#### DELETE /images/{id}
- **Description**: Delete an existing image.
- **Response**:
    ```json
    {
        "message": "Image successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Image not found.
    - `500 Internal Server Error`: Unable to delete image due to database constraints.

### Replies

#### GET /replies
- **Description**: Retrieve a list of all replies.
- **Response**:
    ```json
    [
        {
            "id": 1,
            "reply": "Thanks for your review! We're glad you enjoyed the recipe.",
            "review": {
                "created_at": "2024-08-07 00:00:00",
                "recipe_id": 1,
                "review": "Great recipe!",
                "updated_at": null,
                "user_id": 1
            }
        },
        {
            "id": 2,
            "reply": "We're sorry to hear that. We will work on improving it.",
            "review": {
                "created_at": "2024-08-07 00:00:00",
                "recipe_id": 1,
                "review": "Tasty, but could use more spices.",
                "updated_at": null,
                "user_id": 2
            }
        }
    ]
    ```

#### POST /replies
- **Description**: Create a new reply.
- **Request**:
    ```json
    {
        "review_id": "1.",
        "reply": "Your recipe is a life saver",
    }
    ```
- **Response**:
    ```json
    {
        "id": 3,
        "reply": "I really liked the tomatoes",
        "review": {
            "created_at": "2024-08-07 00:00:00",
            "recipe_id": 1,
            "review": "Tasty, but could use more spices.",
            "updated_at": null,
            "user_id": 2
        }
    }

    ```
- **Errors**:
    - `400 Bad Request`: Missing required fields.
    - `404 Not Found`: Comment or user not found.
    - `500 Internal Server Error`: Unable to create reply.

#### GET /replies/{id}
- **Description**: Get an existing reply.
- **Request**:
    ```json
   {
        "id": 1,
        "reply": "Thanks for your review! We're glad you enjoyed the recipe.",
        "review": {
            "created_at": "2024-08-07 00:00:00",
            "recipe_id": 1,
            "review": "Great recipe!",
            "updated_at": null,
            "user_id": 1
        }
    }
    ```
#### PATCH /replies/{id}
- **Description**: Update an existing reply.
- **Response**:
    ```json
     {
        "review_id": "3",
        "reply": "Your recipe is a life saver"
    }
    ```
- **Response**:
    ```json
    {
        "id": 2,
        "reply": "Your recipe is a life saver",
        "review": {
            "created_at": "2024-08-07 00:00:00",
            "recipe_id": 2,
            "review": "Delicious and easy to make!",
            "updated_at": null,
            "user_id": 3
        }
    }

    ```
- **Errors**:
    - `404 Not Found`: Reply not found.
    - `400 Bad Request`: Invalid data format.
    - `500 Internal Server Error`: Unable to update reply.

#### DELETE /replies/{id}
- **Description**: Delete an existing reply.
- **Response**:
    ```json
    {
        "message": "Reply successfully deleted"
    }
    ```
- **Errors**:
    - `404 Not Found`: Reply not found.
    - `500 Internal Server Error`: Unable to delete reply due to database constraints.
