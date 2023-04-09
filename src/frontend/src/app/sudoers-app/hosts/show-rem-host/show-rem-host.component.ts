import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-host',
  templateUrl: './show-rem-host.component.html',
  styleUrls: ['./show-rem-host.component.css']
})
export class ShowRemHostComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/hosts/';
  hostsList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshHostsList(this.apiurl);
  }

  refreshHostsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hostsList = data.results;

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
    this.refreshHostsList(this.next);
  }

  fetchPrevious() {
    this.refreshHostsList(this.previous);
  }

}
