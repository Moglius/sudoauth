import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-sudorules',
  templateUrl: './show-rem-sudorules.component.html',
  styleUrls: ['./show-rem-sudorules.component.css']
})
export class ShowRemSudorulesComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/rules/';
  sudorulesList: any = [];
  next: string = '';
  previous: string = '';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshSudorulesList(this.apiurl);
  }

  refreshSudorulesList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.sudorulesList = data.results;

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
    this.refreshSudorulesList(this.next);
  }

  fetchPrevious() {
    this.refreshSudorulesList(this.previous);
  }
}
