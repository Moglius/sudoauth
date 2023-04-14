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
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  lnxshell_dep = {};

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

  editClick(lnxshell: any){
    this.lnxshell_dep = {
      'lnxshell': lnxshell,
      'edit': true
    };
    this.modalTitle = 'Edit Shell';
    this.activateAddEditComponent = true;
  }

  deleteClick(lnxshell: any) {

    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + lnxshell.pk + '/').subscribe(data => {
        this.refreshLnxShellsList(this.apiurl);
      });
    }

  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshLnxShellsList(this.apiurl);
  }
}
