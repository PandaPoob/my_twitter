--USERS--
DROP TABLE IF EXISTS users;

CREATE TABLE users(
  user_id                TEXT UNIQUE NOT NULL,
  user_name              TEXT UNIQUE NOT NULL,
  user_full_name         TEXT NOT NULL,
  user_password          TEXT NOT NULL,
  user_email             TEXT UNIQUE NOT NULL,
  user_phonenumber       TEXT,
  user_api_key           TEXT UNIQUE NOT NULL,
  user_created_at        INT NOT NULL,
  user_updated_at        INT NOT NULL,
  user_img_avatar        TEXT,
  user_img_cover         TEXT,
  user_bio_text          TEXT,
  user_bio_location      TEXT,
  user_bio_link          TEXT,
  user_bio_birthday      TEXT NOT NULL,
  user_total_followers   INT DEFAULT 0,
  user_total_following   INT DEFAULT 0,
  user_total_tweets      INT DEFAULT 0,
  user_twitterblue       BOOLEAN DEFAULT false,
  user_account_status    VARCHAR(8) DEFAULT "inactive",
  PRIMARY KEY(user_id)
  ) WITHOUT ROWID;

CREATE INDEX idx_users_user_first_name ON users(user_full_name);


--TWEETS--
DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                VARCHAR(35) UNIQUE NOT NULL,
  tweet_slug              VARCHAR(35) UNIQUE NOT NULL,
  tweet_user_fk           VARCHAR(35) NOT NULL,
  tweet_created_at        INT NOT NULL,
  tweet_updated_at        INT,
  tweet_field_text        VARCHAR(280),
  tweet_field_images      INT DEFAULT 0,
  tweet_total_replies     INT DEFAULT 0,
  tweet_total_likes       INT DEFAULT 0,
  tweet_total_retweets    INT DEFAULT 0,
  tweet_total_views       INT DEFAULT 0,
  tweet_parent_id         VARCHAR(35),
  tweet_type              VARCHAR(7) DEFAULT "default",
  PRIMARY KEY(tweet_id)
  ) WITHOUT ROWID;


--TWEET IMAGES--
DROP TABLE IF EXISTS tweet_images;
create TABLE tweet_images(
  tweet_image_id          VARCHAR(35) UNIQUE NOT NULL,
  tweet_image_tweet_fk    VARCHAR(35) NOT NULL,
  tweet_image_url         VARCHAR(40) UNIQUE NOT NULL,
  tweet_image_order       INT DEFAULT 0,
  tweet_image_created_at  INT NOT NULL,
  PRIMARY KEY(tweet_image_id)
) WITHOUT ROWID;


--TRENDS--
DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  INT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;


--FOLLOWING--
DROP TABLE IF EXISTS following;
CREATE TABLE following(
  follower_fk           TEXT NOT NULL,
  followee_fk           TEXT NOT NULL,
  following_created_at  INT NOT NULL,
  PRIMARY KEY(follower_fk, followee_fk)
) WITHOUT ROWID;

-----VIEWS-----
--This view is to get the user, tweets and images--
DROP VIEW IF EXISTS [users_and_tweets];
CREATE VIEW users_and_tweets
AS
SELECT * FROM tweets
JOIN users ON users.user_id = tweets.tweet_user_fk;

--This view is for follow suggestions so we do not get unnecessary info--
DROP VIEW IF EXISTS [follower_suggestions];
CREATE VIEW follower_suggestions
AS
SELECT users.user_id, users.user_name, users.user_full_name, users.user_img_avatar, users.user_twitterblue
FROM users;


--TRIGGERS--
SELECT name FROM sqlite_master WHERE type = "trigger";

--increase tweet count if user tweets 
DROP TRIGGER IF EXISTS increment_user_total_tweets;
CREATE TRIGGER increment_user_total_tweets AFTER INSERT ON tweets
BEGIN 
    UPDATE users 
    SET user_total_tweets = user_total_tweets + 1
    WHERE user_id = NEW.tweet_user_fk;
END;

--decrease if tweet count on user if tweet is deleted
DROP TRIGGER IF EXISTS decrement_user_total_tweets;
CREATE TRIGGER decrement_user_total_tweets AFTER DELETE ON tweets
BEGIN 
    UPDATE users 
    SET user_total_tweets = user_total_tweets - 1
    WHERE user_id = OLD.tweet_user_fk;
END; 

--increase follower count if user is followed
DROP TRIGGER IF EXISTS increment_user_total_followers;
CREATE TRIGGER increment_user_total_followers AFTER INSERT ON following
BEGIN 
    UPDATE users
    SET user_total_followers = user_total_followers + 1
    WHERE user_id = NEW.followee_fk;
END;

--decrease follower count if user is unfollowed
DROP TRIGGER IF EXISTS decrement_user_total_followers;
CREATE TRIGGER decrement_user_total_followers AFTER DELETE ON following
BEGIN 
    UPDATE users
    SET user_total_followers = user_total_followers - 1
    WHERE user_id = OLD.followee_fk;
END;

--increase followee count if user is followed
DROP TRIGGER IF EXISTS increment_user_total_following;
CREATE TRIGGER increment_user_total_following AFTER INSERT ON following
BEGIN 
    UPDATE users
    SET user_total_following = user_total_following + 1
    WHERE user_id = NEW.follower_fk;
END;

--decrease followee count if user is unfollowed
DROP TRIGGER IF EXISTS decrement_user_total_following;
CREATE TRIGGER decrement_user_total_following AFTER DELETE ON following
BEGIN 
    UPDATE users
    SET user_total_following = user_total_following - 1
    WHERE user_id = OLD.follower_fk;
END;


