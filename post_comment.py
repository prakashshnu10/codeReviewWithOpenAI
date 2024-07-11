import os
import requests
import json 

def get_pull_request_number():
    # GitHub event data contains the pull request number
    with open(os.getenv('GITHUB_EVENT_PATH')) as f:
        event_data = json.load(f)
    return event_data['pull_request']['number']

def post_comment(comment):
    pr_number = get_pull_request_number()
    repo = os.getenv('GITHUB_REPOSITORY')
    token = os.getenv('GITHUB')

    url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "body": comment
    }
    response = requests.post(url, json=data, headers=headers)
    if response.status_code != 201:
        raise Exception(f"Error posting comment: {response.status_code}, {response.text}")

def main():
    with open("analysis.txt", "r") as file:
        analysis = file.read()

    post_comment(analysis)

if __name__ == "__main__":
    main()
