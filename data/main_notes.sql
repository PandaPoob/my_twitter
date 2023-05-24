DROP TABLE IF EXISTS users;

CREATE TABLE users(
  user_id                TEXT UNIQUE NOT NULL,
  user_name              TEXT UNIQUE NOT NULL,
  user_full_name         TEXT UNIQUE NOT NULL,
  user_img_avatar        TEXT UNIQUE DEFAULT "unknown.jpg",
  user_img_cover         TEXT NOT NULL,
  user_verified          TEXT,
  user_bio_text          TEXT,
  user_bio_location      TEXT,
  user_bio_link          TEXT,
  user_bio_birthday      TEXT,
  user_bio_created_at    TEXT NOT NULL,
  user_total_followers   TEXT DEFAULT 0,
  user_total_following   TEXT DEFAULT 0,
  user_total_tweets      TEXT DEFAULT 0,
  PRIMARY KEY(user_id)
  ) WITHOUT ROWID;

--another way to index if you do not write UNIQUE in query:
CREATE UNIQUE INDEX idx_users_user_full_name ON users(user_full_name);
--index your query:
CREATE INDEX idx_users_user_name ON users(user_name);

SELECT name FROM sqlite_master WHERE type = "index";
SELECT name FROM sqlite_master WHERE type = "trigger";
--all the tweets with all the users

INSERT INTO users VALUES("5ae1823bcc5648bd9e5bf6602ae397d6", "elonmusk", "Elon Musk", "5ae1823bcc5648bd9e5bf6602ae397d6.jpg", "ad3b5a9a8fe3471d814ff845b9671cc0.jpg", True, "", "", "", "", "1243814400", "128900000", "177", "22900");
INSERT INTO users VALUES("63bfa35aa8204270a6480557fddf9069", "shakira", "Shakira", "63bfa35aa8204270a6480557fddf9069.jpg", "76a574041471471bb7a806ed197198aa.jpg", True, "MONOTONÍA YA DISPONIBLE", "Barranquilla", "linktr.ee/shakira", "November 30, 1998", "1246406399", "537000000", "235", "8002");
INSERT INTO users VALUES("96e7977bdaab4f0abe84e7ac18a864ec", "BLACKPINK", "BLACKPINKOFFICIAL", "96e7977bdaab4f0abe84e7ac18a864ec.jpg", "0684090441a743e6ba92eb42b4ee8816.jpg", True, "BLΛƆKPIИK", "", "lnk.to/YG_BLACKPINK", "", "1590969600", "8500000", "0", "892");
INSERT INTO users VALUES("a3fb674a90c84918968c2425e21e1a4e", "cat_auras", "cat with confusing auras.", "a3fb674a90c84918968c2425e21e1a4e.jpg", "0f0cb4cb07424f1ea0d0e87705cb1745.jpg", True, "Even cat can confuse “us”. | dm for credit or removal.", "", "catauras.com", "", "1654041600", "1600000", "15", "167");

