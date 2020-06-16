import pyodbc
import pandas as pd
from jira.client import JIRA
from datetime import date

def main():

    conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=IN2396424W1\SQLEXPRESS;'
                      'Database=Test_DB_SSS;'
                      'Trusted_Connection=yes;')
    spname = "IAG_SP"
    cursor = conn.cursor()
    cursor.execute('EXECUTE dbo.' + spname)
    conn.commit()
    print(spname + ' Completed!!!')
    getfinalresults(conn)


def getfinalresults(conn):
    tnameS = "automation_test_result"

    result_data = pd.read_sql('select test_case_id, execution_date, execution_result from [dbo].' + tnameS, conn)
    result_data.execution_date = pd.to_datetime(result_data.execution_date)
    latest_data = result_data.sort_values('execution_date').drop_duplicates(['test_case_id'],keep='last')
    print(latest_data)
    jira_cred(latest_data)

def jira_cred(latest_data):
    api_token = "B7SaYPPeHQqR1iQXnYC09729"
    url = 'https://learnatsj.atlassian.net/'
    email = 'learn.atsj@gmail.com'
    jira = JIRA(options={'server': url},
                basic_auth=(email, api_token))
    print("Jira Connection Successful!!!")
    jira_createTC(api_token,url,email,latest_data)

def jira_createTC(api_token,url,email,latest_data):
    jira = JIRA(options={'server': url},
                basic_auth=(email, api_token))
    for ind in latest_data.index:
        issue = jira.issue(latest_data['test_case_id'][ind])
        summary = str(issue) + "_" + str(date.today())
        print("Creating sub-task ", summary, "for Issue...", issue)
        issueDict = {
            'project': {'key': 'DQT'},
            'summary': summary,
            'issuetype': {'name': 'Sub-task'},
            'parent': {'key': issue.key},
        }
        child = jira.create_issue(fields=issueDict)
        print("Created sub-task: " + child.key)
        jira_updateTC(api_token,url,email,child.key,latest_data['execution_result'][ind])

def jira_updateTC(api_token,url,email,key,result):
    jira = JIRA(options={'server': url},
                basic_auth=(email, api_token))
    issue = jira.issue(key)
    print("Executing Issue...", issue)
    issue.update(fields={'project': {'key': 'DQT'}, 'customfield_10034': {'value': result}})
    issue.update(fields={'project': {'key': 'DQT'}, "customfield_10035": "As Expected."})
    print("Test case executed successfully...", result)

main()