sales_long.csv: sales.csv
	python prepare_csv.py

sales_long.ttl: sales_long.csv
	ruby parse.rb sales_long.csv > sales_long.ttl
