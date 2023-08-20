--MANUAL TESTING--

--Delete tweet
DELETE FROM tweets WHERE tweet_id = "e5cef902955441d1b897aa55f6632a77"; 

--Delete a user
DELETE FROM users WHERE user_id = "1d1b0b166b3e4d75a3f6477f072ecc22"; 

--Delete all user's tweets
DELETE FROM tweets WHERE tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644"; 

--Get tweet id to delete images
SELECT * FROM tweets WHERE tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644";

SELECT tweet_images.tweet_image_url 
FROM tweet_images 
INNER JOIN tweets ON tweet_images.tweet_image_tweet_fk = tweets.tweet_id 
WHERE tweets.tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644";

--Delete all tweets images
DELETE FROM tweet_images WHERE tweet_image_tweet_fk = "be7e9821630b425cae04a45138161d61"; 

DELETE FROM tweet_images WHERE tweet_image_url = "e2c697b11a284f82987357c1a7cd1485.jpg"; 

DELETE FROM users WHERE user_id = "fc462863f59f49518a5f722f44a73e65";

DELETE FROM tweets WHERE tweet_user_fk = "b3094c2f1c144817b7cc0b718fc3c644";

--Update user
UPDATE users
SET user_account_status = "active"
WHERE user_name = "my_name_cleo";

--Update user
UPDATE users
SET user_password = "Pw12345678"
WHERE user_name = "cat_auras";

--following
DELETE FROM following WHERE follower_fk = ""; 


--See user and user's tweets
SELECT * FROM tweets
JOIN users ON users.user_id = tweets.tweet_user_fk
JOIN tweet_images ON tweets.tweet_id = tweet_images.tweet_images_tweet_fk
WHERE users.user_name = "my_name_cleo";

--cleo image tweets
--2 images
INSERT INTO tweets VALUES(
"930afbfbac414b0b86ba12e729851e9e",
"d6517288b0a04e298c69646b10bb6d45",
"b3094c2f1c144817b7cc0b718fc3c644",
"1684791456",
"0",
"2 images",
"0",
"0",
"0",
"0",
"0",
"",
"default");
--3 images
INSERT INTO tweets VALUES(
"ea7619edbb3c45baaabadae28284ccd7",
"7dca2077157f4f6a87cd161f39699202",
"b3094c2f1c144817b7cc0b718fc3c644",
"1684791447",
"0",
"3 images",
"0",
"0",
"0",
"0",
"0",
"",
"default");
--4 images
INSERT INTO tweets VALUES(
"c448657ea0c147ae8fe96e52259ae4f1",
"ac0d55a60cf1423fb2379b3fd3c7ac76",
"b3094c2f1c144817b7cc0b718fc3c644",
"1684775108",
"0",
"4 images",
"0",
"0",
"0",
"0",
"0",
"",
"default");

--TWEET IMAGES TEST--
--2 images
--cleo img 1
INSERT INTO tweet_images VALUES(
"97b6dda4bc6a4385a11aee583eea2bfb",
"930afbfbac414b0b86ba12e729851e9e",
"fdb40744451c42b9b9b2a7783c74d612.jpg",
0,
"1684791456"
);
--cleo img 2
INSERT INTO tweet_images VALUES(
"3891efbc4b624ae4953af7ee4b34f912",
"930afbfbac414b0b86ba12e729851e9e",
"afe45385e58142b8ad97352dcbf2357b.jpg",
1,
"1684791456"
);

--3 images
--cleo img 1
INSERT INTO tweet_images VALUES(
"8198acaeced34d74a36e4e0c1dafeb25",
"ea7619edbb3c45baaabadae28284ccd7",
"a95f2d8bc71d49f683cf0454e353313c.jpg",
0,
"1684791447"
);
--cleo img 2
INSERT INTO tweet_images VALUES(
"f5c2e26f6272468293aac3f124646ac4",
"ea7619edbb3c45baaabadae28284ccd7",
"f1b3379a3ae8464b9c17d0c2f3036563.jpg",
1,
"1684791447"
);
--cleo img 3
INSERT INTO tweet_images VALUES(
"b7e2861999034a6082969ff894201759",
"ea7619edbb3c45baaabadae28284ccd7",
"616987ec6c1249abb9e77b340870c0ae.jpg",
2,
"1684791447"
);
--4 images
--cleo img 1
INSERT INTO tweet_images VALUES(
"9ee51d54b2a543398ca60d39bee836c8",
"c448657ea0c147ae8fe96e52259ae4f1",
"904ec11f3ee54c38a4db0fb1083ba98f.jpg",
0,
"1684775108"
);
--cleo img 2
INSERT INTO tweet_images VALUES(
"ad2e4fafd91a4fdd85218a52375f429c",
"c448657ea0c147ae8fe96e52259ae4f1",
"857061796b524905992dad4262b85409.jpg",
1,
"1684775108"
);
--cleo img 3
INSERT INTO tweet_images VALUES(
"7a6b1ecc22e542dbb01494032ea333bc",
"c448657ea0c147ae8fe96e52259ae4f1",
"80c60357741d4aa59600eaf1d5b949e6.jpg",
2,
"1684775108"
);
--cleo img 4
INSERT INTO tweet_images VALUES(
"d7f1eb1390bb4c4da5d2146d00b2937f",
"c448657ea0c147ae8fe96e52259ae4f1",
"cb6d0e1e2b03493c95ebf63dc4c6d7d8.jpg",
3,
"1684775108"
);