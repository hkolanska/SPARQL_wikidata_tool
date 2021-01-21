from typing import List, Optional

from wikidata_connection.query import Query
from wikidata_connection.enums import select_possibilities,where_possibilities

class SimpleQuery(Query):
    select: List[str]
    where: List[str]
    order_by: Optional[str]
    limit: Optional[int]

    def __init__(self, select_values,where_values, order_by=0, limit=None):
        super().__init__()
        self.select = ["?country", "?countryLabel"]
        self.where = [" ?country wdt:P31 wd:Q3624078 ."]
        for number in select_values:
            self.select.append(select_possibilities[number])
            self.where.append((where_possibilities[number]))
        for number in where_values:
            self.where.append((where_possibilities[number]))
        self.order_by = select_possibilities[order_by]
        self.limit = limit

    def create_query(self):
        self.query = "SELECT DISTINCT"
        for element in self.select:
            self.query += f" {element}"
        self.query += "\n{ \n"
        for element in self.where:
            self.query += f"{element}\n"
        self.query += "SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } \n } \n"
        self.query += f"ORDER BY {self.order_by} \n" if self.order_by else ""
        self.query += f"LIMIT {self.limit} \n" if self.limit else ""