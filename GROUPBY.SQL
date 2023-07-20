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