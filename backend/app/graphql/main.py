# app/graphql/main.py
import strawberry
from strawberry.fastapi import GraphQLRouter

# queries
from app.graphql.queries.relay_status import RelayStatusQuery
from app.graphql.queries.temperature import TemperatureQuery
from app.graphql.queries.relay_schedule import ScheduleQuery
from app.graphql.queries.field import FieldQuery

from app.graphql.queries.resolvers import ResolversQuery
from app.graphql.mutations.field import FieldMutation

# mutations
from app.graphql.mutations.relay_status import RelayStatusMutation

@strawberry.type
class Query(RelayStatusQuery, ScheduleQuery, TemperatureQuery, ResolversQuery, FieldQuery):
    pass

@strawberry.type
class Mutation(RelayStatusMutation, FieldMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)