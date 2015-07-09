
import json


class Jsonable(object):
    def to_json(self):
        return json.dumps(vars(self))
