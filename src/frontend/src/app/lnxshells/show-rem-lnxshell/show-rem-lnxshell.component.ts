import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-lnxshell',
  templateUrl: './show-rem-lnxshell.component.html',
  styleUrls: ['./show-rem-lnxshell.component.css']
})
export class ShowRemLnxshellComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/lnxusers/shells/';
  lnxshellList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLnxShellsList(this.apiurl);
  }

  refreshLnxShellsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.lnxshellList = data.results;

      if (data.next) {
        this.next = data.next;
      }

      if (data.previous) {
        this.previous = data.previous;
      }

    });

  }

  fetchNext() {
    this.refreshLnxShellsList(this.next);
  }

  fetchPrevious() {
    this.refreshLnxShellsList(this.previous);
  }
}
