'''
{'description': [b'Designated administrators of the schema'], 
'member': [b'CN=sync user,CN=Users,DC=localdomain,DC=com'], 
'distinguishedName': [b'CN=Schema Admins,CN=Users,DC=localdomain,DC=com'], 
'memberOf': [b'CN=Denied RODC Password Replication Group,CN=Users,DC=localdomain,DC=com'], 
'objectGUID': [b'R\xc4\xca\xee\xd5\xa94E\x82\xe5\x13\xc1\xcd\x13\x83e'], 
'objectSid': [b'\x01\x05\x00\x00\x00\x00\x00\x05\x15\x00\x00\x00\x90\xf2\x15\xd3\xea\xa0Jz1\xd7\xeeR\x06\x02\x00\x00'], 
'sAMAccountName': [b'Schema Admins']}
'''

import ldap
from ldap import modlist

server = 'ldap://vagrant-2012-r2.localdomain.com'
connect = ldap.initialize(server)
connect.set_option(ldap.OPT_REFERRALS, 0)
user = 'syncuser@localdomain.com'
passwd = 'Vyq59[Tc/?6k4bT2]%aE'
connect.simple_bind_s(user, passwd)

for number in range(1,5000):
    groupname = f"groups3_{number}"
    dn = f"CN={groupname} {groupname},OU=groups3,DC=localdomain,DC=com"
    attrs = {}
    attrs['objectClass'] = [b'top', b'group']
    attrs['description'] = f"{groupname}".encode('utf-8')
    attrs['sAMAccountName'] = f"{groupname}".encode('utf-8')

    ldif = modlist.addModlist(attrs)
    connect.add_s(dn, ldif)
