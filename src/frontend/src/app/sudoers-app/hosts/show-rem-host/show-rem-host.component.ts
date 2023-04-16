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
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  hosts_dep = {};

  hostsFilter: string = "";
  hostListWithoutFilter: any = [];
  addButtonText = 'Add Host';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshHostsList(this.apiurl);
  }

  refreshHostsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hostsList = data.results;
      this.hostListWithoutFilter = data.results;

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

  addClick(){
    this.hosts_dep = {
      'host': '',
      'edit': false
    };
    this.modalTitle = 'Add Host';
    this.activateAddEditComponent = true;
  }

  editClick(host: any){
    this.hosts_dep = {
      'host': host,
      'edit': true
    };
    this.modalTitle = 'Edit Host';
    this.activateAddEditComponent = true;
  }

  deleteClick(host: any) {
    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + host.pk + '/').subscribe(data => {
        this.refreshHostsList(this.apiurl);
      });
    }
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshHostsList(this.apiurl);
    this.hosts_dep = {};
  }

  FilterFn(){
    var lnxshellsFilter = this.hostsFilter;

    this.hostsList = this.hostListWithoutFilter.filter(function (host: any){
        return host.hostname.toString().toLowerCase().includes(
          lnxshellsFilter.toString().trim().toLowerCase()
        )
    });

  }

}
