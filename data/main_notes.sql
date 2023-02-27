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
--
--
--4a15bbbed6474f8992afbab07ee8bc52
--4a63b6acc87e41e3a643973f7fda236e
--5da74ffea06b4a4980dc42a74bd62bf6	
--73a3b83aca5544fd8618b923d717490a
--743680dedee44a43a4299291c0b794ec
--75033bbe66c34586955e4d6339f01f53
--88959f504a644a9780277a4cdcd606a6
--99fa8805dea643d7ad9e038ec37195e9
--a0aaf00257774f4597c9b486a1d66078
--ab1bbb1d5ac34d6c84bdb306442a8ff0
--ba010f716d20427a86185400003dca0a


