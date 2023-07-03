--USERS--
INSERT INTO users VALUES("5ae1823bcc5648bd9e5bf6602ae397d6", "elonmusk", "1243814400", "1243814400", "9f15c5de3a1e4611839c703a0c5f1d12", False, "blue", "active", "elonmusk@mail.com", "", "Elon Musk", "1971-06-28", "elonmuskpass", "5ae1823bcc5648bd9e5bf6602ae397d6.jpg", "ad3b5a9a8fe3471d814ff845b9671cc0.jpg", "", "", "", False, "22900", "177", "128900000");
INSERT INTO users VALUES("96e7977bdaab4f0abe84e7ac18a864ec", "BLACKPINK", "1590969600", "1590969600", "f09e8a21ca874b388146c4be4783d7e6", False, "blue", "active", "blackpink@mail.com", "", "BLACKPINKOFFICIAL", "1995-01-03", "blackpinkpass", "96e7977bdaab4f0abe84e7ac18a864ec.jpg", "0684090441a743e6ba92eb42b4ee8816.jpg", "BLΛƆKPIИK", "", "lnk.to/YG_BLACKPINK", False, "892", "0", "8500000");
INSERT INTO users VALUES("a3fb674a90c84918968c2425e21e1a4e", "cat_auras", "1654041600", "1654041600", "d6cf3f0560a04bc1a49193c9f81f0ae3", False, "blue", "active", "cat_auras@mail.com", "", "cat with confusing auras.", "1999-10-02", "cat_auraspass", "a3fb674a90c84918968c2425e21e1a4e.jpg", "0f0cb4cb07424f1ea0d0e87705cb1745.jpg", "Even cat can confuse “us”. | dm for credit or removal.", "", "catauras.com", False, "167", "15", "1600000");
INSERT INTO users VALUES("b3094c2f1c144817b7cc0b718fc3c644", "my_name_cleo", "1677605053", "1677605053", "032d3d3b0fb24dc186d9f27c59340ed1", False, "basic", "active", "my_name_cleo@mail.com", "", "Cleo", "1998-11-30", "Pw12345678", "b3094c2f1c144817b7cc0b718fc3c644.jpg", "8e89394382ca44d2bb3cc45d067c2a7e.jpg", "I am a happy doge", "", "https://www.instagram.com/my_name_cleo/", False, "0", "0", "126");


--TRENDS--
INSERT INTO trends VALUES("882f3de5c2e5450eaf6e59c14be1db70", "Ahri", "17100");
INSERT INTO trends VALUES("7a90e16350074cf7a15fba48113c4046", "#AssassinsCreed", "1380");
INSERT INTO trends VALUES("43ace034564c42788169ac18aaf601f5", "Suicide Squad", "2982");
INSERT INTO trends VALUES("2a9470bc61314187b19d7190b76cd535", "Slack", "6869");
INSERT INTO trends VALUES("c9773e2bb68647039a7a40c2ee7d4716", "Twitch", "315000");

--TRIGGER SO TWEET IMAGE NO GETS UPDATED
DROP TRIGGER IF EXISTS update_tweet_images;
CREATE TRIGGER update_tweet_images AFTER INSERT ON tweet_images
BEGIN 
    UPDATE tweets
    SET tweet_field_images = tweet_field_images + 1
    WHERE tweet_id = NEW.tweet_image_tweet_fk;
END;

--TWEETS--
  --11 elon musk tweets
