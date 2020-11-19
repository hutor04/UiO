-- Oppgave 1

--Tog(togNr, startStasjon, endeStasjon, ankomstTid)
--TogTabell(togNr, avgangsTid, stasjon)
--Plass(dato, togNr, vognNr, plassNr, vindu, ledig)

-- togNr is integer, they are typically integers.
-- Station names are max 30 characters, that must saffice for long names if any
-- we simultaneously exclude invalid inputs.
-- Time and Date are in ordinary formats.
-- Car number, seat number are integers, as they typically are.
-- Window seat, and Free seat are encoded with Boolean, since the values are naturally binary.
-- All the fields are restricted to be NOT NULL, again based on common sense considerations,
-- since all of them must be specified.

CREATE SCHEMA TOGBASE;

CREATE TABLE TOGBASE.Tog(
    togNr INTEGER PRIMARY KEY,
    startStasjon VARCHAR(30) NOT NULL,
    endeStasjon  VARCHAR(30) NOT NULL,
    ankomstTid TIME NOT NULL
);

CREATE TABLE TOGBASE.TogTabell(
    togNr INTEGER NOT NULL REFERENCES TOGBASE.Tog (togNr),
    avgangsTid TIME NOT NULL,
    stasjon VARCHAR(30) NOT NULL,
    PRIMARY KEY (togNr, avgangsTid)
);

CREATE TABLE TOGBASE.Plass(
    dato DATE,
    togNr INTEGER NOT NULL REFERENCES TOGBASE.Tog (togNr),
    vognNr INTEGER NOT NULL,
    plassNr INTEGER NOT NULL,
    vindu BOOLEAN NOT NULL,
    ledig BOOLEAN NOT NULL,
    PRIMARY KEY (dato, togNr, vognNr, plassNr)
);

-- Testing Insertions
INSERT INTO TOGBASE.Tog (togNr, startStasjon, endeStasjon, ankomstTid)
VALUES (1, 'Example Start', 'Example End', '23:15:00');

INSERT INTO TOGBASE.TogTabell (togNr, avgangsTid, stasjon)
VALUES (1, '15:00:00', 'Hauketo');

INSERT INTO TOGBASE.Plass (dato, togNr, vognNr, plassNr, vindu, ledig)
VALUES ('10/28/2019', 1, 2, 15, 'True', 'True');

-- Oppgave 2
-- a) Hvilke kandidatnøkler har R?

-- Not on the right side: C, F
-- Attributes that are always on the right side: G
-- X = ACF, C+ = ABCDEFG
-- X = BCF, C+ = ABCDEFG
-- X = CFDE, C+ = ABCDEFG

-- Result:
-- Candidate keys are: ACF, BCF, CFDE

-- b) Finn den høyeste normalformen som R tilfredsstiller.
-- BCNF:
-- R is not in BCNF, because, for example, in FD CDE -> B, CDE is not a candidate key.

-- 3NF:
-- D -> G is non-tivial FD, D is not a candidate key, G is not part of some key
-- in R. Thus R is not in 3NF.

-- 2NF:
-- Non-prime attributes: G
-- CDE -> B is non-trivial FD, CDE is subset of CFDE, B is prime attribute.
-- Thus R is not in 3NF

-- Result:
-- R is in 1NF.


-- c) Dekomponer R tapsfritt til BCNF. Start dekomposisjonen ved å ta

-- Step 1: R(A,B,C,D,E,F,G), CDE -> B violates BCNF.
-- Y = CDE, Y+ = CDEBAG, S1(Y+) = S1(A,B,C,D,E,G), S2(Y,X/Y+) = S2(C,D,E,F)
-- S2(C,D,E,F) is OK

-- Step 2: Continue with R(A,B,C,D,E,G), CDE -> B, B -> A, D -> G
-- B -> A violates BCNF
-- Y = B, Y+ = BA, S1(A,B), S2(B,C,D,E,G)
-- S1(A, B) with B -> A is OK

-- Step 3: R(B,C,D,E,G), CDE -> B, D -> G
-- D -> G violates BCNF
-- Y = D, Y+ = DG, S1(D,G), S2(C,D,E,B)
-- S1(D, G) with D -> G is OK
-- S2(C,D,E,B) with CDE -> B is OK

-- Result
-- R1(C,D,E,F})
-- R2(A,B), B -> A
-- R3(D,G), D -> G
-- R4(B,C,D,E), CDE -> B