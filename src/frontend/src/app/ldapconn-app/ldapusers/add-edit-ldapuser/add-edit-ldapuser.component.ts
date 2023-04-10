import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-add-edit-ldapuser',
  templateUrl: './add-edit-ldapuser.component.html',
  styleUrls: ['./add-edit-ldapuser.component.css']
})
export class AddEditLdapuserComponent implements OnInit{

  @Input() ldapuser_dep: any;
  objectGUIDHex: string = '';
  sAMAccountName: string = '';

  ngOnInit(): void {

    this.objectGUIDHex = this.ldapuser_dep.objectGUIDHex;
    this.sAMAccountName = this.ldapuser_dep.sAMAccountName;

  }

  addLdapUser(){
    console.log(this.objectGUIDHex)

  }

}