INSERT INTO tweets VALUES(
"500151d40e26414f82b9aca854c5a059",
"34c69b02ab0b4fa284ba18c5585b336c",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676834368",
"0",
"",
"0",
"65786",
"237100",
"16400",
"",
"default"
);
INSERT INTO tweets VALUES(
"3c417a8c92d244dc80e7b2c2a5def367",
"d3ccf6b6bfdc47f1ac643f6055273a7e",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676819968",
"0",
"All things in moderation, 
especially content moderation",
"0",
"10000",
"85700",
"8082",
"",
"default");
INSERT INTO tweets VALUES(
"4d2db7af8d02411b831bcb0064de19ca",
"1e9a875c71eb4b9dac167899b93d2ede",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676812768",
"0",
"BingChatGPT reminds me of Lucky in Waiting for Godot",
"0",
"4125",
"63000",
"4301",
"",
"default");
INSERT INTO tweets VALUES(
"1b45faeadfb046f4a90c0c151b86ca6a",
"8b55960f5f4a4c53a6652767d718dff7",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676798368",
"0",
"",
"0",
"14600",
"461400",
"31500",
"",
"default");
INSERT INTO tweets VALUES(
"4b88a9d72171459ca1b4690d1a8c3792",
"c40d9884221d4305b8b37b003d77914b",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676719168",
"0",
"Surround your house with treadmills set to jogging speed to stop walking dead ur welcome",
"0",
"17300",
"462500",
"36800",
"",
"default");
INSERT INTO tweets VALUES(
"58838f22d6be43ffae7d73585d5e2b76",
"3fd14b169c0045d6a83714a942653438",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676704768",
"0",
"Interesting",
"0",
"10800",
"173700",
"17800",
"",
"default");
INSERT INTO tweets VALUES(
"b7d54f24ac224981b41d33c68fc54323",
"0ba0f3e6ab9b48e4ae87139683a1ae26",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676701168",
"0",
"",
"0",
"5991",
"120600",
"8351",
"",
"default");
INSERT INTO tweets VALUES(
"5bd98366765342579e9d15cc4b71b6a8",
"5053e2ce9f034d259d9631972407e24a",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676629168",
"0",
"Note: if many people who you follow or like also follow me, it is highly probable that the algorithm will recommend my tweets. It’s not super sophisticated.

In coming months, we will offer the ability to adjust the algorithm to closer match what is most compelling to you.",
"0",
"10400",
"161800",
"11500",
"",
"default");
INSERT INTO tweets VALUES(
"5e7c131e977646b491c8e06d7852c12d",
"f9dc8faf012447538e746b15f6505986",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676625568",
"0",
"What we need is TruthGPT",
"0",
"21300",
"297300",
"29600",
"",
"default");
INSERT INTO tweets VALUES(
"6de4cffad29d4b23a7e30e7f6688bfbd",
"79081b8132214ccfbd0c8e7c5c1dbf74",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676621968",
"0",
"Sorry for showing you so many irrelevant & annoying ads on Twitter! 

We're taking the (obvious) corrective action of tying ads to keywords & topics in tweets, like Google does with search.

This will improve contextual relevance dramatically.",
"0",
"7720",
"126700",
"8218",
"",
"default");
INSERT INTO tweets VALUES(
"d14d81bdc33d4953b0acec2867a899c7",
"f449a2d763a4429ab482890e80836beb",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676607568",
"0",
"ChatGPT to the mainstream media",
"0",
"9747",
"325300",
"26900",
"",
"default");
INSERT INTO tweets VALUES(
"b66b072968e84e98b67d342e4c92a5ef",
"9ae200950eed41668221be7e09a3f6f6",
"5ae1823bcc5648bd9e5bf6602ae397d6",
"1676467168",
"0",
"He's great with numbers!",
"0",
"14900",
"614200",
"40100",
"",
"default");

--11 blackpink tweets
INSERT INTO tweets VALUES(
"9a8280289f5547369e7cddbeb1a9aded",
"c65f96169a9443039293059acab30a77",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1676647168",
"0",
"BLACKPINK TOUR MERCH RESTOCK",
"0",
"603",
"33300",
"4497",
"",
"default");
INSERT INTO tweets VALUES(
"8b0fbf87efbb4e478a27c804e54b3cb3",
"7b195f2e8a774e678e291a11b988493b",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1676639968",
"0",
"BLACKPINK [BORN PINK] VINYL",
"0",
"703",
"26900",
"4100",
"",
"default");
INSERT INTO tweets VALUES(
"47b32482e78e48d093579c3f683132e1",
"f31dff6daae04b099e2c3379deff6630",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1675430368",
"0",
"Abu Dhabi, you guys were just🔥 We had so much fun on stage and the night was just so beautiful✨ Hope to do this all over again soon!",
"0",
"316",
"62300",
"12600",
"",
"default");
INSERT INTO tweets VALUES(
"bccee4843924480eb2d6931306d8fe78",
"04c9877d60a14428a19fb0c704948164",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1675257568",
"0",
"#BLACKPINK WORLD TOUR [BORN PINK] AUSTRALIA POSTER",
"0",
"485",
"47300",
"8965",
"",
"default");
INSERT INTO tweets VALUES(
"e596244e073542c79d35725493086937",
"a3168493f54d4ca0a326605d727238a3",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674479968",
"0",
"#BLACKPINK 'Shut Down' DANCE PERFORMANCE VIDEO HITS 100 MILLION VIEWS",
"0",
"499",
"63600",
"15600",
"",
"default");
INSERT INTO tweets VALUES(
"3f335349141f44a494c316ad9ae221fd",
"1cf710237b954724b69351a6de5312b2",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674134368",
"0",
"#BLACKPINK 2nd VINYL LP [BORN PINK] -LIMITED EDITION-
Detail page notice has been uploaded",
"0",
"402",
"51000",
"9205",
"",
"default");
INSERT INTO tweets VALUES(
"5f7b3fff1dc24e7191bc979469b8b96c",
"cc4a63b54c034ac5b535b33fb08d027d",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1674047968",
"0",
"Three days haven't felt so short! We certainly had a blast with our Hong Kong fans this week🔥
Thank you so much for these unforgettable memories. Love you all!❤️",
"0",
"317",
"78300",
"16800",
"",
"default");
INSERT INTO tweets VALUES(
"8d92eace86dc43a38170ce37b1d8be7f",
"bbc8ea69dc494af9b46dc1f1f7916c20",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673875168",
"0",
"#BLACKPINK '불장난 (PLAYING WITH FIRE)' M/V HITS 800 MILLION VIEWS",
"0",
"408",
"56100",
"14300",
"",
"default");

