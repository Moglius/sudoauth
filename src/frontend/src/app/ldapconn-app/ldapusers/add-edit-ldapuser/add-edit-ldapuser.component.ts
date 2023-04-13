import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-ldapuser',
  templateUrl: './add-edit-ldapuser.component.html',
  styleUrls: ['./add-edit-ldapuser.component.css']
})
export class AddEditLdapuserComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild = new EventEmitter();
  @Input() ldapuser_dep: any;
  readonly url: string = 'http://localhost:8000/api/ldapconn/ldapusers/'
  ldapuser: any;
  addFrom = false;

  ngOnInit(): void {
    this.ldapuser = this.ldapuser_dep['ldapuser'];
    this.addFrom = this.ldapuser_dep['add'];
  }

  addLdapUser(ldapuser: any){
    let val = { 'objectGUIDHex': ldapuser.objectGUIDHex }
    this.service.addEntry(this.url, val).subscribe();
    this.closeChild.emit(null);
  }

}
