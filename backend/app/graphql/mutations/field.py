import strawberry
from app.db.session import SessionLocal
from app.entities.field import Field, FieldType, FieldInput

@strawberry.type
class FieldMutation:
    @strawberry.mutation
    def create_field(self, input: FieldInput) -> FieldType:
        with SessionLocal() as db:
            field = Field(name=input.name, location=input.location)
            db.add(field)
            db.commit()
            db.refresh(field)
            return FieldType(id=field.id, name=field.name, location=field.location, created_at=field.created_at)

    @strawberry.mutation
    def update_field(self, id: int, input: FieldInput) -> FieldType:
        with SessionLocal() as db:
            field = db.query(Field).filter(Field.id == id).first()
            if field:
                field.name = input.name
                field.location = input.location
                db.commit()
                db.refresh(field)
                return FieldType(id=field.id, name=field.name, location=field.location, created_at=field.created_at)
            raise ValueError(f"Field with id {id} not found.")
