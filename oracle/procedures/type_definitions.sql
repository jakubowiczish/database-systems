CREATE OR REPLACE TYPE osoby_wycieczki_type AS OBJECT
(
    imie              varchar(50),
    nazwisko          varchar(50),
    "nazwa wycieczki" varchar(200),
    "data wycieczki"  date,
    kraj              varchar(50),
    status            char(1)
);

CREATE OR REPLACE TYPE osoby_wycieczki_table IS TABLE OF osoby_wycieczki_type;


CREATE OR REPLACE TYPE wycieczki_type AS OBJECT
(
    "id wycieczki"    number,
    "nazwa wycieczki" varchar2(100),
    kraj              varchar2(50),
    opis              varchar2(200),
    "liczba miejsc"   number,
    "data"            date
);

CREATE OR REPLACE TYPE wycieczki_table IS TABLE OF wycieczki_type;
