import strawberry
from strawberry.fastapi import GraphQLRouter

from app.graphql.queries import Query  # queries/__init__.py をインポート
from app.graphql.mutations import Mutation  # mutations/__init__.py をインポート

schema = strawberry.Schema(query=Query, mutation=Mutation)
graphql_app = GraphQLRouter(schema)
