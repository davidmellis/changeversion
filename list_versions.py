import sys
import requests
from requests.auth import HTTPBasicAuth
from distutils.version import LooseVersion

def versions(package_name, limit_releases=500):
    url = "http://18.170.223.248:8080/" + sys.argv[1] + "/json"
    print("URL: " + url)
    data = requests.get(url, verify=False).json()
    versions = list(data["releases"].keys())
    versions.sort(key=LooseVersion, reverse=True)
    return versions[:limit_releases]

print("\n".join(versions(sys.argv[1])))
