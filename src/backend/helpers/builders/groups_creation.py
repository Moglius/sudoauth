import ldap
from ldap import modlist

server = "ldap://vagrant-2012-r2.localdomain.com"
connect = ldap.initialize(server)
connect.set_option(ldap.OPT_REFERRALS, 0)
user = "syncuser@localdomain.com"
passwd = "Vyq59[Tc/?6k4bT2]%aE"
connect.simple_bind_s(user, passwd)

for number in range(1, 5000):
    groupname = f"groups3_{number}"
    dn = f"CN={groupname} {groupname},OU=groups3,DC=localdomain,DC=com"
    attrs = {
        "objectClass": [b"top", b"group"],
        "description": f"{groupname}".encode("utf-8"),
        "sAMAccountName": f"{groupname}".encode("utf-8"),
    }
    ldif = modlist.addModlist(attrs)
    connect.add_s(dn, ldif)
