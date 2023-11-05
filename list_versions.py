import requests
from requests.auth import HTTPBasicAuth
from distutils.version import LooseVersion

def versions(package_name, limit_releases=1000):
    url = "http://18.170.223.248:8080/changeversion/json"
    data = requests.get(url, verify=False).json()
    versions = list(data["releases"].keys())
    versions.sort(key=LooseVersion, reverse=True)
    return versions[:limit_releases]

print("\n".join(versions("changeversion")))
