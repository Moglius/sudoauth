import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-lnxshell',
  templateUrl: './show-rem-lnxshell.component.html',
  styleUrls: ['./show-rem-lnxshell.component.css']
})
export class ShowRemLnxshellComponent implements OnInit{

  constructor(private service: LnxuserService) {}

  readonly apiurl = 'http://localhost:8000/api/lnxusers/shells/';
  lnxshellList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  lnxshell_dep = {};

  lnxshellsFilter: string = "";
  lnxshellsListWithoutFilter: any = [];
  addButtonText = 'Add LnxShell';

  ngOnInit(): void {
    this.refreshLnxShellsList(this.apiurl);
  }

  refreshLnxShellsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.lnxshellList = data.results;
      this.lnxshellsListWithoutFilter = data.results;

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

  addClick(){
    this.lnxshell_dep = {
      'lnxshell': '',
      'edit': false
    };
    this.modalTitle = 'Add Shell';
    this.activateAddEditComponent = true;
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
    this.lnxshell_dep = {};
  }

  FilterFn(){
    var lnxshellsFilter = this.lnxshellsFilter;

    this.lnxshellList = this.lnxshellsListWithoutFilter.filter(function (ldaprule: any){
        return ldaprule.shell.toString().toLowerCase().includes(
          lnxshellsFilter.toString().trim().toLowerCase()
        )
    });

  }
}
