import argparse
import requests

# create parser
parser = argparse.ArgumentParser(description="XYZ Check")
parser.add_argument("uuid", help="UUID of the check")
 
# parse the arguments
args = parser.parse_args()

#see https://github.com/edupr91/nagios-plugin-syncthing

try:
    r = requests.get("https://hc-ping.com/" + args.uuid, timeout=10, headers={"User-Agent": 'Python'})
    status = r.status_code
except requests.exceptions.ConnectionError:
    sys.stderr.write("Connection error\n")
except requests.exceptions.Timeout:
    sys.stderr.write("Connection timed out\n")

if status not in (200, 400):
    sys.stderr.write("Received HTTP status %d\n" % status)