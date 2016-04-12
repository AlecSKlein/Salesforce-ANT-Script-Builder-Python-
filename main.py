from simple_salesforce import Salesforce

def sf_login(username, password, sandbox, security_token=''):
    return Salesforce(username=username, password=password, sandbox=sandbox, security_token=security_token)

def get_sobjects(sfDescripion):
    sobjects = {True: [], False: []}
    for sobject in sfDescripion['sobjects']:
        sobjects[sobject['customSetting']].append(sobject)
    return sobjects