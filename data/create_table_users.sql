DROP TABLE IF EXISTS users;

CREATE TABLE users(
  id                TEXT,
  username          TEXT,
  fullname          TEXT,
  avatar_img        TEXT,
  cover_img         TEXT,
  verified          TEXT,
  bio_text          TEXT,
  bio_location      TEXT,
  bio_link          TEXT,
  bio_birthday      TEXT,
  bio_created_at    TEXT,
  total_followers   TEXT,
  total_following   TEXT,
  total_tweets      TEXT,
  PRIMARY KEY(id)
  ) WITHOUT ROWID;



INSERT INTO users VALUES("5ae1823bcc5648bd9e5bf6602ae397d6", "elonmusk", "Elon Musk", "5ae1823bcc5648bd9e5bf6602ae397d6.jpg", "ad3b5a9a8fe3471d814ff845b9671cc0.jpg", True, "", "", "", "", "1243814400", "128900000", "177", "22900");
INSERT INTO users VALUES("63bfa35aa8204270a6480557fddf9069", "shakira", "Shakira", "63bfa35aa8204270a6480557fddf9069.jpg", "76a574041471471bb7a806ed197198aa.jpg", True, "MONOTONÍA YA DISPONIBLE", "Barranquilla", "linktr.ee/shakira", "November 30, 1998", "1246406399", "537000000", "235", "8002");
INSERT INTO users VALUES("96e7977bdaab4f0abe84e7ac18a864ec", "BLACKPINK", "BLACKPINKOFFICIAL", "96e7977bdaab4f0abe84e7ac18a864ec.jpg", "0684090441a743e6ba92eb42b4ee8816.jpg", True, "BLΛƆKPIИK", "", "lnk.to/YG_BLACKPINK", "", "1590969600", "8500000", "0", "892");
INSERT INTO users VALUES("a3fb674a90c84918968c2425e21e1a4e", "cat_auras", "cat with confusing auras.", "a3fb674a90c84918968c2425e21e1a4e.jpg", "0f0cb4cb07424f1ea0d0e87705cb1745.jpg", True, "Even cat can confuse “us”. | dm for credit or removal.", "", "catauras.com", "", "1654041600", "1600000", "15", "167");