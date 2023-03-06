DROP TABLE IF EXISTS users;

CREATE TABLE users(
  user_id                TEXT UNIQUE NOT NULL,
  user_name              TEXT UNIQUE NOT NULL,
  user_full_name         TEXT NOT NULL,
  user_password          TEXT NOT NULL,
  user_img_avatar        TEXT UNIQUE,
  user_img_cover         TEXT NOT NULL,
  user_verified          TEXT DEFAULT false,
  user_bio_text          TEXT,
  user_bio_location      TEXT,
  user_bio_link          TEXT,
  user_bio_birthday      TEXT NOT NULL,
  user_bio_created_at    INT NOT NULL,
  user_total_followers   INT DEFAULT 0,
  user_total_following   INT DEFAULT 0,
  user_total_tweets      INT DEFAULT 0,
  PRIMARY KEY(user_id)
  ) WITHOUT ROWID;

INSERT INTO users VALUES("5ae1823bcc5648bd9e5bf6602ae397d6", "elonmusk", "Elon Musk", "elonmuskpass", "5ae1823bcc5648bd9e5bf6602ae397d6.jpg", "ad3b5a9a8fe3471d814ff845b9671cc0.jpg", True, "", "", "", "", "1243814400", "128900000", "177", "22900");
INSERT INTO users VALUES("63bfa35aa8204270a6480557fddf9069", "shakira", "Shakira", "shakirapass", "63bfa35aa8204270a6480557fddf9069.jpg", "76a574041471471bb7a806ed197198aa.jpg", True, "MONOTONÍA YA DISPONIBLE", "Barranquilla", "linktr.ee/shakira", "November 30, 1998", "1246406399", "537000000", "235", "8002");
INSERT INTO users VALUES("96e7977bdaab4f0abe84e7ac18a864ec", "BLACKPINK", "BLACKPINKOFFICIAL", "blackpinkpass", "96e7977bdaab4f0abe84e7ac18a864ec.jpg", "0684090441a743e6ba92eb42b4ee8816.jpg", True, "BLΛƆKPIИK", "", "lnk.to/YG_BLACKPINK", "", "1590969600", "8500000", "0", "892");
INSERT INTO users VALUES("a3fb674a90c84918968c2425e21e1a4e", "cat_auras", "cat with confusing auras.", "cat_auraspass", "a3fb674a90c84918968c2425e21e1a4e.jpg", "0f0cb4cb07424f1ea0d0e87705cb1745.jpg", True, "Even cat can confuse “us”. | dm for credit or removal.", "", "catauras.com", "", "1654041600", "1600000", "15", "167");
INSERT INTO users VALUES("b3094c2f1c144817b7cc0b718fc3c644", "my_name_cleo", "Cleo", "my_name_cleopass", "b3094c2f1c144817b7cc0b718fc3c644.jpg", "8e89394382ca44d2bb3cc45d067c2a7e.jpg", False, "I am a happy doge", "", "https://www.instagram.com/my_name_cleo/", "", "1677605053", "126", "0", "0");

CREATE INDEX idx_users_user_first_name ON users(user_full_name);


--##############################################################

DROP TABLE IF EXISTS tweets;
CREATE TABLE tweets(
  tweet_id                TEXT,
  tweet_user_fk           TEXT,
  tweet_created_at        INT,
  tweet_field_text        TEXT,
  tweet_field_img         TEXT,
  tweet_updated_at        TEXT,
  tweet_total_replies     INT DEFAULT 0,
  tweet_total_likes       INT DEFAULT 0,
  tweet_total_retweets    INT DEFAULT 0,
  tweet_total_views       INT DEFAULT 0,
  PRIMARY KEY(tweet_id)
  ) WITHOUT ROWID;

  --11 elon musk tweets
