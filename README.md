# Querying Wikiata using Python
## Abstract
The project aimed to create an application, which can generate a SPARQL query from user input, run it on the wikidata's endpoint and show its results.

## Implementation
The project was implemented in Python with libraries: Tkinter for GUI and SPARQLWrapper for running queries. 

### Query
Application is based on (and extend) query: 
```
SELECT DISTINCT ?country ?countryLabel
{ 
 ?country wdt:P31 wd:Q3624078 .
SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } 
 } 
ORDER BY DESC(?countryLabel) 
```
It is possible to extend this query by adding more parameters to select, more where clauses, limitation of results, and changing order by's parameter. 
The options to choose from are in the file
[to_choice.py](https://github.com/hkolanska/SPARQL_wikidata_tool/blob/main/wikidata_connection_to_choice.py).
This file also contains translation wikidata's objects and relations to more user-friendly names.

One of the complicated queries created by the app:
```
SELECT DISTINCT ?country ?countryLabel ?population ?life_expectancy ?GDB ?capitalLabel
{ 
 ?country wdt:P31 wd:Q3624078 .
?country wdt:P1082 ?population .
?country wdt:P2250 ?life_expectancy .
?country wdt:P2131 ?GDB .
?country wdt:P36 ?capital .
?country wdt:P463 wd:Q1065 .
?country wdt:P463 wd:Q458 .
?country wdt:P463 wd:Q7184 .
?country wdt:P30 wd:Q46 .
SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } 
 } 
ORDER BY DESC(?population) 
LIMIT 5 
```
It was created by choosing the following parameters:

![alt text](https://github.com/hkolanska/SPARQL_wikidata_tool/raw/main/ReadmeImages/complex_query.png "Complex query")

### GUI
GUI was made using tkinter. The file consisting GUI code is in a directory [GUI](https://github.com/hkolanska/SPARQL_wikidata_tool/blob/main/GUI).

##Example usage
### Creating query
To start the application, run the file [app.py](https://github.com/hkolanska/SPARQL_wikidata_tool/blob/main/app.py).
 Then the create query view will be shown. There can be selected options extending basic query.

![alt text](https://github.com/hkolanska/SPARQL_wikidata_tool/raw/main/ReadmeImages/create_querry_view.png "Create")

After filling the form and pressing "RUN" button, the results will be displayed.
![alt text](https://github.com/hkolanska/SPARQL_wikidata_tool/raw/main/ReadmeImages/results_view.png "Results")


## Authors
[@hkolanska](https://github.com/hkolanska)
[@patrycjabru](https://github.com/patrycjabru)


