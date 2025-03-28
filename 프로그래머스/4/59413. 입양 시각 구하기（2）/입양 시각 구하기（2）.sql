WITH RECURSIVE TIME AS (
    SELECT 0 AS HOUR
    
    UNION ALL
    SELECT HOUR + 1
    FROM TIME
    WHERE HOUR<23
)

SELECT t.HOUR, COALESCE(a.COUNT, 0) as COUNT
FROM TIME t
LEFT JOIN (SELECT DATE_FORMAT(DATETIME, '%H') as HOUR, COUNT(ANIMAL_ID) as COUNT
           FROM ANIMAL_OUTS
           GROUP BY DATE_FORMAT(DATETIME, '%H')) a
ON t.HOUR = a.HOUR
ORDER BY 1;