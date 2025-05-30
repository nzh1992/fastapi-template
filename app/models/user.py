from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app import models
from app.db import Base


class User(models.AbstractBaseModel, models.AbstractDeleteModel):
    """
    用户
    """
    __tablename__ = "user"
    __table_args__ = {'comment': '用户表'}

    username = Column(String, unique=True, index=True, comment="用户名")
    hashed_password = Column(String, comment="哈希密码")
    email = Column(String, unique=True, index=True, comment="邮箱")
    is_active = Column(Integer, default=1, comment="是否激活 1激活 0禁用")
    is_admin = Column(Integer, default=0, comment="是否管理员 1管理员 0普通用户")

    # orders = relationship("Order", back_populates="user")