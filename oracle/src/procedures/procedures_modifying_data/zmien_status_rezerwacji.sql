CREATE OR REPLACE PROCEDURE zmien_status_rezerwacji(id_rezerwacji_param NUMBER, new_status CHAR) AS
    old_status CHAR(1);
    counter    INTEGER;
BEGIN
    SELECT COUNT(*)
    INTO counter
    FROM WYCIECZKI_PRZYSZLE wp
             JOIN REZERWACJE r ON r.ID_WYCIECZKI = wp.ID_WYCIECZKI
    WHERE r.NR_REZERWACJI = id_rezerwacji_param;

    IF counter = 0 THEN
        raise_application_error(-20015,
                                'Nie mozna zmienic statusu rezerwacji dla wycieczek, ktore nie sa w przyszlosci');
    END IF;

    SELECT COUNT(*)
    INTO counter
    FROM REZERWACJE r
    WHERE r.NR_REZERWACJI = id_rezerwacji_param;

    IF counter = 0 THEN
        raise_application_error(-20016,
                                'Nie istnieje rezerwacja o podanym numerze');
    END IF;

    SELECT STATUS
    INTO old_status
    FROM REZERWACJE
    WHERE NR_REZERWACJI = id_rezerwacji_param;

    CASE
        WHEN old_status IS NULL
            THEN
                raise_application_error(-20016,
                                        'Nie istnieje rezerwacja o podanym numerze');

        WHEN old_status = 'A'
            THEN
                SELECT COUNT(*)
                INTO counter
                FROM DOSTEPNE_WYCIECZKI_VIEW v
                         JOIN REZERWACJE r on R.ID_WYCIECZKI = v.ID_WYCIECZKI
                WHERE r.NR_REZERWACJI = id_rezerwacji_param;

                IF counter = 0 THEN
                    raise_application_error(-20018,
                                            'Nie ma wystarczajacej ilosci miejsc, aby przywrocic anulowana rezerwacje o podanym id');
                END IF;

        WHEN new_status = 'N'
            THEN raise_application_error(-20017,
                                         'Rezerwacja, ktora juz istnieje nie moze zmienic statusu na nowa. Podano bledny argument');

        ELSE NULL;
        END CASE;

    UPDATE REZERWACJE
    SET STATUS = new_status
    WHERE NR_REZERWACJI = id_rezerwacji_param;
END;