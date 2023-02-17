DROP TABLE IF EXISTS tweets;


CREATE TABLE tweets(
  id                TEXT,
  user_fk           TEXT,
  created_at        TEXT,
  message           TEXT,
  image             TEXT,
  updated_at        TEXT,
  total_replies     TEXT,
  total_likes       TEXT,
  total_retweets    TEXT,
  total_views       TEXT,

  PRIMARY KEY(id)
  ) WITHOUT ROWID;

INSERT INTO tweets VALUES(
"9a1e4f0a4c9c4468a47b0d69936524d4",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676283575",
"My first tweet",
"",
"0",
"0",
"0",
"0",
"0");