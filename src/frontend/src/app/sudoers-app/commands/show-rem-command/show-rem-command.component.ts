import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-command',
  templateUrl: './show-rem-command.component.html',
  styleUrls: ['./show-rem-command.component.css']
})
export class ShowRemCommandComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/commands/';
  commandsList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshCommandsList(this.apiurl);
  }

  refreshCommandsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commandsList = data.results;

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
    this.refreshCommandsList(this.next);
  }

  fetchPrevious() {
    this.refreshCommandsList(this.previous);
  }

}
