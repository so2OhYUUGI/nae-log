import strawberry

from app.graphql.mutations.field import FieldMutation
from app.graphql.mutations.relay import RelayMutation

# 複数のミューテーションをまとめてインポート
@strawberry.type
class Mutation(FieldMutation, RelayMutation):
    pass
