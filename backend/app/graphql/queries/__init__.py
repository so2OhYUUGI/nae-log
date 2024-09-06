import strawberry

from app.graphql.queries.temperature import TemperatureQuery
from app.graphql.queries.automation_schedule import ScheduleQuery
from app.graphql.queries.field import FieldQuery
from app.graphql.queries.relay import RelayQuery
from app.graphql.queries.resolvers import ResolversQuery

# 複数のクエリをまとめてインポート
@strawberry.type
class Query(ScheduleQuery, TemperatureQuery, ResolversQuery, FieldQuery, RelayQuery):
    pass
