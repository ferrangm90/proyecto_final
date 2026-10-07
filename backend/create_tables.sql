CREATE TABLE "comment" (
	"id"	INTEGER,
	"id_omdb"	TEXT NOT NULL,
	"nombre"	TEXT NOT NULL,
	"comentario"	TEXT NOT NULL,
    "fecha"	TEXT NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);