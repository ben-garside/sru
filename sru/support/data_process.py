import json
import logging

log = logging.getLogger(__name__)

def jsonify(data, **kwargs):
    try:
        if len(kwargs.keys()) > 0:
            data.update(kwargs)
        return json.dumps(data)
    except Exception as e:
        log.error("Error: {}".format(str(e)))
        return None

def encode(data, encode="utf-8", json=False, **kwargs):
    if json:
        output = jsonify(data, **kwargs).encode("utf-8")
    else:
        output = data.encode("utf-8")
    return output