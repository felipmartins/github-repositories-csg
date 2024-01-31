import os


APP_CONFIG = {
    "MONGO_URI": os.getenv("MONGO_URI", "mongodb://localhost:27017"),
    "DB_NAME": os.getenv("DB_NAME", "csgi_test"),
}
