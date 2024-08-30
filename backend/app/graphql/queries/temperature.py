import strawberry

@strawberry.type
class TemperatureQuery:
    @strawberry.field
    def temperature(self) -> float:
        # ここでセンサーから温度データを取得
        return 24.5  # 仮の値です