

# PROCESS=`ps -edf | grep -i "$1"`
# RETCODE="/fail"
# curl -fsS --retry 3 -X POST -H "Content-Type: application/json" "https://hchk.io/$2$RETCODE" >/dev/null 2>&1

import argparse
import requests
import sys
import psutil

# create parser
parser = argparse.ArgumentParser(description="Process Check")
parser.add_argument("uuid", help="UUID of the check")
parser.add_argument("dir", help="directory of partition to check")
parser.add_argument("min_free", type=float, help="min free percentage")

# parse the arguments
args = parser.parse_args()
found = False
hc_url = "https://hc-ping.com/" + args.uuid

disk_usage = psutil.disk_usage(args.dir)

print(disk_usage)

if (disk_usage.percent < args.min_free):
    hc_url = hc_url + "/fail"

try:
    r = requests.get(hc_url, timeout=10, headers={"User-Agent": 'Python'})
    status = r.status_code
except requests.exceptions.ConnectionError:
    sys.stderr.write("Connection error\n")
except requests.exceptions.Timeout:
    sys.stderr.write("Connection timed out\n")

if status not in (200, 400):
    sys.stderr.write("Received HTTP status %d\n" % status)