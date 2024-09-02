import strawberry
from typing import List, Optional
from app.db.session import SessionLocal
from app.entities.field import Field
from app.graphql.types.field import FieldType

@strawberry.type
class FieldQuery:
    @strawberry.field
    def fields(self) -> List[FieldType]:
        with SessionLocal() as db:
            fields = db.query(Field).all()
            return [FieldType(id=field.id, name=field.name, location=field.location, created_at=field.created_at) for field in fields]

    @strawberry.field
    def field(self, id: int) -> Optional[FieldType]:
        with SessionLocal() as db:
            field = db.query(Field).filter(Field.id == id).first()
            if field:
                return FieldType(id=field.id, name=field.name, location=field.location, created_at=field.created_at)
            return None
