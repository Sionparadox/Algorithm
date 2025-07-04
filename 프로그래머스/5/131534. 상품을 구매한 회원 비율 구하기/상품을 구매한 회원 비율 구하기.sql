# WITH TOTAL_USER as (
#     SELECT COUNT(*) as TOT
#     FROM USER_INFO
#     WHERE YEAR(JOINED) = 2021
# )


# SELECT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, COUNT(DISTINCT(os.USER_ID)) as PURCHASED_USERS, ROUND(COUNT(DISTINCT(os.USER_ID)) / tu.TOT, 1) as PUCHASED_RATIO
# FROM ONLINE_SALE os
# JOIN USER_INFO ui
# ON os.USER_ID = ui.USER_ID
# CROSS JOIN TOTAL_USER tu
# WHERE YEAR(JOINED) = 2021
# GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
# ORDER BY 1,2

WITH TOTAL_USER as (
    SELECT COUNT(*) as TOT
    FROM USER_INFO
    WHERE YEAR(JOINED) = 2021
)

SELECT YEAR(SALES_DATE) as YEAR, MONTH(SALES_DATE) as MONTH, COUNT(DISTINCT(os.USER_ID)) as PURCHASED_USERS, ROUND(COUNT(DISTINCT(os.USER_ID))/ tu.TOT, 1) as PUCHASED_RATIO
FROM ONLINE_SALE os
JOIN USER_INFO ui
ON os.USER_ID = ui.USER_ID
CROSS JOIN TOTAL_USER tu
WHERE YEAR(JOINED) = 2021
GROUP BY YEAR(SALES_DATE), MONTH(SALES_DATE)
ORDER BY 1,2