import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-lnxgroup',
  templateUrl: './show-rem-lnxgroup.component.html',
  styleUrls: ['./show-rem-lnxgroup.component.css']
})
export class ShowRemLnxgroupComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/lnxusers/groups/';
  lnxgroupList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLnxGroupsList(this.apiurl);
  }

  refreshLnxGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.lnxgroupList = data.results;

      if (data.next) {
        this.next = data.next;
      }

      if (data.previous) {
        this.previous = data.previous;
      }

    });

  }

  fetchNext() {
    this.refreshLnxGroupsList(this.next);
  }

  fetchPrevious() {
    this.refreshLnxGroupsList(this.previous);
  }

}
