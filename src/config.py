import os


APP_CONFIG = {
    "MONGO_URI": os.getenv("MONGO_URI", "mongodb://localhost:27017"),
    "DB_NAME": os.getenv("DB_NAME", "csgi_test"),
}


CELERY_CONFIG = {
    "broker": os.getenv("CELERY_BROKER_URL", "pyamqp://guest@localhost//"),
    "backend": os.getenv("CELERY_RESULT_BACKEND", "mongodb://localhost:27017"),
}
