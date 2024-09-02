# app/graphql/main.py
import strawberry
from strawberry.fastapi import GraphQLRouter

####################################################################
# queries
from app.graphql.queries.temperature import TemperatureQuery
from app.graphql.queries.relay_schedule import ScheduleQuery
from app.graphql.queries.field import FieldQuery
from app.graphql.queries.relay import RelayQuery

from app.graphql.queries.resolvers import ResolversQuery

####################################################################
# mutations
from app.graphql.mutations.field import FieldMutation
from app.graphql.mutations.relay import RelayMutation

@strawberry.type
class Query(ScheduleQuery, TemperatureQuery, ResolversQuery, FieldQuery, RelayQuery):
    pass

@strawberry.type
class Mutation(FieldMutation, RelayMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)