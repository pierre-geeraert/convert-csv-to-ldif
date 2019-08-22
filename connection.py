import json
from ldap3 import Server, Connection, ALL, NTLM

PathCredential_ldap = "ignore/ldap_credential.json"

def readCredential(PathCredential_ldap, type):
    with open(PathCredential_ldap) as f:
        data = json.load(f)
    return data[type]

### usefull help: https://ldap3.readthedocs.io/tutorial.html

server = Server(readCredential(PathCredential_ldap,"server"), get_info=ALL)
conn = Connection(server, readCredential(PathCredential_ldap,"id"), readCredential(PathCredential_ldap,"password"), auto_bind=True)
print(conn.extend.standard.who_am_i())