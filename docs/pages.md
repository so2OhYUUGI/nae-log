画面遷移図 (Mermaid)

```mermaid
graph TD
    A[トップ] --> B[ホーム]
    
    B --> C[照明管理]
    B --> D[温度 / 湿度記録]
    B --> E[カメラ]
    B --> F[設定 / プロフィール]
    B --> G[ヘルプ]

    C --> B
    D --> B
    E --> B
    F --> B
    G --> B
```


