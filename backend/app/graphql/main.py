# app/graphql/main.py
import strawberry
from strawberry.fastapi import GraphQLRouter

# queries
from app.graphql.queries.relay_status import RelayStatusQuery
from app.graphql.queries.temperature import TemperatureQuery
from app.graphql.queries.relay_schedule import ScheduleQuery

# mutations
from app.graphql.mutations.relay_status import RelayStatusMutation

@strawberry.type
class Query(RelayStatusQuery, ScheduleQuery, TemperatureQuery):
    pass

@strawberry.type
class Mutation(RelayStatusMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)



