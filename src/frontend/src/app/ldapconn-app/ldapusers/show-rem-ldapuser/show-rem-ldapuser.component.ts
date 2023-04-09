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

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLdapUsersList(this.apiurl);
  }

  refreshLdapUsersList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.ldapuserList = data.results;

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

}
