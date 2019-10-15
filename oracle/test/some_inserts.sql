INSERT INTO osoby (imie, nazwisko, pesel, kontakt)
VALUES ('Marcin', 'Kowalski', '12345678', '123456789');

INSERT INTO rezerwacje(id_wycieczki, id_osoby, status)
VALUES (9, 41, 'P');

INSERT INTO wycieczki (nazwa, kraj, data, opis, liczba_miejsc)
VALUES ('Bochnia', 'Polska', TO_DATE('2017-03-04', 'YYYY-MM-DD'), 'Kopalnia soli', 10);