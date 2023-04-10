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

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLdapGroupsList(this.apiurl);
  }

  refreshLdapGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.ldapgroupList = data.results;

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

}