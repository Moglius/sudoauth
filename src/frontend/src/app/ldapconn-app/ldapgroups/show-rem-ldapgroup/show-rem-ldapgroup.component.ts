import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-ldapgroup',
  templateUrl: './show-rem-ldapgroup.component.html',
  styleUrls: ['./show-rem-ldapgroup.component.css']
})
export class ShowRemLdapgroupComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/ldapconn/ldapgroups/';
  ldapgroupList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  ldapgroup_dep = {};

  ldapgroupsFilter: string = "";
  ldapgroupsListWithoutFilter: any = [];

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLdapGroupsList(this.apiurl);
  }

  refreshLdapGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.ldapgroupList = data.results;
      this.ldapgroupsListWithoutFilter = data.results;

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
    this.refreshLdapGroupsList(this.next);
  }

  fetchPrevious() {
    this.refreshLdapGroupsList(this.previous);
  }

  addClick(ldapgroup: any){
    this.ldapgroup_dep = {
      'ldapgroup': ldapgroup,
      'add': true
    };
    this.modalTitle = 'Add Group';
    this.activateAddEditComponent = true;
  }

  showClick(ldapgroup: any){
    this.ldapgroup_dep = {
      'ldapgroup': ldapgroup,
      'add': false
    };
    this.modalTitle = 'Show Group';
    this.activateAddEditComponent = true;
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshLdapGroupsList(this.apiurl);
  }

  FilterFn(event: any){

    if (!event.target || event.target.value.length > 2) {
      this.refreshLdapGroupsList(`${this.apiurl}?name=${event.target.value}`);
    } else {
      this.refreshLdapGroupsList(this.apiurl);
    }
  }

}
