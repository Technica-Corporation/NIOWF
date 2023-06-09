import os
import string
import random
import base64
import binascii
import json
from datetime import date, datetime


def file_write(data, path, filename):
    os.makedirs(path, exist_ok=True)
    if data:
        with open('{}/{}.json'.format(path, filename), 'w+') as outfile:
            outfile.write(data)
        outfile.close()


def json_serializer(obj: {}):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    # failure fallback
    if not isinstance(obj, str):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)


def bin2ascii(v):
    decoded = base64.b64decode(v.split(':').pop())
    replaced = binascii.hexlify(decoded)
    return bool(int(replaced, 16))


def generate_password(size=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(size))


def get_mapping_for_table(table_name, path='migration_result'):
    with open(path + '/mapping/' + table_name + '.json') as json_file:
        data = json.load(json_file)
        return data


def convert_string_to_time(date_string, timezone):

    import dateutil.parser
    date_time_obj = dateutil.parser.parse(date_string, ignoretz=True)

    # from datetime import datetime
    import pytz
    #
    # date_time_obj = datetime.strptime(date_string[:26], '%Y-%m-%d %H:%M:%S.%f')
    date_time_obj_timezone = pytz.timezone(timezone).localize(date_time_obj)

    return date_time_obj_timezone


def sortedWalk(top, topdown=True, onerror=None):
    from os.path import join, isdir, islink

    names = os.listdir(top)
    names.sort()
    dirs, nondirs = [], []

    for name in names:
        if isdir(os.path.join(top, name)):
            dirs.append(name)
        else:
            nondirs.append(name)

    if topdown:
        yield top, dirs, nondirs
    for name in dirs:
        path = join(top, name)
        if not os.path.islink(path):
            for x in sortedWalk(path, topdown, onerror):
                yield x
    if not topdown:
        yield top, dirs, nondirs
