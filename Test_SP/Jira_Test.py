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
    print("Creating new Bug ")
    issueDict = {
            'project': {'key': 'DQT'},
            'summary': summary,
            'description': 'Creating of an issue using project keys and issue type names using the REST API',
            'issuetype': {'name': 'Bug'},
        
    child = jira.create_issue(fields=issueDict)
    print("Created new Bug: " + child.key)

main()
