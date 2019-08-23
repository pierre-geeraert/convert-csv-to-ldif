from pushbullet import Pushbullet
from connection import readCredential,PathCredential_ldap


pb = Pushbullet(readCredential(PathCredential_ldap,"token_pushbullet"))
push = pb.push_note("This is the title", "This is the body")