INSERT INTO tweets VALUES(
"500151d40e26414f82b9aca854c5a059",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676834368",
"",
"500151d40e26414f82b9aca854c5a059.jpg",
"0",
"65786",
"237100",
"16400",
"46900000");
INSERT INTO tweets VALUES(
"3c417a8c92d244dc80e7b2c2a5def367",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676819968",
"All things in moderation, 
especially content moderation",
"3c417a8c92d244dc80e7b2c2a5def367.jpg",
"0",
"10000",
"85700",
"8082",
"29700000");
INSERT INTO tweets VALUES(
"4d2db7af8d02411b831bcb0064de19ca",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676812768",
"BingChatGPT reminds me of Lucky in Waiting for Godot",
"",
"0",
"4125",
"63000",
"4301",
"31300000");
INSERT INTO tweets VALUES(
"1b45faeadfb046f4a90c0c151b86ca6a",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676798368",
"",
"1b45faeadfb046f4a90c0c151b86ca6a.jpg",
"0",
"14600",
"461400",
"31500",
"58200000");
INSERT INTO tweets VALUES(
"4b88a9d72171459ca1b4690d1a8c3792",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676719168",
"Surround your house with treadmills set to jogging speed to stop walking dead ur welcome",
"4b88a9d72171459ca1b4690d1a8c3792.jpg",
"0",
"17300",
"462500",
"36800",
"65600000");
INSERT INTO tweets VALUES(
"58838f22d6be43ffae7d73585d5e2b76",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676704768",
"Interesting",
"58838f22d6be43ffae7d73585d5e2b76.jpg",
"0",
"10800",
"173700",
"17800",
"45900000");
INSERT INTO tweets VALUES(
"b7d54f24ac224981b41d33c68fc54323",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676701168",
"",
"b7d54f24ac224981b41d33c68fc54323.jpg",
"0",
"5991",
"120600",
"8351",
"36400000");
INSERT INTO tweets VALUES(
"5bd98366765342579e9d15cc4b71b6a8",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676629168",
"Note: if many people who you follow or like also follow me, it is highly probable that the algorithm will recommend my tweets. It’s not super sophisticated.

In coming months, we will offer the ability to adjust the algorithm to closer match what is most compelling to you.",
"",
"0",
"10400",
"161800",
"11500",
"36600000");
INSERT INTO tweets VALUES(
"5e7c131e977646b491c8e06d7852c12d",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676625568",
"What we need is TruthGPT",
"",
"0",
"21300",
"297300",
"29600",
"49100000");
INSERT INTO tweets VALUES(
"6de4cffad29d4b23a7e30e7f6688bfbd",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676621968",
"Sorry for showing you so many irrelevant & annoying ads on Twitter! 

We're taking the (obvious) corrective action of tying ads to keywords & topics in tweets, like Google does with search.

This will improve contextual relevance dramatically.",
"",
"0",
"7720",
"126700",
"8218",
"67000000");
INSERT INTO tweets VALUES(
"d14d81bdc33d4953b0acec2867a899c7",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676607568",
"ChatGPT to the mainstream media",
"d14d81bdc33d4953b0acec2867a899c7.jpg",
"0",
"9747",
"325300",
"26900",
"60700000");
INSERT INTO tweets VALUES(
"b66b072968e84e98b67d342e4c92a5ef",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676467168",
"He's great with numbers!",
"b66b072968e84e98b67d342e4c92a5ef.jpg",
"0",
"14900",
"614200",
"40100",
"80600000");

