import strawberry

from app.graphql.mutations.field import FieldMutation
from app.graphql.mutations.relay import RelayMutation
from app.graphql.mutations.automation_schedule import RelayScheduleMutation

# 複数のミューテーションをまとめてインポート
@strawberry.type
class Mutation(FieldMutation, RelayMutation, RelayScheduleMutation):
    pass
