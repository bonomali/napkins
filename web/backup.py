import schedule
import time
import datetime

import boto
from web.private_settings import *

conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)

bucket_name = "qurse-warehouse"
bucket = conn.get_bucket(bucket_name, validate=False)

db_file = "db.sqlite3"
from boto.s3.key import Key
k = Key(bucket)

import sys
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

def backup():
	print "uploading " + datetime.datetime.now().strftime("%y/%m/%d/db.sqlite3")
	k.key = datetime.datetime.now().strftime("%y/%m/%d/db.sqlite3")
	k.set_contents_from_filename(db_file, cb=percent_cb, num_cb=10)

schedule.every().day.at("3:00").do(backup)

while True:
    schedule.run_pending()
    time.sleep(60)