from apscheduler.schedulers.background import BackgroundScheduler

# スケジューラのインスタンスを作成
scheduler = BackgroundScheduler()
scheduler.start()
job_id = "relay_job"