INSERT INTO users VALUES("63bfa35aa8204270a6480557fddf9069", "shakira", "Shakira", "shakirapass", "shakira@mail.com", "", "9feb12d3732e4f32bfdf9c37a732541f", "1246406399", "1246406399", "63bfa35aa8204270a6480557fddf9069.jpg", "76a574041471471bb7a806ed197198aa.jpg", "MONOTONÍA YA DISPONIBLE", "Barranquilla", "linktr.ee/shakira", "November 30, 1998", "537000000", "235", "8002", True, "active");
--11 shakira tweets
INSERT INTO tweets VALUES(
"0355140a4ddf4601b472918a34e70684",
"220b3ad490fb4909b9665b7d974a536e",
"63bfa35aa8204270a6480557fddf9069",
"1672492768",
"0",
"Música y amistad, la mejor combinación",
"0",
"1791",
"69400",
"2442",
"5000000",
"",
"default");
INSERT INTO tweets VALUES(
"9c5a606cea5e4f83ac7212d546f663c0",
"6f7ba09da87146389daf2c205f82ccf8",
"63bfa35aa8204270a6480557fddf9069",
"1672406368",
"0",
"Estou contigo Brazil.",
"0",
"2833",
"214600",
"9570",
"69000000",
"",
"default");
INSERT INTO tweets VALUES(
"40adb4f73536454aa083ab2d016f639a",
"f51ff35d0c9c49d5855f2291039ac2f7",
"63bfa35aa8204270a6480557fddf9069",
"1671974368",
"0",
"In the desert this Christmas, searching for serenity. En el desierto buscando la serenidad en esta navidad.",
"0",
"1177",
"12700",
"3980",
"5100000",
"",
"default");
INSERT INTO tweets VALUES(
"0a1ec9740bc1473f981d6a396ddd5b58",
"00aac862c88746419a612ab96e21a0bc",
"63bfa35aa8204270a6480557fddf9069",
"1671887968",
"0",
"Thanks for all the love and support you gave me and my kids during this year. I wish you a sweet holiday. Here's to a 2023 that's filled with peace and hope.",
"0",
"780",
"33400",
"1535",
"21000000",
"",
"default");
INSERT INTO tweets VALUES(
"8382c24d21a94d2fa252b07da288f070",
"f6b4ab3e302e4458814e12cfcb016dbe",
"63bfa35aa8204270a6480557fddf9069",
"1671376768",
"0",
"Today at the final of the World Cup, I only hope the players on the field and the whole world remembers that there’s a man and fellow footballer called Amir Nasr, on death row, only for speaking in favor of Women's rights.",
"0",
"3292",
"573500",
"151400",
"24000000",
"",
"default");
INSERT INTO tweets VALUES(
"0abb3835b51a44c28e7c931f524d4329",
"14fdcf07fe43435a8770d909f673c2bd",
"63bfa35aa8204270a6480557fddf9069",
"1670685568",
"0",
"This time for Africa!!",
"0",
"11200",
"1100000",
"204100",
"1",
"",
"default");
INSERT INTO tweets VALUES(
"e165daf4ec884838bd47eb0da9a1f000",
"dee930956fa64c939439b94df484f420",
"63bfa35aa8204270a6480557fddf9069",
"1667315968",
"0",
"Is this so pathetic that I'm eating my kids candy?",
"0",
"956",
"27300",
"1195",
"1",
"",
"default");
INSERT INTO tweets VALUES(
"198c648b70304d7483c0e10fa1c5525c",
"aa5b029f394e42b3b67cfcb2c4706862",
"63bfa35aa8204270a6480557fddf9069",
"1667229568",
"0",
"De porrista a súper héroe. Por cierto la mujer maravilla fue mi primer disfraz! Halloween, la excusa perfecta para sublimar deseos de infancia! ",
"0",
"976",
"57700",
"3350",
"1",
"",
"default");
INSERT INTO tweets VALUES(
"a62046b4a2054d9f99608931ef29c4d5",
"536d66f347ae41ffb32d39eb41d2e5f0",
"63bfa35aa8204270a6480557fddf9069",
"1666192768",
"0",
"Gracias por la camiseta Ozu!  And happy launch day!",
"0",
"557",
"41100",
"1797",
"1",
"",
"default");
INSERT INTO tweets VALUES(
"b6173e050d4d4aa9a1fda4eb675f6221",
"915bdeb6ad02469795f4cd0b2849b713",
"63bfa35aa8204270a6480557fddf9069",
"1665501568",
"0",
"My heart is with Mahsa Amini's family and with the women and schoolgirls of Iran and all those fighting for freedom of expression.",
"0",
"7931",
"119800",
"36600",
"1",
"",
"default");
INSERT INTO tweets VALUES(
"576ba96baaaf47c481b664fce91d27af",
"ee78c76982f24529a23b8d035a73f2d6",
"63bfa35aa8204270a6480557fddf9069",
"1660144768",
"0",
"Perteneciste a una raza antigua. De pies descalzos y de sueños blancos…",
"0",
"3326",
"164000",
"21100",
"1",
"",
"default");

