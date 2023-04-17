DROP TABLE IF EXISTS posts;
CREATE VIRTUAL TABLE posts 
USING FTS5(title, body);

INSERT INTO posts(title,body)

VALUES('We are trying this database','We hope this works'),
('Send a text message','We do it via fiotext'),
('Macs are great','Windows are even better');

--SELECT * FROM posts;
SELECT * 
FROM posts 
WHERE posts MATCH 'are NOT trying';