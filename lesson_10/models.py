import mongoengine as me

me.connect('Users_august')

class User(me.Document):
    first_name = me.StringField(min_length=1, max_length=256)
    surname = me.StringField(min_length=1, max_length=256)
    age = me.IntField(min_value=9, max_value=99)
    interests = me.ListField(me.StringField())

obj = User(first_name='Valera', surname='Gorets', age=29, interests=['Sport', 'Music', 'Reading'])

obj.save()