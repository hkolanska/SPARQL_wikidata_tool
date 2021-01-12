from typing import List

from wikidata_connection.query import  Query



class SingleCountQuery(Query):
    select: List[str]
    count: str
    where: List[str]
    order_by: str
    limit: int

    def __init__(self):
        super().__init__()
        self.select = ["?country", "?countryLabel"]
        self.where = [" ?country wdt:P31 wd:Q3624078 ."]

    def create_query(self):
        query = "SELECT DISTINCT"
        for element in self.select:
            query += f" {element}"
        query += "\n{ \n"
        for element in self.where:
            query += f"{element}\n"
        query += "SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } \n } \n"