--11 shakira tweets
INSERT INTO tweets VALUES(
"0355140a4ddf4601b472918a34e70684",
"63bfa35aa8204270a6480557fddf9069",
"1672492768",
"Música y amistad, la mejor combinación",
"0355140a4ddf4601b472918a34e70684.jpg",
"0",
"1791",
"69400",
"2442",
"5000000");
INSERT INTO tweets VALUES(
"9c5a606cea5e4f83ac7212d546f663c0",
"63bfa35aa8204270a6480557fddf9069",
"1672406368",
"Estou contigo Brazil.",
"",
"0",
"2833",
"214600",
"9570",
"69000000");
INSERT INTO tweets VALUES(
"40adb4f73536454aa083ab2d016f639a",
"63bfa35aa8204270a6480557fddf9069",
"1671974368",
"In the desert this Christmas, searching for serenity. En el desierto buscando la serenidad en esta navidad.",
"40adb4f73536454aa083ab2d016f639a.jpg",
"0",
"1177",
"12700",
"3980",
"5100000");
INSERT INTO tweets VALUES(
"0a1ec9740bc1473f981d6a396ddd5b58",
"63bfa35aa8204270a6480557fddf9069",
"1671887968",
"Thanks for all the love and support you gave me and my kids during this year. I wish you a sweet holiday. Here's to a 2023 that's filled with peace and hope.",
"0a1ec9740bc1473f981d6a396ddd5b58.jpg",
"0",
"780",
"33400",
"1535",
"21000000");
INSERT INTO tweets VALUES(
"8382c24d21a94d2fa252b07da288f070",
"63bfa35aa8204270a6480557fddf9069",
"1671376768",
"Today at the final of the World Cup, I only hope the players on the field and the whole world remembers that there’s a man and fellow footballer called Amir Nasr, on death row, only for speaking in favor of Women's rights.",
"8382c24d21a94d2fa252b07da288f070.jpg",
"0",
"3292",
"573500",
"151400",
"24000000");
INSERT INTO tweets VALUES(
"0abb3835b51a44c28e7c931f524d4329",
"63bfa35aa8204270a6480557fddf9069",
"1670685568",
"This time for Africa!!",
"",
"0",
"11200",
"1100000",
"204100",
"1");
INSERT INTO tweets VALUES(
"e165daf4ec884838bd47eb0da9a1f000",
"63bfa35aa8204270a6480557fddf9069",
"1667315968",
"Is this so pathetic that I'm eating my kids candy?",
"e165daf4ec884838bd47eb0da9a1f000.jpg",
"0",
"956",
"27300",
"1195",
"1");
INSERT INTO tweets VALUES(
"198c648b70304d7483c0e10fa1c5525c",
"63bfa35aa8204270a6480557fddf9069",
"1667229568",
"De porrista a súper héroe. Por cierto la mujer maravilla fue mi primer disfraz! Halloween, la excusa perfecta para sublimar deseos de infancia! ",
"198c648b70304d7483c0e10fa1c5525c.jpg",
"0",
"976",
"57700",
"3350",
"1");
INSERT INTO tweets VALUES(
"a62046b4a2054d9f99608931ef29c4d5",
"63bfa35aa8204270a6480557fddf9069",
"1666192768",
"Gracias por la camiseta Ozu!  And happy launch day!",
"a62046b4a2054d9f99608931ef29c4d5.jpg",
"0",
"557",
"41100",
"1797",
"1");
INSERT INTO tweets VALUES(
"b6173e050d4d4aa9a1fda4eb675f6221",
"63bfa35aa8204270a6480557fddf9069",
"1665501568",
"My heart is with Mahsa Amini's family and with the women and schoolgirls of Iran and all those fighting for freedom of expression.",
"b6173e050d4d4aa9a1fda4eb675f6221.jpg",
"0",
"7931",
"119800",
"36600",
"1");
INSERT INTO tweets VALUES(
"576ba96baaaf47c481b664fce91d27af",
"63bfa35aa8204270a6480557fddf9069",
"1660144768",
"Perteneciste a una raza antigua. De pies descalzos y de sueños blancos…",
"",
"0",
"3326",
"164000",
"21100",
"1");


