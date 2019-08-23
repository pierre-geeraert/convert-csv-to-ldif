### usefull help: https://ldap3.readthedocs.io/tutorial.html

import json
import datetime
from ldap3 import Server, Connection, ALL, NTLM


def if_the_date_is_today(date_in):
    today = datetime.date.today()
    if str(date_in) == str(today):
        return "equal"
    else:
        return "none"



def readCredential(PathCredential_ldap, type):
    with open(PathCredential_ldap) as f:
        data = json.load(f)
    return data[type]

def modify_entry(cn_input,newName,connection_input):
    connection_input.modify_dn(cn_input, newName)


###
PathCredential_ldap = "ignore/ldap_credential.json"
BaseDN = readCredential(PathCredential_ldap,"baseDN")
###

server = Server(readCredential(PathCredential_ldap,"server"), get_info=ALL)
conn = Connection(server, readCredential(PathCredential_ldap,"id"), readCredential(PathCredential_ldap,"password"), auto_bind=True)
#test if connection is good
#print(conn.extend.standard.who_am_i())





#conn.search('ou=cesi,'+BaseDN, '(cn=*)', attributes=['objectclass', 'sn', 'cn', 'givenname'])
entries = conn.extend.standard.paged_search('ou=cesi,'+BaseDN, '(objectClass=person)', attributes=['sn'])
for entry in entries:

    new_name = input("modify "+str(entry['dn'])+" ?")
    if new_name == "":
        print("no changes")
    elif new_name == "stop":
        break
    else:
        print(new_name)
        print(modify_entry(entry['dn'],'cn='+new_name,conn))




#conn.modify_dn('cn=Anthony D,ou=cesi,'+BaseDN, 'cn=Anthony DESCAMPS')

"""

#'dc=geeraert,dc=eu'

result = conn.entries[0]
print(result.homePhone)

print(if_the_date_is_today(result.homePhone))

"""












