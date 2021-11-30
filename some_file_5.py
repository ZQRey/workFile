import json

# user = [
#     {
#         'username': 'john',
#         'pass': '123123'
#     },
#     {
#         'username': 'lila',
#         'pass': 'stich'
#     },
#
# ]

class User:
    def __init__(self, name, pswd):
        self.username = name
        self.pswd = pswd

    def to_json(self):
        return {'username': self.username, 'pswd': self.pswd}

    @classmethod
    def from_json(cls, js_object):
        return cls(js_object['username'], js_object['pswd'])

    def __repr__(self):
        return 'User({!r}, {!r}'.format(self.username, self.pswd)

user = [User('John', '123213'), User('Lila', 'Stich')]

with open('data/some_text_4.json', 'w') as data:
    json.dump(user, data, indent=2, default=User.to_json)

with open('data/some_text_4.json') as data:
    user = json.load(data, object_hook=User.from_json)

print(user)