INSERT INTO tweets VALUES(
"87b42f1e8a104867b46156b54321d2c8",
"05e5136aa078412199a43781f151a4a6",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673788768",
"0",
"HAPPY BIRTHDAY JENNIE 🎉
✅2023.01.16",
"0",
"7730",
"251600",
"101800",
"",
"default");
INSERT INTO tweets VALUES(
"cc0613085c4c4cb5936e6fe80ccbee29",
"c7506a8a76f84a839f4610cd6fc7a382",
"96e7977bdaab4f0abe84e7ac18a864ec",
"1673443168",
"0",
"BLACKPINK COACHELLA HEADLINER ANNOUNCEMENT POSTER",
"0",
"2023",
"152700",
"55600",
"",
"default");


--11 cat auras tweets
INSERT INTO tweets VALUES(
"d908a55a28e046fabfd3f17c0df4a6dd",
"71bd7c490d6e4f48890229f10a9b6943",
"a3fb674a90c84918968c2425e21e1a4e",
"1676923228",
"0",
"Sunny ☀️",
"0",
"72",
"41100",
"3652",
"",
"default");
INSERT INTO tweets VALUES(
"60e8710079ef4270ab58b2a899f830ea",
"fdb0b26ac05f4a88bf42a5562538cb75",
"a3fb674a90c84918968c2425e21e1a4e",
"1676908828",
"0",
"",
"0",
"106",
"50500",
"7055",
"",
"default");
INSERT INTO tweets VALUES(
"369cf2b563854d329454fe4e1cd50180",
"c73209b449384a79aef88ba66977cf21",
"a3fb674a90c84918968c2425e21e1a4e",
"1676883628",
"0",
"",
"0",
"281",
"135800",
"18200",
"",
"default");
INSERT INTO tweets VALUES(
"2e0dcbb08cb640159473613c9c3ea846",
"673c758ca8014fc281525960d41f20ba",
"a3fb674a90c84918968c2425e21e1a4e",
"1676854828",
"0",
"",
"0",
"186",
"133900",
"15700",
"",
"default");
INSERT INTO tweets VALUES(
"c292b44280144e4c90c478d4cd918963",
"9fc97e2bc24148ca86d7bb4481e3649b",
"a3fb674a90c84918968c2425e21e1a4e",
"1676812768",
"0",
"",
"0",
"108",
"136200",
"13400",
"",
"default");
INSERT INTO tweets VALUES(
"3f94b2e783d64cbfbf02ca02930c2cb6",
"162b6aa2f25e4307b4fb6ae2256ea341",
"a3fb674a90c84918968c2425e21e1a4e",
"1676805568",
"0",
"",
"0",
"255",
"173700",
"22800",
"",
"default");
INSERT INTO tweets VALUES(
"c1ddc98ab86e4f3dab760ad3de5f2c6c",
"806075ece35c463bb5b8b641e04e8e30",
"a3fb674a90c84918968c2425e21e1a4e",
"1676719168",
"0",
"",
"0",
"449",
"283400",
"44200",
"",
"default");
INSERT INTO tweets VALUES(
"2dc09c9d72cf439486e1132a8d5b715c",
"1a3e86ed53b444ed9865ba63944e918d",
"a3fb674a90c84918968c2425e21e1a4e",
"1676546368",
"0",
"Hide and seek",
"0",
"250",
"133100",
"14700",
"",
"default");
INSERT INTO tweets VALUES(
"d6b67fc55de147ae8889f0d6187dcc50",
"34970bc478b54cb387885239134385df",
"a3fb674a90c84918968c2425e21e1a4e",
"1676459968",
"0",
"mood",
"0",
"666",
"365200",
"61000",
"",
"default");
INSERT INTO tweets VALUES(
"1cde54c0b01444f0940c5422ad679381",
"b9fb231255e74670b0dc08b595e17636",
"a3fb674a90c84918968c2425e21e1a4e",
"1676287168",
"0",
"Me and you 🤍",
"0",
"2516",
"312100",
"41300",
"",
"default");
INSERT INTO tweets VALUES(
"447ae99181ca45718fffbb2001c3f059",
"6f5f256f71884f4fb5656b84097f02fb",
"a3fb674a90c84918968c2425e21e1a4e",
"1676114368",
"0",
"meow",
"0",
"154",
"15300",
"3640",
"",
"default");

