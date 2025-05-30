from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool

from app.core.config import get_settings


# 获取配置信息
settings = get_settings()

# sqlalchemy配置
engine_setting = {
    "url": str(settings.SQLALCHEMY_DATABASE_URI),
    "pool_pre_ping": True,                  # 启用连接活性检查
    "echo": False,                          # 执行SQL时，输出到控制台
    "echo_pool": False,                     # 输出连接池的操作日志
    "poolclass": QueuePool,                 # 连接池类型
    "pool_size": 20,                        # 连接池数量
    "pool_recycle": 3600,                   # 连接池回收连接时间(秒)
    "pool_timeout": 60,                     # 放弃从连接池中获取连接之前等待的秒数
    "max_overflow": 100,                    # 允许溢出数量
    "pool_reset_on_return": "rollback",     # 控制连接归还到连接池时，是否自动执行重置操作
}

# 配置映射到引擎
engine = create_engine(**engine_setting)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """
    获取数据库会话
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()