--Shakira images
INSERT INTO tweet_images VALUES(
"f163c4e7111c4e9f8a5716d697effe70",
"0a1ec9740bc1473f981d6a396ddd5b58",
"0f9fe9d6487e4374855565e5a42a3d05.jpg",
0,
"1671887968"
);
INSERT INTO tweet_images VALUES(
"1cb4e361f92b4c9cb98c9b31470f7ee0",
"e165daf4ec884838bd47eb0da9a1f000",
"4b4e450df49847bfb778df8620dafb83.jpg",
0,
"1667315968"
);
INSERT INTO tweet_images VALUES(
"00e116e2926541d1932876f60d64f7e7",
"b6173e050d4d4aa9a1fda4eb675f6221",
"05b95fe121cd4e6dbaf8537535cfbc9f.jpg",
0,
"1665501568"
);
INSERT INTO tweet_images VALUES(
"ca925d6f37d74d6b9261bb0c8c5559e0",
"a62046b4a2054d9f99608931ef29c4d5",
"e701f27cda9d47e0bfb368ee8da0ac57.jpg",
0,
"1666192768"
);
INSERT INTO tweet_images VALUES(
"8954c33aa3fd4ba1b79c05e02b1af3fd",
"0355140a4ddf4601b472918a34e70684",
"f4127dbd14fe42b5ac5d856d1f5a207e.jpg",
0,
"1672492768"
);
INSERT INTO tweet_images VALUES(
"20fa71b714544b9881f60fae91cc1d35",
"198c648b70304d7483c0e10fa1c5525c",
"f4709b9b8faa449daf02194f74ffd11b.jpg",
0,
"1667229568"
);
INSERT INTO tweet_images VALUES(
"186dc3aa1b9f4d0db137ee0852a0c4c7",
"40adb4f73536454aa083ab2d016f639a",
"f7036717e88d499c8e1b727fd5befbf2.jpg",
0,
"1671974368"
);

INSERT INTO tweet_images VALUES(
"5947237d40384dec8638cabab704bcff",
"8382c24d21a94d2fa252b07da288f070",
"fc0f8c2cce82492f87fd932b43203441.jpg",
0,
"1671376768"
);

SELECT * FROM users
JOIN tweets
ON users.user_id = tweets.user_fk;

--CREATE VIEW users_by_name
--AS
--SELECT * FROM users ORDER BY fullname COLLATE NOCASE ASC;
DROP VIEW IF EXISTS [users_and_tweets];
CREATE VIEW users_and_tweets
AS
SELECT * FROM users
JOIN tweets
ON users.user_id = tweets.user_fk;

SELECT * FROM tweets ORDER BY created_at DESC;
--You can now call the view/virtual table
SELECT * FROM users_by_name;
--Give you only 1:
--SELECT * FROM users_by_name LIMIT 1;

CREATE TABLE tweets(
  tweet_id                TEXT,
  tweet_user_fk           TEXT,
  tweet_created_at        TEXT,
  tweet_field_text        TEXT,
  tweet_field_img         TEXT,
  tweet_updated_at        TEXT,
  tweet_total_replies     TEXT,
  tweet_total_likes       TEXT,
  tweet_total_retweets    TEXT,
  tweet_total_views       TEXT,
  PRIMARY KEY(tweet_id)
  ) WITHOUT ROWID;

CREATE TABLE trends(
  trend_id                TEXT,
  trend_title             TEXT NOT NULL,
  trend_total_tweets      TEXT DEFAULT 0,

  PRIMARY KEY(id)
  ) WITHOUT ROWID;


DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN 
    UPDATE users 
    SET user_total_tweets = user_total_tweets + 1
    WHERE user_id = NEW.user_fk;
END;

DROP TRIGGER IF EXISTS decrement_user_total_tweets;
DROP TRIGGER IF EXISTS decrease_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN 
    UPDATE users 
    SET user_total_tweets = user_total_tweets - 1
    WHERE user_id = OLD.user_fk;
END;


SELECT user_name, user_total_tweets FROM users;

INSERT INTO tweets VALUES(
"447ae99181ca45718fffbb2001c3f429",
"a3fb674a90c84918968c2425e21e1a4e",
"1676114368",
"meow 2",
"",
"0",
"154",
"15300",
"3640",
"12000000");

DELETE FROM tweets WHERE tweet_id = "43d756d87e6240d6b8295aea3a96c070";

