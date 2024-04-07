import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-ldapgroup',
  templateUrl: './add-edit-ldapgroup.component.html',
  styleUrls: ['./add-edit-ldapgroup.component.css']
})
export class AddEditLdapgroupComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild = new EventEmitter();
  @Input() ldapgroup_dep: any;
  readonly url: string = 'http://localhost:8000/api/ldapconn/ldapgroups/'
  ldapgroup: any;
  addFrom = false;

  ngOnInit(): void {
    this.ldapgroup = this.ldapgroup_dep['ldapgroup'];
    this.addFrom = this.ldapgroup_dep['add'];
  }

  addLdapGroup(ldapgroup: any){
    let val = { 'objectGUIDHex': ldapgroup.objectGUIDHex }
    this.service.addEntry(this.url, val).subscribe();
    this.closeChild.emit(null);
  }

}
