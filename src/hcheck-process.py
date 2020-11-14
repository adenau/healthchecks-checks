

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
parser.add_argument("process_name", help="name of the process")

# parse the arguments
args = parser.parse_args()
found = False
hc_url = "https://hc-ping.com/" + args.uuid

for proc in psutil.process_iter():
    try:
        processName = proc.name()
        
        if (processName.find(args.process_name) >= 0):
            found = True
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass

print(found)

if (found == False):
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