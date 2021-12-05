-- 1.4.27

CREATE TABLE "user" (
	id SERIAL NOT NULL, 
	name VARCHAR, 
	email VARCHAR, 
	PRIMARY KEY (id)
)

;
CREATE USER readonly WITH PASSWORD 'readonly';
GRANT SELECT ON public.user TO readonly;
