-- Import this table dump: metal_bands.sql.zip
-- Column names must be: origin and nb_fans
-- Your script can be executed on any database
SELECT origin,
	SUM(fans) as nb_fans
FROM metal_bands
group by origin
order by nb_fans DESC;
