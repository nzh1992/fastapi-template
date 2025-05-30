from datetime import datetime
from sqlalchemy import schema
from sqlalchemy.sql import sqltypes
from app.db.base_class import Base


class AbstractBaseModel(Base):
    __abstract__ = True

    id = schema.Column(sqltypes.Integer, primary_key=True, autoincrement=True)
    create_time = schema.Column(sqltypes.DateTime, default=datetime.now, comment="创建时间")
    update_time = schema.Column(
        sqltypes.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间"
    )


class AbstractDeleteModel:
    __abstract__ = True

    delete_time = schema.Column(sqltypes.DateTime, comment="删除时间")
    is_deleted = schema.Column(
        sqltypes.Boolean, default=False, index=True, comment="是否删除"
    )
