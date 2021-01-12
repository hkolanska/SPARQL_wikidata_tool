from typing import List

from wikidata_connection.query import Query


class GroupByQuery(Query):
    select: List[str]
    count: str
    where: List[str]
    order_by: str
    limit: int
