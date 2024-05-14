from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

# User model
class User(db.Model):

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sa.String(64), index=True, unique=True)
    email: orm.Mapped[str] = orm.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: orm.Mapped[Optional[str]] = orm.mapped_column(sa.String(128))

    # String representation
    def __repr__(self) -> str:
        return f'<User {self.username}>'
    
# Post model
class Post(db.Model):

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    body: orm.Mapped[str] = orm.mapped_column(sa.String(140))
    timestamp: orm.Mapped[datetime] = orm.mapped_column(sa.DateTime, index=True, default=lambda: datetime.now(timezone.utc))
    user_id: orm.Mapped[int] = orm.mapped_column(sa.ForeignKey('user.id'), index=True)
    author: orm.Mapped[User] = orm.relationship('User', back_populates='posts')

    # String representation
    def __repr__(self) -> str:
        return f'<Post {self.body}>'
