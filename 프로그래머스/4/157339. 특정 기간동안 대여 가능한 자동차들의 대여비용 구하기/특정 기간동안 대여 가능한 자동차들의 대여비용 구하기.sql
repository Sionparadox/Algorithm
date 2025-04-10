SELECT c.CAR_ID, CAR_TYPE, FEE
FROM (SELECT CAR_ID, car.CAR_TYPE, FLOOR(DAILY_FEE * (1- DISCOUNT_RATE/100) * 30) AS FEE
      FROM CAR_RENTAL_COMPANY_CAR car
      JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN dis
      ON car.CAR_TYPE = dis.CAR_TYPE
      WHERE car.CAR_TYPE IN ('세단', 'SUV') 
      AND dis.DURATION_TYPE = '30일 이상'
     ) c
WHERE c.CAR_ID NOT IN (
    SELECT DISTINCT(CAR_ID) 
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE >= DATE('2022-11-1') AND START_DATE <= DATE('2022-11-30')
    )
AND FEE BETWEEN 500000 AND 2000000
ORDER BY FEE desc, CAR_TYPE asc, CAR_ID desc;

# SELECT DISTINCT(CAR_ID) 
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE END_DATE < DATE('2022-11-1') || START_DATE > DATE('2022-11-30')
# ORDER BY 1;

# SELECT *
# FROM CAR_RENTAL_COMPANY_CAR

# SELECT c.CAR_ID, c.CAR_TYPE
# FROM CAR_RENTAL_COMPANY_CAR c
# JOIN (
#     SELECT DISTINCT(CAR_ID) 
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE END_DATE < DATE('2022-11-1') || START_DATE > DATE('2022-11-30')
#     ) t
# ON t.CAR_ID = c.CAR_ID
# WHERE CAR_TYPE IN ('세단', 'SUV')