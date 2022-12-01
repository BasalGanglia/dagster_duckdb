class SQL:
    def __init__(self, sql, **bindings) -> None:
        self.sql = sql
        self.bindings = bindings
