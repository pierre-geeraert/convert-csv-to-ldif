### usefull help: https://ldap3.readthedocs.io/tutorial.html

import json
from ldap3 import Server, Connection, ALL, NTLM
from ldap_function import modify_entry, test_connection






def readCredential(PathCredential_ldap, type):
    with open(PathCredential_ldap) as f:
        data = json.load(f)
    return data[type]


###
PathCredential_ldap = "ignore/ldap_credential.json"
BaseDN = readCredential(PathCredential_ldap,"baseDN")
###

server = Server(readCredential(PathCredential_ldap,"server"), get_info=ALL)
conn = Connection(server, readCredential(PathCredential_ldap,"id"), readCredential(PathCredential_ldap,"password"), auto_bind=True)





#print("you don't have to read this")
"""
conn.search('ou=cesi,'+BaseDN, '(cn=*)', attributes=['objectclass', 'sn', 'cn', 'givenname'])

result = conn.entries[0]
print(result)
"""
#list all "ou" in ldap server



#list_and_modify_users("cesi")

"""

#'dc=geeraert,dc=eu'

result = conn.entries[0]
print(result.homePhone)

print(if_the_date_is_today(result.homePhone))

"""












