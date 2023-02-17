DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  name              TEXT,
  last_name         TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  avatar            TEXT,
  verified          TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;



INSERT INTO users VALUES("5ae1823bcc5648bd9e5bf6602ae397d6", "elonmusk", "Elon", "Musk", "128900000", "177", "22700", "5ae1823bcc5648bd9e5bf6602ae397d6.jpg", True);
INSERT INTO users VALUES("63bfa35aa8204270a6480557fddf9069", "shakira", "Shakira", "", "537000000", "235", "7999", "63bfa35aa8204270a6480557fddf9069.jpg", True);
INSERT INTO users VALUES("5af69f7e5f6544248bb45f5cf0a99a9e", "rihanna", "Rihanna", "", "107900000", "980", "10600", "5af69f7e5f6544248bb45f5cf0a99a9e.jpg", True);