import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-lnxuser',
  templateUrl: './show-rem-lnxuser.component.html',
  styleUrls: ['./show-rem-lnxuser.component.css']
})
export class ShowRemLnxuserComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/lnxusers/users/';
  lnxuserList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLnxUsersList(this.apiurl);
  }

  refreshLnxUsersList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.lnxuserList = data.results;

      if (data.next) {
        this.next = data.next;
      }

      if (data.previous) {
        this.previous = data.previous;
      }

    });

  }

  fetchNext() {
    this.refreshLnxUsersList(this.next);
  }

  fetchPrevious() {
    this.refreshLnxUsersList(this.previous);
  }

}
