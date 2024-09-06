import strawberry
from typing import Optional
from sqlalchemy import inspect
from app.db.session import engine

@strawberry.type
class ColumnInfo:
    name: str
    type: str
    nullable: bool
    default: Optional[str]

@strawberry.type
class TableInfo:
    name: str
    columns: list[ColumnInfo]

@strawberry.type
class ResolversQuery:
    @strawberry.field
    def get_table_structure(self) -> list[TableInfo]:
        inspector = inspect(engine)
        tables = []
        for table_name in inspector.get_table_names():
            columns = []
            for column in inspector.get_columns(table_name):
                col_info = ColumnInfo(
                    name=column['name'],
                    type=str(column['type']),
                    nullable=column['nullable'],
                    default=str(column['default']) if column['default'] is not None else None
                )
                columns.append(col_info)
            tables.append(TableInfo(name=table_name, columns=columns))
        return tables
