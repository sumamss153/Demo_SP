import requests

r = requests.get('https://myproject.atlassian.net/rest/api/2/search?jql=project="myproject"&maxResults=20', auth=('learn.atsj@gmail.com', 'B7SaYPPeHQqR1iQXnYC09729'))


for k in response.json().keys():
    #print(k)
    #print(response.json()[k])
    if k == 'fields':
        print(response.json()[k]['issuetype'])
        print(response.json()[k]['description'])
        print(response.json()[k]['lastViewed'])

print(r.json())
