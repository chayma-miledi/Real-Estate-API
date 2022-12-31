from marshmallow import Schema, fields

#Rename ItemSchema to PlainItemSchema
class PlainItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)



class PlainStoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)

#we have PlainStoreSchema and PlainItemSchema so that when we use
#nesting, we can only include a part of the fields and not these nested fields.

class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()
    store_id = fields.Int() #added



class ItemSchema(PlainItemSchema):
    store_id = fields.Int(required=True, load_only=True)
    store = fields.Nested(PlainStoreSchema(), dump_only=True)
    #And this here will only be used when returning data to the client and 
    #not when receiving data from them

class StoreSchema(PlainStoreSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)



