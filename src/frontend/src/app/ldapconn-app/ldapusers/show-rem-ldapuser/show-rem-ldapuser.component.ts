import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-ldapuser',
  templateUrl: './show-rem-ldapuser.component.html',
  styleUrls: ['./show-rem-ldapuser.component.css']
})
export class ShowRemLdapuserComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/ldapconn/ldapusers/';
  ldapuserList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  ldapuser_dep = {};

  ldapusersFilter: string = "";
  ldapusersListWithoutFilter: any = [];

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLdapUsersList(this.apiurl);
  }

  refreshLdapUsersList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.ldapuserList = data.results;
      this.ldapusersListWithoutFilter = data.results;

      if (data.next) {
        this.next = data.next;
      }else{
        this.next = '';
      }

      if (data.previous) {
        this.previous = data.previous;
      }else{
        this.previous = '';
      }

    });

  }

  fetchNext() {
    this.refreshLdapUsersList(this.next);
  }

  fetchPrevious() {
    this.refreshLdapUsersList(this.previous);
  }

  addClick(ldapuser: any){
    this.ldapuser_dep = {
      'ldapuser': ldapuser,
      'add': true
    };
    this.modalTitle = 'Add User';
    this.activateAddEditComponent = true;
  }

  showClick(ldapuser: any){
    this.ldapuser_dep = {
      'ldapuser': ldapuser,
      'add': false
    };
    this.modalTitle = 'Show User';
    this.activateAddEditComponent = true;
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshLdapUsersList(this.apiurl);
  }

  FilterFn(){
    var ldapusersFilter = this.ldapusersFilter;

    this.ldapuserList = this.ldapusersListWithoutFilter.filter(function (ldapuser: any){
        return ldapuser.sAMAccountName.toString().toLowerCase().includes(
          ldapusersFilter.toString().trim().toLowerCase()
        )||
        ldapuser.objectGUIDHex.toString().toLowerCase().includes(
          ldapusersFilter.toString().trim().toLowerCase()
        )
    });
  }

}
