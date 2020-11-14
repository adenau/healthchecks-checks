

# PROCESS=`ps -edf | grep -i "$1"`
# RETCODE="/fail"
# curl -fsS --retry 3 -X POST -H "Content-Type: application/json" "https://hchk.io/$2$RETCODE" >/dev/null 2>&1

import argparse
import requests
import sys
import pySMART

# create parser
parser = argparse.ArgumentParser(description="Process Check")
parser.add_argument("uuid", help="UUID of the check")
parser.add_argument("devices", help="devices to check, comma seperated (ex: sda,sdb)")

# parse the arguments
args = parser.parse_args()
passed = True
hc_url = "https://hc-ping.com/" + args.uuid

device_list = args.devices.split(",")

for device_name in device_list:
    device = Device('/dev/' + device_name)
    
    if (sda.assessment != 'PASS'):
        passed = False

if (passed == False):
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