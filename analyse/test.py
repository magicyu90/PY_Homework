from datetime import datetime
import pymongo
from pytz import timezone


def convert_timestamp_in_datetime_local(timestamp_received):
    dt_naive_utc = datetime.utcfromtimestamp(timestamp_received)
    return dt_naive_utc.replace(tzinfo=timezone('Asia/Shanghai'))


readable = convert_timestamp_in_datetime_local(1521277753)
conn = pymongo.MongoClient('localhost', 27017)
db = conn['SITS']
db.test.insert({'name': 'Hugo', 'clock': readable})
