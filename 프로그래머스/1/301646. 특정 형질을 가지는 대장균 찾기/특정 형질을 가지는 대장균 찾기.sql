SELECT COUNT(ID) as COUNT
FROM ECOLI_DATA
WHERE GENOTYPE & 2 = 0 and (GENOTYPE & 1 = 1 or GENOTYPE & 4 = 4);
