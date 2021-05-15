#!/usr/bin/env python3

import requests
from pprint import pprint
from secrets import GITHUB_TOKEN
import argparse
import os


parser = argparse.ArgumentParser()
parser.add_argument("--name", "-n", type=str, dest="name", required=True)
parser.add_argument("--private", "-p", dest="is_private", action="store_true")
args = parser.parse_args()
pprint(args)

repo_name = args.name
is_private = args.is_private


API_URL = "https://api.github.com"
if is_private:
    payload = '{"name": "' + repo_name + '", "private": true}' 
else:
    payload = '{"name": "' + repo_name + '", "private": false}' 
    
headers = {
    "Authorization": "token "+ GITHUB_TOKEN,
    "Accept": "application/vnd.github.v3+json"
}

try:
    r = requests.post(API_URL+"/user/repos", data=payload, headers=headers)
    r.raise_for_status()
    
    
    REPO_PATH = "/Users/sasalugu/SSP/sspGithub/"
    os.chdir(REPO_PATH)
    os.system("mkdir " + repo_name)
    os.chdir(REPO_PATH + repo_name)
    os.system("git init")
    os.system("git remote add origin https://github.com/user/" + repo_name + ".git")
    os.system("echo '#" + repo_name + "' >> README.md")
    os.system("git add . && git commit -m 'Intial Commit' && git branch -M main && git push origin main")

    
except requests.exceptions.RequestException as err:
    raise SystemError(err)


