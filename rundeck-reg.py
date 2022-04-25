import requests
from requests import get


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


name = "YOUR_NAME"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
rundeck_url = "https://rundeck.natuurenbos.be"

external_ip = get('https://api.ipify.org').content.decode('utf8')

print(f"{bcolors.HEADER} Public IP: {external_ip}{bcolors.ENDC}")

s = requests.Session()
r = s.post(rundeck_url + "/j_security_check",
           data={"j_username": username, "j_password": password})

# jobdata = {"options": {"IP": external_ip, "Naam": name}}
jobdata = {"option.IP": external_ip, "option.Naam": name}
requestheaders = {'Accept': 'application/json'}

r = s.post(rundeck_url + "/api/27/job/e8507b3b-b82c-4454-af30-e128cd7dbb06/run",
           data=jobdata,
           headers=requestheaders)

print(f"{bcolors.OKGREEN} Status Dev Tools: OK{bcolors.ENDC}") if r.status_code == 200 else print(
    f"{bcolors.FAIL} Status Dev Tools: NOK{bcolors.ENDC}")

r = s.post(rundeck_url + "/api/27/job/9a190daf-3a6c-4d9f-8f28-e4d4a771ffbc/run",
           data=jobdata,
           headers=requestheaders)

print(f"{bcolors.OKGREEN} Status Non-prod: OK{bcolors.ENDC}") if r.status_code == 200 else print(
    f"{bcolors.FAIL} Status Non-prod: NOK{bcolors.ENDC}")

r = s.post(rundeck_url + "/api/27/job/cde17503-06eb-4b09-b5fc-8388e0fa1902/run",
           data=jobdata,
           headers=requestheaders)

print(f"{bcolors.OKGREEN} Status Prod: OK{bcolors.ENDC}") if r.status_code == 200 else print(
    f"{bcolors.FAIL} Status Prod: NOK{bcolors.ENDC}")

s.close()
