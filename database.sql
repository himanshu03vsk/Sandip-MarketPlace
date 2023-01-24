-- #Instead of having 2 table auction we can have a category of auction_type and selling_type
-- #We may need different set of attributes to be set by user in regard to the type of item so some fields might be empty,
-- so maybe we can keep them seperate.


CREATE TABLE user (
    user_id varchar(100) NOT NULL,
    lastname varchar(255) NOT NULL,
    firstname varchar(255)NOT NULL,
    password varchar(255) NOT NULL,    
    location varchar(255) NOT NULL,
    institute_name varchar(255),
    user_photo text,
    PRIMARY KEY(user_id)
);


CREATE TABLE selling_items (
	item_id int NOT NULL AUTO_INCREMENT,
	name varchar(255),
	description text,
	posting_date varchar(20),
	is_sold Boolean,
	sold_to varchar(100),
	seller_id varchar(100),
	item_category varchar(255),
    PRIMARY KEY(item_id),
	FOREIGN KEY (sold_to) REFERENCES user(user_id),
	FOREIGN KEY (seller_id) REFERENCES user(user_id)
);


CREATE TABLE ads_list (
	selling_item_id int,
	user_id varchar(255),
	auction_item_id int,
	FOREIGN KEY (user_id) REFERENCES user(user_id),
	FOREIGN KEY (auction_item_id) REFERENCES auction_item(item_id),
	FOREIGN KEY (selling_item_id) REFERENCES selling_items(item_id)

);



CREATE TABLE auction_item(
	item_id int NOT NULL AUTO_INCREMENT,
	name varchar(255),
	description text,
	posting_date varchar(50),
	seller_id varchar(255),
	sold_to varchar(255),
	is_sold BOOLEAN,
	item_category varchar(255),
    PRIMARY KEY (item_id),
    FOREIGN KEY (seller_id) REFERENCES user(user_id),
    FOREIGN KEY (sold_to) REFERENCES user(user_id)
);	