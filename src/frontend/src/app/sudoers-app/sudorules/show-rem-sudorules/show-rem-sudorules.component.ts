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

  get_commands(commands: any){
    return commands.map((obj: { full_command: string; }) => obj.full_command).join(', ')
  }

  get_hosts(hosts: any){
    return hosts.map((obj: { hostname: string; }) => obj.hostname).join(', ')
  }

}
