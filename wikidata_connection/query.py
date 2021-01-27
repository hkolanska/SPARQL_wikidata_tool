from typing import List, Optional, Set
from SPARQLWrapper import SPARQLWrapper, JSON
import abc


class Query:
    __metaclass__ = abc.ABCMeta
    results: Optional[List[List[str]]]
    query: str
    head: Optional[Set]

    def __init__(self):
        self.results = None
        self.query = ""
        return

    @abc.abstractmethod
    def create_query(self):
        return

    def run_query(self):
        sparql = SPARQLWrapper(
            "https://query.wikidata.org/bigdata/namespace/wdq/sparql}")
        sparql.setQuery(self.query)
        sparql.setReturnFormat(JSON)
        raw_results = sparql.query().convert()
        self.head = raw_results["head"]["vars"]
        self.results = [[row[key]["value"] for key in self.head]
                        for row in raw_results["results"]["bindings"]]