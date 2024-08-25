import strawberry
from strawberry.fastapi import GraphQLRouter

# queries
from app.graphql.queries.relay_status import RelayStatusQuery
from app.graphql.queries.temperature import TemperatureQuery

# mutations
from app.graphql.mutations.relay import RelayStatusMutation

@strawberry.type
class Query(RelayStatusQuery, TemperatureQuery):
    pass

@strawberry.type
class Mutation(RelayStatusMutation):
    pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
