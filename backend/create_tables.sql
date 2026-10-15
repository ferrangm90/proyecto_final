CREATE TABLE "comment" (
	"id"	INTEGER,
	"id_omdb"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"comment"	TEXT NOT NULL,
    "fecha"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);

CREATE TABLE "calificacion" (
	"id"	INTEGER,
	"id_omdb"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"calificacion"	INTEGER NOT NULL,
	"fecha"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);