from ninja import Schema

from accounts.schemas import UserSchema


class ReviewSchema(Schema):
    reviewer: UserSchema
    review: str