--11 blackpink tweets
INSERT INTO tweets VALUES(
"9a8280289f5547369e7cddbeb1a9aded",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1676647168",
"BLACKPINK TOUR MERCH RESTOCK",
"9a8280289f5547369e7cddbeb1a9aded.jpg",
"0",
"603",
"33300",
"4497",
"1000000");
INSERT INTO tweets VALUES(
"8b0fbf87efbb4e478a27c804e54b3cb3",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1676639968",
"BLACKPINK [BORN PINK] VINYL",
"8b0fbf87efbb4e478a27c804e54b3cb3.jpg",
"0",
"703",
"26900",
"4100",
"812400");
INSERT INTO tweets VALUES(
"47b32482e78e48d093579c3f683132e1",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1675430368",
"Abu Dhabi, you guys were just🔥 We had so much fun on stage and the night was just so beautiful✨ Hope to do this all over again soon!",
"47b32482e78e48d093579c3f683132e1.jpg",
"0",
"316",
"62300",
"12600",
"13000000");
INSERT INTO tweets VALUES(
"bccee4843924480eb2d6931306d8fe78",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1675257568",
"#BLACKPINK WORLD TOUR [BORN PINK] AUSTRALIA POSTER",
"bccee4843924480eb2d6931306d8fe78.jpg",
"0",
"485",
"47300",
"8965",
"13000000");
INSERT INTO tweets VALUES(
"e596244e073542c79d35725493086937",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674479968",
"#BLACKPINK 'Shut Down' DANCE PERFORMANCE VIDEO HITS 100 MILLION VIEWS",
"e596244e073542c79d35725493086937.jpg",
"0",
"499",
"63600",
"15600",
"12000000");
INSERT INTO tweets VALUES(
"3f335349141f44a494c316ad9ae221fd",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674134368",
"#BLACKPINK 2nd VINYL LP [BORN PINK] -LIMITED EDITION-
Detail page notice has been uploaded",
"3f335349141f44a494c316ad9ae221fd.jpg",
"0",
"402",
"51000",
"9205",
"17000000");
INSERT INTO tweets VALUES(
"5f7b3fff1dc24e7191bc979469b8b96c",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674047968",
"Three days haven't felt so short! We certainly had a blast with our Hong Kong fans this week🔥
Thank you so much for these unforgettable memories. Love you all!❤️",
"5f7b3fff1dc24e7191bc979469b8b96c.jpg",
"0",
"317",
"78300",
"16800",
"15000000");
INSERT INTO tweets VALUES(
"8d92eace86dc43a38170ce37b1d8be7f",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673875168",
"#BLACKPINK '불장난 (PLAYING WITH FIRE)' M/V HITS 800 MILLION VIEWS",
"8d92eace86dc43a38170ce37b1d8be7f.jpg",
"0",
"408",
"56100",
"14300",
"970100");

INSERT INTO tweets VALUES(
"87b42f1e8a104867b46156b54321d2c8",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673788768",
"HAPPY BIRTHDAY JENNIE 🎉
✅2023.01.16",
"87b42f1e8a104867b46156b54321d2c8.jpg",
"0",
"7730",
"251600",
"101800",
"48000000");
INSERT INTO tweets VALUES(
"cc0613085c4c4cb5936e6fe80ccbee29",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673443168",
"BLACKPINK COACHELLA HEADLINER ANNOUNCEMENT POSTER",
"cc0613085c4c4cb5936e6fe80ccbee29.jpg",
"0",
"2023",
"152700",
"55600",
"48000000");


