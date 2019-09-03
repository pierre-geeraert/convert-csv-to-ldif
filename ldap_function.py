import json
from ldap3 import Server, Connection, ALL, NTLM


def make_connection(PathCredential_ldap,BaseDN):

    try:
        server = Server(readCredential(PathCredential_ldap, "server"), get_info=ALL)
        conn = Connection(server, readCredential(PathCredential_ldap, "id"),readCredential(PathCredential_ldap, "password"), auto_bind=True)
        print("connection successful")
    except:
        print("Impossible connection")
    return conn


def modify_entry(cn_input,newName,connection_input):
    connection_input.modify_dn(cn_input, newName)

#test if connection is good
def test_connection(conn_in):
    print(conn_in.extend.standard.who_am_i())

def readCredential(PathCredential_ldap, type):
    with open(PathCredential_ldap) as f:
        data = json.load(f)
    return data[type]


#function to list all users in ldap and ask if you want to modify them or not.
def list_and_modify_users(ou_target,conn_in,BaseDn_in):
    entries = conn_in.extend.standard.paged_search('ou='+ou_target+','+BaseDn_in, '(objectClass=person)', attributes=['sn'])
    for entry in entries:

        new_name = input("modify "+str(entry['dn'])+" ?")
        if new_name == "":
            print("no changes")
        elif new_name == "stop":
            break
        else:
            print(new_name)
            print(modify_entry(entry['dn'],'cn='+new_name,conn_in))


def list_ou_ldap():
    return 0