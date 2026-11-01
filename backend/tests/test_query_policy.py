import pytest
from app.security.query_policy import check_query_shape, QueryRejected


def test_simple_select_shape():
    check_query_shape("SELECT 1")


@pytest.mark.parametrize("query", [
    "DELETE FROM orders",
    "DROP TABLE orders",
    "SELECT 1; DELETE FROM orders",
    "WITH t AS (DELETE FROM orders RETURNING *) SELECT * FROM t",
])
def test_rejects_unsupported_sql(query):
    with pytest.raises(QueryRejected):
        check_query_shape(query)
