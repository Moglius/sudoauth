import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-hostgroup',
  templateUrl: './show-rem-hostgroup.component.html',
  styleUrls: ['./show-rem-hostgroup.component.css']
})
export class ShowRemHostgroupComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/netgroups/';
  hostgroupsList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  hostgroups_dep = {};

  hostgroupsFilter: string = "";
  hostgroupListWithoutFilter: any = [];
  addButtonText = 'Add Host Group';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshHostGroupList(this.apiurl);
  }

  refreshHostGroupList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hostgroupsList = data.results;
      this.hostgroupListWithoutFilter = data.results;

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
    this.refreshHostGroupList(this.next);
  }

  fetchPrevious() {
    this.refreshHostGroupList(this.previous);
  }

  addClick(){
    this.hostgroups_dep = {
      'hostgroup': '',
      'edit': false
    };
    this.modalTitle = 'Add Host Group';
    this.activateAddEditComponent = true;
  }

  editClick(hostgroup: any){
    this.hostgroups_dep = {
      'hostgroup': hostgroup,
      'edit': true
    };
    this.modalTitle = 'Edit Host Group';
    this.activateAddEditComponent = true;
  }

  deleteClick(hostgroup: any) {
    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + hostgroup.id + '/').subscribe(data => {
        this.refreshHostGroupList(this.apiurl);
      });
    }
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshHostGroupList(this.apiurl);
    this.hostgroups_dep = {};
  }

  FilterFn(){
    var hostgroupsFilter = this.hostgroupsFilter;

    this.hostgroupsList = this.hostgroupListWithoutFilter.filter(function (hostgroups: any){
        return hostgroups.name.toString().toLowerCase().includes(
          hostgroupsFilter.toString().trim().toLowerCase()
        )
    });

  }

  get_servers(hostgroup: any){
    return hostgroup.servers.map((obj: { hostname: string; }) => obj.hostname).join(', ');
  }

  get_nested(hostgroup: any){
    return hostgroup.nested.map((obj: { id: string; }) => obj.id).join(', ');
  }
}
