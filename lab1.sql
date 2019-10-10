INSERT INTO osoby (imie, nazwisko, pesel, kontakt)
VALUES ('Adam', 'Kowalski', '87654321', 'tel: 6623');

INSERT INTO osoby (imie, nazwisko, pesel, kontakt)
VALUES ('Jan', 'Nowak', '12345678', 'tel: 2312, dzwonić po 18.00');

select *
from WYCIECZKI_OSOBY;

select *
from WYCIECZKI;
select *
from OSOBY;
select *
from REZERWACJE;


INSERT INTO rezerwacje(id_wycieczki, id_osoby, status)
VALUES (7, 23, 'N');

INSERT INTO rezerwacje(id_wycieczki, id_osoby, status)
VALUES (8, 24, 'P');

CREATE VIEW wycieczki_osoby_potwierdzone
AS
SELECT w.ID_WYCIECZKI,
       w.NAZWA,
       w.KRAJ,
       w.DATA,
       o.IMIE,
       o.NAZWISKO,
       r.STATUS
FROM WYCIECZKI w
         JOIN REZERWACJE r ON w.ID_WYCIECZKI = r.ID_WYCIECZKI
         JOIN OSOBY o ON r.ID_OSOBY = o.ID_OSOBY
WHERE r.STATUS = 'P';

select *
from wycieczki_osoby_potwierdzone;

CREATE VIEW wycieczki_przyszle
AS
SELECT w.ID_WYCIECZKI,
       w.NAZWA,
       w.KRAJ,
       w.DATA,
       o.IMIE,
       o.NAZWISKO,
       r.STATUS
FROM WYCIECZKI w
         JOIN REZERWACJE r ON w.ID_WYCIECZKI = r.ID_WYCIECZKI
         JOIN OSOBY o ON r.ID_OSOBY = o.ID_OSOBY
WHERE w.data > CURRENT_DATE;

select *
from wycieczki_przyszle;

CREATE VIEW wycieczki_miejsca
AS
SELECT w.NAZWA,
       w.KRAJ,
       w.DATA,
       w.LICZBA_MIEJSC,
       w.LICZBA_MIEJSC
           - (select count(*)
              from REZERWACJE
              where REZERWACJE.ID_WYCIECZKI = w.ID_WYCIECZKI
                and status != 'A') as liczba_wolnych_miejsc
FROM WYCIECZKI w;

select *
from wycieczki_miejsca;

CREATE VIEW dostepne_wycieczki
AS
SELECT w.NAZWA,
       w.KRAJ,
       w.DATA,
       w.LICZBA_MIEJSC,
       w.LICZBA_MIEJSC
           - (select count(*)
              from REZERWACJE
              where REZERWACJE.ID_WYCIECZKI = w.ID_WYCIECZKI
                and status != 'A') as liczba_wolnych_miejsc
FROM WYCIECZKI w
where w.DATA > CURRENT_DATE
  and (select count(*)
       from REZERWACJE
       where REZERWACJE.ID_WYCIECZKI = w.ID_WYCIECZKI) > 0;

select *
from dostepne_wycieczki;

CREATE VIEW rezerwacje_do_anulowania
AS
SELECT r.NR_REZERWACJI,
       r.ID_WYCIECZKI,
       r.ID_OSOBY,
       r.STATUS
FROM REZERWACJE r
         join WYCIECZKI w on r.ID_WYCIECZKI = w.ID_WYCIECZKI
where w.DATA - CURRENT_DATE <= 7
  and r.STATUS = 'N';

select * from rezerwacje_do_anulowania;




