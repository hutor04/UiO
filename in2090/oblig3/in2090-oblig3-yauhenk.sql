-- Oppgave 1
SELECT filmcharacter, num
FROM (SELECT filmcharacter, count(*) as num
      FROM filmcharacter GROUP BY filmcharacter) as FOO
WHERE num > 2000
ORDER BY num DESC;

-- Oppgave 2a
SELECT title, prodyear
FROM film
INNER JOIN filmparticipation
ON filmparticipation.filmid = film.filmid
INNER JOIN person
ON filmparticipation.personid = person.personid
WHERE person.lastname LIKE 'Kubrick' AND person.firstname LIKE 'Stanley' AND filmparticipation.parttype LIKE 'director';

-- Oppgave 2b
SELECT title, prodyear
FROM film
NATURAL JOIN filmparticipation
NATURAL JOIN person
WHERE lastname LIKE 'Kubrick' AND firstname LIKE 'Stanley' AND parttype LIKE 'director';

-- Oppgave 2c
SELECT title, prodyear
FROM film, filmparticipation, person
WHERE filmparticipation.filmid = film.filmid AND
      filmparticipation.personid = person.personid AND
      person.lastname LIKE 'Kubrick' AND
      person.firstname LIKE 'Stanley' AND
      filmparticipation.parttype LIKE 'director';

-- Oppgave 3
SELECT person.personid, CONCAT(person.firstname, ' ', person.lastname) as Fullname, film.title, filmcountry.country
FROM filmcharacter
INNER JOIN filmparticipation
ON filmcharacter.partid = filmparticipation.partid
INNER JOIN person
ON filmparticipation.personid = person.personid
INNER JOIN film
ON filmparticipation.filmid = film.filmid
INNER JOIN filmcountry
ON filmparticipation.filmid = filmcountry.filmid
WHERE filmcharacter.filmcharacter LIKE 'Ingrid' AND person.firstname LIKE 'Ingrid';

-- Oppgave 4
SELECT
DISTINCT ON (film.filmid) film.filmid, film.title, filmgenre.genre,
CASE WHEN filmgenre.genre IS NULL 
            THEN 0 
            ELSE COUNT(*) OVER(PARTITION BY filmgenre.genre) 
    END
AS Count
FROM (film LEFT OUTER JOIN filmgenre ON film.filmid = filmgenre.filmid)
WHERE film.title LIKE '%Antoine %'
GROUP BY film.filmid, film.title, filmgenre.genre;

-- Oppgave 5
SELECT film.title, filmparticipation.parttype, COUNT(filmparticipation.parttype) as num
FROM filmparticipation
INNER JOIN film
ON filmparticipation.filmid = film.filmid
INNER JOIN filmitem
ON filmparticipation.filmid = filmitem.filmid
WHERE film.title LIKE '%Lord of the Rings%' AND filmitem.filmtype LIKE 'C'
GROUP BY film.title, filmparticipation.parttype;

-- Oppgave 6
SELECT film.title, film.prodyear
FROM Film
WHERE film.prodyear = (SELECT MIN(film.prodyear) FROM film);

-- Oppgave 7
SELECT film.title, film.prodyear
FROM film
WHERE film.filmid IN
        (SELECT film.filmid
        FROM film
        INNER JOIN filmgenre
        ON filmgenre.filmid = film.filmid
        WHERE filmgenre.genre LIKE 'Film-Noir')
        AND
        film.filmid IN
        (SELECT film.filmid
        FROM film
        INNER JOIN filmgenre
        ON filmgenre.filmid = film.filmid
        WHERE filmgenre.genre LIKE 'Comedy');

-- Oppgave 8;
SELECT film.title, film.prodyear
FROM Film
WHERE film.prodyear = (SELECT MIN(film.prodyear) FROM film)
UNION
SELECT film.title, film.prodyear
FROM film
WHERE film.filmid IN
        (SELECT film.filmid
        FROM film
        INNER JOIN filmgenre
        ON filmgenre.filmid = film.filmid
        WHERE filmgenre.genre LIKE 'Film-Noir')
        AND
        film.filmid IN
        (SELECT film.filmid
        FROM film
        INNER JOIN filmgenre
        ON filmgenre.filmid = film.filmid
        WHERE filmgenre.genre LIKE 'Comedy');

-- Oppgave 9;
SELECT title, prodyear
FROM film
WHERE film.filmid IN
        (SELECT film.filmid
        FROM film
        NATURAL JOIN filmparticipation
        NATURAL JOIN person
        WHERE lastname LIKE 'Kubrick' AND firstname LIKE 'Stanley' AND parttype LIKE 'director')
        AND
        film.filmid IN
        (SELECT film.filmid
        FROM film
        NATURAL JOIN filmparticipation
        NATURAL JOIN person
        WHERE lastname LIKE 'Kubrick' AND firstname LIKE 'Stanley' AND parttype LIKE 'cast');

-- Oppgave 10;
WITH topseries AS
            (SELECT series.maintitle, filmrating.votes, filmrating.rank
            FROM series
            INNER JOIN filmrating
            ON filmrating.filmid = series.seriesid
            WHERE filmrating.votes > 1000)
SELECT topseries.maintitle
FROM topseries
WHERE topseries.rank = (SELECT MAX(topseries.rank) FROM topseries);

-- Oppgave 11;
SELECT foo.country
FROM 
    (SELECT *, COUNT(*) OVER (PARTITION BY filmcountry.country) as num
    FROM filmcountry
    ) AS foo 
WHERE num = 1;

-- Oppgave 12;
WITH characters AS (SELECT foo.partid, foo.personid
FROM 
    (SELECT DISTINCT ON (filmcharacter.filmcharacter) filmcharacter.partid, filmparticipation.personid,
    COUNT(*) OVER (PARTITION BY filmcharacter.filmcharacter) as num
    FROM filmcharacter
    INNER JOIN filmparticipation
    ON filmparticipation.partid = filmcharacter.partid
    ) AS foo 
WHERE num = 1)
SELECT *
FROM (SELECT person.firstname, person.lastname
    FROM characters
    INNER JOIN person
    ON characters.personid = person.personid
    GROUP BY person.firstname, person.lastname HAVING COUNT(*) > 199
    ) AS foo;

-- Oppgave 13;
WITH caseone AS (SELECT DISTINCT ON (personid) personid, COUNT (personid) as num
FROM filmparticipation
WHERE filmid IN (
                SELECT filmid
                FROM filmrating
                WHERE votes > 60000 AND rank >= 8
)
AND parttype LIKE 'director'
GROUP BY personid),
casetwo AS (SELECT DISTINCT ON (personid) personid, COUNT (personid) as num
FROM filmparticipation
WHERE filmid IN (
                SELECT filmid
                FROM filmrating
                WHERE votes > 60000
)
AND parttype LIKE 'director'
GROUP BY personid)
SELECT firstname, lastname
FROM person
INNER JOIN caseone
ON caseone.personid = person.personid
INNER JOIN casetwo
ON casetwo.personid = person.personid
WHERE caseone.num = casetwo.num;






