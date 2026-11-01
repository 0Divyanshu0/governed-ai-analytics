"""Exploratory SQL syntax gate. NOT an execution authorization control.

A complete authorization policy will require scoped schema/column resolution,
proven joins, function allowlisting, and independent PostgreSQL read-only grants.
"""

import sqlglot
from sqlglot import exp


class QueryRejected(ValueError):
    """The submitted SQL does not pass the prototype syntax gate."""


def check_query_shape(sql: str) -> None:
    """Reject anything except a simple single SELECT at the AST root.

    Does not authorize execution. Callers MUST NOT treat success as database
    permission or a guarantee that referenced data is safe to access.
    """
    try:
        statements = sqlglot.parse(sql, read="postgres")
    except sqlglot.errors.ParseError as exc:
        raise QueryRejected("Invalid SQL") from exc

    if len(statements) != 1 or not isinstance(statements[0], exp.Select):
        raise QueryRejected("Expected exactly one SELECT statement")

    statement = statements[0]
    if statement.find(exp.Insert, exp.Update, exp.Delete, exp.Create, exp.Drop, exp.Command):
        raise QueryRejected("Mutating or unsupported SQL")
