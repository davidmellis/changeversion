import requests
from requests.auth import HTTPBasicAuth
from distutils.version import LooseVersion

def versions(package_name, limit_releases=10):
    url = "https://18.170.223.248:8080/changeversion/json"
    s = requests.Session()
    #s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'

    # s.max_redirects = 560
    data = requests.get(url, verify=False).json()
    versions = list(data["releases"].keys())
    versions.sort(key=LooseVersion, reverse=True)
    return versions[:limit_releases]

print("\n".join(versions("changeversion")))
