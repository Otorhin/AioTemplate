from tortoise import fields, Model


class User(Model):
    id = fields.BigIntField(pk=True)

    class Meta:
        table = "users"
