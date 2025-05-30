from sqlalchemy import orm, schema
from sqlalchemy.sql import sqltypes
from app import models
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base_class import Base


class User(models.AbstractBaseModel, models.AbstractDeleteModel):
    """
    用户
    """

    email = schema.Column(sqltypes.String(255), index=True, comment="邮箱")
    password = schema.Column(sqltypes.String(255), comment="密码")
    is_active = schema.Column(sqltypes.Boolean, default=False, index=True, comment="是否激活")