--133026
SELECT ingredient_type, sum(total_order) total_order
from first_half inner join icecream_info
on first_half.flavor = icecream_info.flavor
group by ingredient_type

--59040
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID)
FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE 

--59041
SELECT NAME,COUNT(ANIMAL_ID)
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >=2
ORDER BY NAME

--56788
--MYSQL
SELECT 
substring(datetime,12,2) as hour,
count(*)
from animal_outs
where substring(datetime,12,2)  between 9 and 19
group by hour
order by hour