SELECT * FROM UCZESTNICY_WYCIECZKI(7);
SELECT * FROM REZERWACJE_OSOBY(23);

SELECT * FROM DOSTEPNE_WYCIECZKI_FUNCTION('POLSKA', CURRENT_DATE, CURRENT_DATE + 190000)

BEGIN
    DODAJ_REZERWACJE(8, 41);
END;

select UCZESTNICY_WYCIECZKI(7) from dual;

select REZERWACJE_OSOBY(23) from dual;

select PRZYSZLE_REZERWACJE_OSOBY(24) from dual;

begin
    ZMIEN_STATUS_REZERWACJI(23, 'Z');
end;

begin
    ZMIEN_LICZBE_MIEJSC(7, 10);
end;

begin
    DODAJ_REZERWACJE2(41, 23);
end;