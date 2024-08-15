PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE alembic_version (
	version_num VARCHAR(32) NOT NULL, 
	CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);
INSERT INTO alembic_version VALUES('151b1fba3660');
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(80) NOT NULL, 
	first_name VARCHAR(80) NOT NULL, 
	last_name VARCHAR(80) NOT NULL, 
	email VARCHAR(80) NOT NULL, 
	_password_hash VARCHAR NOT NULL, 
	image_url VARCHAR, 
	bio VARCHAR, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
	country VARCHAR, 
	updated_at DATETIME, 
	is_admin BOOLEAN, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
INSERT INTO users VALUES(1,'user1','Anthony','Gachie','user1@example.com','$2b$12$zQnBBe57xsIrERvJ50MoAuSbHzepnoSBZeNfzqR2KneMo0UD6rGei',NULL,NULL,'2024-08-12 10:50:06','Kenya',NULL,0);
INSERT INTO users VALUES(2,'user2','Ben','Gitau','user2@example.com','$2b$12$SLLso/bWKdAaDFOHvYJ6mupWmQ1b.CAWO/kOJG1nI3C/MQ.TTwUyG',NULL,NULL,'2024-08-12 10:50:06','Uganda',NULL,0);
INSERT INTO users VALUES(3,'user3','Audrey','Cherop','user3@example.com','$2b$12$qKN9bw7h8uAKmuV/J0C9WeoGjBT9kkMwPEzVMdYX53duI1pNbMEDG',NULL,NULL,'2024-08-12 10:50:06','Congo',NULL,0);
INSERT INTO users VALUES(4,'user4','Bryan','Odongo','user4@example.com','$2b$12$8Ev3CBv5rEQfiFjiZQbwq.WmbEvvTRJow.EVJtvNxfXUkDmxterbO',NULL,NULL,'2024-08-12 10:50:06','Tanzania',NULL,0);
INSERT INTO users VALUES(5,'user5','Brian','Kipkirui','user5@example.com','$2b$12$YC6ORZPNjy9E9fiwyckHwOXjoS4mJbv763cIm92ba8nKy4GvXRRqe',NULL,NULL,'2024-08-12 10:50:06','Rwanda',NULL,0);
CREATE TABLE cookinghacks (
	id INTEGER NOT NULL, 
	content VARCHAR(2000) NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO cookinghacks VALUES(1,'To prevent pasta from sticking, add a little oil to the water.');
INSERT INTO cookinghacks VALUES(2,'To keep herbs fresh, store them in a jar with a bit of water and cover with a plastic bag.');
CREATE TABLE cookingtips (
	id INTEGER NOT NULL, 
	title VARCHAR(200) NOT NULL, 
	content VARCHAR(2000) NOT NULL, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	updated_at DATETIME NOT NULL, 
	PRIMARY KEY (id)
);
INSERT INTO cookingtips VALUES(1,'How to cook perfect rice','Rinse rice before cooking. Use a 1:2 rice-to-water ratio.','2024-08-07 00:00:00.000000','2024-08-07 00:00:00.000000');
INSERT INTO cookingtips VALUES(2,'Tips for baking bread','Use room temperature ingredients. Don''t overmix the dough.','2024-08-07 00:00:00.000000','2024-08-07 00:00:00.000000');
CREATE TABLE news (
	id INTEGER NOT NULL, 
	image_url VARCHAR, 
	content TEXT, 
	link VARCHAR, 
	PRIMARY KEY (id)
);
INSERT INTO news VALUES(1,'http://example.com/news1.jpg','Breaking: New recipe trends for 2024!','http://example.com/news1');
INSERT INTO news VALUES(2,'http://example.com/news2.jpg','Top 10 kitchen gadgets you need to try.','http://example.com/news2');
CREATE TABLE recipes (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	title VARCHAR(255) NOT NULL, 
	description VARCHAR(2000) NOT NULL, 
	instructions VARCHAR(2000) NOT NULL, 
	country VARCHAR(100) NOT NULL, 
	prep_time INTEGER NOT NULL, 
	cook_time INTEGER NOT NULL, 
	servings INTEGER NOT NULL, 
	diet VARCHAR(100) NOT NULL, 
	banner_image VARCHAR(255) NOT NULL, 
	skill_level VARCHAR(100), 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
);
INSERT INTO recipes VALUES(1,1,'Pilau','A classic Kenyan dish made with rice.','1. Boil Rice. 2. Cook Onions. 3. Fry Tomatoes. 4. Combine all ingredients.','Kenya',15,20,4,'Vegetarian','http://example.com/spaghetti.jpg','Medium','2024-08-07 00:00:00.000000');
INSERT INTO recipes VALUES(2,2,'Chicken Curry','A spicy and flavorful chicken curry with coconut milk and aromatic spices.','1. Cook chicken with spices. 2. Add coconut milk and simmer. 3. Serve with rice.','India',20,40,4,'Non-Vegetarian','http://example.com/curry.jpg','Hard','2024-08-07 00:00:00.000000');
INSERT INTO recipes VALUES(3,1,'Spaghetti ','Classic italian meal made of','Cook pasta. Make Sauce','Italy',15,30,4,'Vegetarian','http://example.com/spaghetti.jpg','Medium','2024-07-10 12:00:00.000000');
INSERT INTO recipes VALUES(4,1,'Spaghetti ','Classic italian meal made of','Cook pasta. Make Sauce','Italy',15,30,4,'Vegetarian','http://example.com/spaghetti.jpg','Medium','2024-07-10 12:00:00.000000');
CREATE TABLE ingredients (
	id INTEGER NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	name VARCHAR(100) NOT NULL, 
	image VARCHAR(255), 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);
INSERT INTO ingredients VALUES(1,1,'Updated Ingredient Name','http://example.com/new_image.jpg');
INSERT INTO ingredients VALUES(2,1,'Pancetta','http://example.com/pancetta.jpg');
INSERT INTO ingredients VALUES(3,2,'Chicken','http://example.com/chicken.jpg');
INSERT INTO ingredients VALUES(4,2,'Coconut Milk','http://example.com/coconut_milk.jpg');
INSERT INTO ingredients VALUES(5,4,'Flour','http://example.com/flour.jpg');
INSERT INTO ingredients VALUES(6,4,'beef','http://example.com/beef.jpg');
INSERT INTO ingredients VALUES(7,4,'pork','http://example.com/tomato.jpg');
INSERT INTO ingredients VALUES(8,1,'Kachumbari','http://example.com/images/tomato.jpg');
CREATE TABLE images (
	id INTEGER NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	image_url VARCHAR(255), 
	PRIMARY KEY (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);
INSERT INTO images VALUES(1,1,'http://example.com/updated_image.jpg');
INSERT INTO images VALUES(2,1,'http://example.com/spaghetti2.jpg');
INSERT INTO images VALUES(3,2,'http://example.com/curry1.jpg');
INSERT INTO images VALUES(4,2,'http://example.com/curry2.jpg');
INSERT INTO images VALUES(5,4,'http://example.com/image1.jpg');
CREATE TABLE reviews (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	recipe_id INTEGER, 
	review TEXT, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
	updated_at DATETIME, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);
INSERT INTO reviews VALUES(1,1,1,'Great recipe!','2024-08-07 00:00:00.000000',NULL);
INSERT INTO reviews VALUES(2,2,1,'Tasty, but could use more spices.','2024-08-07 00:00:00.000000',NULL);
INSERT INTO reviews VALUES(3,3,2,'Delicious and easy to make!','2024-08-07 00:00:00.000000',NULL);
INSERT INTO reviews VALUES(4,4,2,'Too spicy for my taste.','2024-08-07 00:00:00.000000',NULL);
CREATE TABLE bookmarks (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	recipe_id INTEGER, 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);
INSERT INTO bookmarks VALUES(1,1,1,'2024-08-12 10:50:07');
INSERT INTO bookmarks VALUES(2,2,2,'2024-08-12 10:50:07');
CREATE TABLE ratings (
	id INTEGER NOT NULL, 
	user_id INTEGER NOT NULL, 
	recipe_id INTEGER NOT NULL, 
	rating INTEGER NOT NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id), 
	FOREIGN KEY(recipe_id) REFERENCES recipes (id)
);
INSERT INTO ratings VALUES(1,1,1,4);
INSERT INTO ratings VALUES(2,2,1,3);
INSERT INTO ratings VALUES(3,3,2,5);
INSERT INTO ratings VALUES(4,4,2,2);
CREATE TABLE replies (
	id INTEGER NOT NULL, 
	review_id INTEGER NOT NULL, 
	reply VARCHAR(1000), 
	PRIMARY KEY (id), 
	FOREIGN KEY(review_id) REFERENCES reviews (id)
);
INSERT INTO replies VALUES(1,1,'Thanks for your review! We''re glad you enjoyed the recipe.');
INSERT INTO replies VALUES(2,3,'Your recipe is a life saver');
INSERT INTO replies VALUES(3,2,'I really liked the tomatoes');
COMMIT;