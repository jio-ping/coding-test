--131697 mysql&oracle
SELECT max(price) max_price
from product

--59415
SELECT max(datetime) 시간
from animal_ins

--59038
SELECT min(datetime) 시간
from animal_ins

--59406
SELECT count(animal_id)
from animal_ins

--59408
SELECT count(distinct name)
from animal_ins

--131115
select * from
(SELECT product_id, product_name, product_cd, category, price
from food_product
order by price desc )
where rownum = 1;