--11 cat auras tweets
INSERT INTO tweets VALUES(
"d908a55a28e046fabfd3f17c0df4a6dd",
"a3fb674a90c84918968c2425e21e1a4e",
"1676923228",
"Sunny ☀️",
"d908a55a28e046fabfd3f17c0df4a6dd.jpg",
"0",
"72",
"41100",
"3652",
"635400");
INSERT INTO tweets VALUES(
"60e8710079ef4270ab58b2a899f830ea",
"a3fb674a90c84918968c2425e21e1a4e",
"1676908828",
"",
"60e8710079ef4270ab58b2a899f830ea.jpg",
"0",
"106",
"50500",
"7055",
"11000000");
INSERT INTO tweets VALUES(
"369cf2b563854d329454fe4e1cd50180",
"a3fb674a90c84918968c2425e21e1a4e",
"1676883628",
"",
"369cf2b563854d329454fe4e1cd50180.jpg",
"0",
"281",
"135800",
"18200",
"38000000");
INSERT INTO tweets VALUES(
"2e0dcbb08cb640159473613c9c3ea846",
"a3fb674a90c84918968c2425e21e1a4e",
"1676854828",
"",
"2e0dcbb08cb640159473613c9c3ea846.jpg",
"0",
"186",
"133900",
"15700",
"36000000");
INSERT INTO tweets VALUES(
"c292b44280144e4c90c478d4cd918963",
"a3fb674a90c84918968c2425e21e1a4e",
"1676812768",
"",
"c292b44280144e4c90c478d4cd918963.jpg",
"0",
"108",
"136200",
"13400",
"36000000");
INSERT INTO tweets VALUES(
"3f94b2e783d64cbfbf02ca02930c2cb6",
"a3fb674a90c84918968c2425e21e1a4e",
"1676805568",
"",
"3f94b2e783d64cbfbf02ca02930c2cb6.jpg",
"0",
"255",
"173700",
"22800",
"54000000");
INSERT INTO tweets VALUES(
"c1ddc98ab86e4f3dab760ad3de5f2c6c",
"a3fb674a90c84918968c2425e21e1a4e",
"1676719168",
"",
"c1ddc98ab86e4f3dab760ad3de5f2c6c.jpg",
"0",
"449",
"283400",
"44200",
"89000000");
INSERT INTO tweets VALUES(
"2dc09c9d72cf439486e1132a8d5b715c",
"a3fb674a90c84918968c2425e21e1a4e",
"1676546368",
"Hide and seek",
"2dc09c9d72cf439486e1132a8d5b715c.jpg",
"0",
"250",
"133100",
"14700",
"35000000");
INSERT INTO tweets VALUES(
"d6b67fc55de147ae8889f0d6187dcc50",
"a3fb674a90c84918968c2425e21e1a4e",
"1676459968",
"mood",
"d6b67fc55de147ae8889f0d6187dcc50.jpg",
"0",
"666",
"365200",
"61000",
"11000000");
INSERT INTO tweets VALUES(
"1cde54c0b01444f0940c5422ad679381",
"a3fb674a90c84918968c2425e21e1a4e",
"1676287168",
"Me and you 🤍",
"1cde54c0b01444f0940c5422ad679381.jpg",
"0",
"2516",
"312100",
"41300",
"103000000");
INSERT INTO tweets VALUES(
"447ae99181ca45718fffbb2001c3f059",
"a3fb674a90c84918968c2425e21e1a4e",
"1676114368",
"meow",
"",
"0",
"154",
"15300",
"3640",
"12000000");

--##############################################################

DROP TABLE IF EXISTS trends;
CREATE TABLE trends(
  trend_id            TEXT,
  trend_title         TEXT NOT NULL,
  trend_total_tweets  INT DEFAULT 0,
  PRIMARY KEY(trend_id)
) WITHOUT ROWID;
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "Ahri", "17100");
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "#AssassinsCreed", "1380");
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Suicide Squad", "2982");
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Slack", "6869");
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Twitch", "315000");

--##############################################################
-----VIEWS-----

--This view is to get the user and tweets
DROP VIEW IF EXISTS [users_and_tweets];
CREATE VIEW users_and_tweets
AS
SELECT * FROM users
JOIN tweets
ON users.user_id = tweets.tweet_user_fk;

--This view is for follow suggestions so we do not get unnecessary info
DROP VIEW IF EXISTS [follower_suggestions];
CREATE VIEW follower_suggestions
AS
SELECT users.user_id, users.user_name, users.user_full_name, users.user_img_avatar, users.user_verified
FROM users;
 

--##############################################################
----TRIGGERS----
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

--manual testing:
INSERT INTO tweets VALUES(
"21e03682c6c348f09e3729ece60e4e90",
"b3094c2f1c144817b7cc0b718fc3c644",
"1677607833",
"My first tweet",
"",
"0",
"0",
"0",
"0",
"0");

DELETE FROM tweets WHERE tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644"; 