PRAGMA foreign_keys = ON;
--TWEETS IMAGES--
INSERT INTO tweet_images VALUES(
"eb7415d6efec4f6d8099cb6de949218c",
"500151d40e26414f82b9aca854c5a059",
"00b087641d6e4c8b955564a6c8c3bb86.jpg",
0,
"1676834368"
);
INSERT INTO tweet_images VALUES(
"3ed6be65e1464998a92c7a4dda011810",
"3c417a8c92d244dc80e7b2c2a5def367",
"ea9cedd1220342dc8d4f9d76e823b958.jpg",
0,
"1676819968"
);
INSERT INTO tweet_images VALUES(
"02217f4997544b77aaf7c6266ee5f295",
"1b45faeadfb046f4a90c0c151b86ca6a",
"de2351efcc294e2d8796d5d8cf2a7631.jpg",
0,
"1676798368"
);
INSERT INTO tweet_images VALUES(
"4dbb5c61880e4203ad408faf88b799c0",
"4b88a9d72171459ca1b4690d1a8c3792",
"0f8ee582f1a24f3397191c564ef83393.jpg",
0,
"1676719168"
);
INSERT INTO tweet_images VALUES(
"fe2e1d53ec1e41a79e34d0fa0001bf5c",
"58838f22d6be43ffae7d73585d5e2b76",
"d00e6595f9bc47558c45f30bd34a66d0.jpg",
0,
"1676704768"
);
INSERT INTO tweet_images VALUES(
"a7fc853fb9ca4adb81167798ed82c8ac",
"b7d54f24ac224981b41d33c68fc54323",
"9323fd150fd84cf9991f38017db33d4d.jpg",
0,
"1676701168"
);
INSERT INTO tweet_images VALUES(
"3e940b31d75c49aea51d5262224a02e3",
"d14d81bdc33d4953b0acec2867a899c7",
"94df910b1d774b6bae0bbd314f6be012.jpg",
0,
"1676607568"
);
INSERT INTO tweet_images VALUES(
"05f88adc4282407ba9aa01cbd89216df",
"b66b072968e84e98b67d342e4c92a5ef",
"94c438d98f2940cc8f8e711f4227458d.jpg",
0,
"1676467168"
);
INSERT INTO tweet_images VALUES(
"87739451b3d74a0cb649767a9cbec705",
"9a8280289f5547369e7cddbeb1a9aded",
"6d3eafc75f684c6cabf316e30a694733.jpg",
0,
"1676647168"
);
INSERT INTO tweet_images VALUES(
"f3acdbb231e54dec8209a0022016b39d",
"8b0fbf87efbb4e478a27c804e54b3cb3",
"1bb6806142544c56a0a852bde5ad72fb.jpg",
0,
"1676639968"
);
INSERT INTO tweet_images VALUES(
"bd836c5ea82640bc8f2069bfeecfdc34",
"47b32482e78e48d093579c3f683132e1",
"0a4fe639da1f4ee9a6663b3f58587a35.jpg",
0,
"1675430368"
);
INSERT INTO tweet_images VALUES(
"247fdd9df15f4f28b33e3686aee5cf44",
"bccee4843924480eb2d6931306d8fe78",
"d638319190bb438889ed0937c9165ec8.jpg",
0,
"1675257568"
);
INSERT INTO tweet_images VALUES(
"d42f2144fe9146ed8162490a3917515c",
"e596244e073542c79d35725493086937",
"0982cc95f1c94dd89424bd6b82adaeec.jpg",
0,
"1674479968"
);
INSERT INTO tweet_images VALUES(
"429c60a2bafa431da6f841194c1bb985",
"3f335349141f44a494c316ad9ae221fd",
"2509765d56a1433a899e9085c0a9cd6d.jpg",
0,
"1674134368"
);
INSERT INTO tweet_images VALUES(
"7c5f72b7884c446eb50a329b9576f70a",
"5f7b3fff1dc24e7191bc979469b8b96c",
"839bb1e244794a5da287905f8f99f2ea.jpg",
0,
"1674047968"
);
INSERT INTO tweet_images VALUES(
"1ddc77565dde4220b6a37b04a33c2b1a",
"8d92eace86dc43a38170ce37b1d8be7f",
"063da388b0354d8b916e55790a2bf0e3.jpg",
0,
"1673875168"
);
INSERT INTO tweet_images VALUES(
"5e2d89d78c0347638bed142c4d5cd3e3",
"87b42f1e8a104867b46156b54321d2c8",
"a1197371a154438aaa6b9ba095fd375c.jpg",
0,
"1673788768"
);
INSERT INTO tweet_images VALUES(
"ba76e4eccf0b4f89b590f59eb09a8244",
"cc0613085c4c4cb5936e6fe80ccbee29",
"a56d6f7687614a2687ec0a572f164a06.jpg",
0,
"1673443168"
);
INSERT INTO tweet_images VALUES(
"17d6d7a333c24b32a86dd0096e2cf0ea",
"d908a55a28e046fabfd3f17c0df4a6dd",
"5b479f72b43942e9b90e76f3a56a9cb8.jpg",
0,
"1676923228"
);
INSERT INTO tweet_images VALUES(
"363a6b6d449a47cab61894b4567e12d0",
"60e8710079ef4270ab58b2a899f830ea",
"e7f9793f47fe4f3987f9421076c1e8a7.jpg",
0,
"1676908828"
);
INSERT INTO tweet_images VALUES(
"d0c4752d90df41d49ceb4fb9c71acded",
"369cf2b563854d329454fe4e1cd50180",
"2c18896c071c413ba7b5a486db486507.jpg",
0,
"1676883628"
);
INSERT INTO tweet_images VALUES(
"1329d13d91d545baafd34b4f91fbf65d",
"2e0dcbb08cb640159473613c9c3ea846",
"492a20d2d41a460cbeca455d46222aaf.jpg",
0,
"1676854828"
);
INSERT INTO tweet_images VALUES(
"add97f677d5249238ec869ba150f9abe",
"c292b44280144e4c90c478d4cd918963",
"54ebc81108b3499cb34eea26d2a9f8f6.jpg",
0,
"1676812768"
);
INSERT INTO tweet_images VALUES(
"ca56c655b80243889aaa96c21e37c854",
"3f94b2e783d64cbfbf02ca02930c2cb6",
"742a5ff48cd44923b44368555aaa4823.jpg",
0,
"1676805568"
);
INSERT INTO tweet_images VALUES(
"038e37218527449d9a9948cf5fcb03c2",
"c1ddc98ab86e4f3dab760ad3de5f2c6c",
"7d0fc49cfd724209a963d4295c948f1b.jpg",
0,
"1676719168"
);
INSERT INTO tweet_images VALUES(
"fa140188016e42ebb155933d7771889d",
"2dc09c9d72cf439486e1132a8d5b715c",
"5b5a30b53450494eb9c888a448e081a1.jpg",
0,
"1676546368"
);
INSERT INTO tweet_images VALUES(
"80fcc0a646a74d7d837c6813838c372a",
"d6b67fc55de147ae8889f0d6187dcc50",
"c562c04d276e4c6f83a3e541f84687a7.jpg",
0,
"1676459968"
);
INSERT INTO tweet_images VALUES(
"1412e4f80fbf42d1817178f808e42e20",
"1cde54c0b01444f0940c5422ad679381",
"3d4392e7dbe144ed8bb7756c1eb729f9.jpg",
0,
"1676287168"
);

