-- Oppgave 1
SELECT filmcharacter, num
FROM (SELECT filmcharacter, count(*) as num
      FROM filmcharacter GROUP BY filmcharacter) as FOO
WHERE num > 2000;