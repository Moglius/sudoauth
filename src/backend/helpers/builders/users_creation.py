import ldap
from ldap import modlist

server = "ldap://vagrant-2012-r2.localdomain.com"
connect = ldap.initialize(server)
connect.set_option(ldap.OPT_REFERRALS, 0)
user = "syncuser@localdomain.com"
passwd = "Vyq59[Tc/?6k4bT2]%aE"
connect.simple_bind_s(user, passwd)

for number in range(1, 5000):
    username = f"mdmuser{number}"
    dn = f"CN={username} {username},OU=users2,DC=localdomain,DC=com"
    attrs = {
        "objectClass": [b"top", b"person", b"organizationalPerson", b"user"],
        "cn": f"{username} {username}".encode("utf-8"),
        "sn": f"{username}".encode("utf-8"),
        "givenName": f"{username}".encode("utf-8"),
        "displayName": f"{username}".encode("utf-8"),
        "name": f"{username}".encode("utf-8"),
        "sAMAccountName": f"{username}".encode("utf-8"),
        "userPrincipalName": f"{username}@localdomain.com".encode("utf-8"),
        "userAccountControl": [b"544"],
    }
    ldif = modlist.addModlist(attrs)
    connect.add_s(dn, ldif)
