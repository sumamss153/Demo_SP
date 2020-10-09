import pyodbc
import pandas as pd
from jira.client import JIRA
from datetime import date

def main():


    api_token = "B7SaYPPeHQqR1iQXnYC09729"
    url = 'https://learnatsj.atlassian.net/'
    email = 'learn.atsj@gmail.com'
    jira = JIRA(options={'server': url},
                basic_auth=(email, api_token))
    print("Jira Connection Successful!!!")
    summary = "Bug_" + str(date.today())
    print("Creating new Sub-task...")
    issueDict = {
            'project': {'key': 'DQT'},
            'summary': summary,
            'issuetype': {'name': 'Task'},
    }  
    child = jira.create_issue(fields=issueDict)
    print("Created new Sub-task: " + child.key)

main()
