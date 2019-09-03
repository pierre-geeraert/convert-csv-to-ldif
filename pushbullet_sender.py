from pushbullet import Pushbullet
from ldap_function import readCredential

PathCredential_ldap = "ignore/ldap_credential.json"

def send_pushbullet_notif(title,message):
    pb = Pushbullet(readCredential(PathCredential_ldap,"token_pushbullet"))
    push = pb.push_note(title,message)
