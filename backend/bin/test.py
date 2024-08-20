from crontab import CronTab
from datetime import datetime, timedelta

# Crontabのインスタンスを作成
cron = CronTab(user=True)

# 現在時刻を取得
now = datetime.now()

# 10秒後の時刻を計算
run_time = now + timedelta(minutes=1)

# 時刻の各要素を取得
minute = run_time.minute
hour = run_time.hour

# 新しいジョブを作成
job = cron.new(command='/home/so2/nae-log/.venv/bin/python3 /home/so2/nae-log/backend/bin/test-relay.py', comment='Test Relay Job')

# 時刻を設定 (10秒後の次の分に設定)
job.minute.on(minute)
job.hour.on(hour)

# 一度だけ実行するよう設定
job.setall(f'{minute} {hour} * * *')

# Crontabを更新して保存
cron.write()

print(f"Job scheduled to run at {run_time.strftime('%Y-%m-%d %H:%M:%S')}")
