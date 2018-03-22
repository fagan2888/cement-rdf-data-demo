# Cement production data as an RDF data cube

This is an exploration of how to represent data tables using the [RDF Data
Cube](https://www.w3.org/TR/vocab-data-cube/) vocabulary.

The data is based on the [Mineral Products Association cement "channel of sale"
statistics](http://cement.mineralproducts.org/downloads/industry_statistics.php).
The data is reproduced in the `sales.csv` file in this repo.

Steps:
1. Transform the data to long format `sales_long.csv`:

   `make sales_long.csv`
   
2. Transform the data into RDF (Turtle format) using
   [rdf-tabular](https://github.com/ruby-rdf/rdf-tabular). The `parse.rb` file
   in this repo is just taken from there -- I guess I don't know enough Ruby to
   install it properly.
   
   `make sales_long.ttl`

The RDF data is produced based on the specification in
`sales_long.csv-metadata.json`.
