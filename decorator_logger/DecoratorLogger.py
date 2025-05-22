import logging
import time
from functools import wraps
from pathlib import Path

# 로그 디렉토리 생성
log_dir = Path("./logs")
log_dir.mkdir(exist_ok=True)

app_logger = logging.getLogger("app")
app_logger.setLevel(logging.INFO)
app_handler = logging.FileHandler(log_dir / "app.log", mode="a")
app_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
app_logger.addHandler(app_handler)


def return_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        app_logger.info(f"함수 '{func.__name__}' 리턴값: {result}")
        return result

    return wrapper


def time_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        app_logger.info(f"함수 '{func.__name__}' 실행시간: {execution_time}")
        return result

    return wrapper


def error_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)  # 함수 실행
        except Exception as e:
            result = str(e)
        app_logger.info(f"함수 '{func.__name__}' 리턴값: {result}")
        return result

    return wrapper
