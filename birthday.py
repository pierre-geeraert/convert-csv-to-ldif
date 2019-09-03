from ldap_connection import BaseDN
from ldap_function import make_connection,readCredential
import datetime
from pushbullet_sender import send_pushbullet_notif
from ldap3.utils.conv import escape_bytes

PathCredential_ldap = "ignore/ldap_credential.json"
BaseDN = readCredential(PathCredential_ldap,"baseDN")

#check if date_in is today or not and send 1 if it's today
def if_the_date_is_today(date_in):
    today = datetime.date.today()
    if str(date_in) == str(today):
        return True
    else:
        return False

#list all people in specific "ou", attributes should be on quotes and separate with comma
def list_people_in_ou(connection_in):
    entries = connection.extend.standard.paged_search(BaseDN, '(objectClass=person)',attributes=['cn', 'givenName', 'homePhone'])
    """
    for entry in entries:
        
        print(homePhone)
        print(if_the_date_is_today(homePhone))
    """
    return entries

connection = make_connection(PathCredential_ldap,BaseDN)
entries = list_people_in_ou(connection)

#explore entries_in and search occurence with date
def explore_entries_find_birthday(entries_in):
    list = []
    for entry in entries_in:
        name_entry_string = ''.join(entry['attributes']['givenname'])
        homePhone = entry['attributes']['homePhone']
        homePhone_string = ''.join(homePhone)
        if if_the_date_is_today(homePhone_string):
            #print("Happy birthday " + name_entry_string)
            list.append(name_entry_string)
            list.append(" ")
    return list

#print(explore_entries_find_birthday(entries))
text = ''.join(explore_entries_find_birthday(entries))
send_pushbullet_notif("Birthday of "+str(datetime.date.today())+" hour:"+str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute),"Happy birthday for : "+text)
