create table irispipeline (
	id serial,
	sepal_length numeric (5,2),
	sepal_width numeric (5,2),
	petal_length numeric (5,2),
	petal_width numeric (5,2),
	species varchar (225),
	PRIMARY KEY (id)
)

-- drop table irispipeline

select * from irispipeline

SELECT * FROM irispipeline
LIMIT 5; 

SELECT * FROM irispipeline ORDER BY id DESC LIMIT 5