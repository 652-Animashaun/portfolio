from marshmallow import Schema, fields, INCLUDE
from pprint import pprint
import datetime as dt



# class ArtistSchema(Schema):
#     name = fields.Str()


class BlogSchema(Schema):
    content_type = fields.Str(read_only=True)
    title = fields.Str()
    description = fields.Str()
    body = fields.Str()
    author = fields.Str()
    _id = fields.Str(dump_only=True)
    published = fields.DateTime()
    last_revision = fields.DateTime()
    class Meta:
        unknown = INCLUDE

class PortfolioSchema(Schema):
    content_type = fields.Str(read_only=True)
    project_name = fields.Str()
    description = fields.Str()
    link = fields.Str()
    _id = fields.Str(dump_only=True)
    tags = fields.List(fields.Str())
    class Meta:
        unknown = INCLUDE


    # artist = fields.Nested(ArtistSchema())

# class ContentSchema(Schema):
#   content_type = fields.Str()
#   content = fields.Nested(ArtistSchema())
