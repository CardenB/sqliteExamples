BEGIN TRANSACTION;
CREATE TABLE cars(Id INT, Name TEXT, Price INT);
INSERT INTO "cars" VALUES(1,'Audi',62300);
INSERT INTO "cars" VALUES(2,'Mercedes',57127);
INSERT INTO "cars" VALUES(5,'Bentley',350000);
INSERT INTO "cars" VALUES(6,'Hummer',41400);
COMMIT;