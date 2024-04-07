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

  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  lnxgroup_dep = {};

  lnxgroupsFilter: string = "";
  lnxgroupsListWithoutFilter: any = [];

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLnxGroupsList(this.apiurl);
  }

  refreshLnxGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.lnxgroupList = data.results;
      this.lnxgroupsListWithoutFilter = data.results;

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

  editClick(lnxgroup: any){
    this.lnxgroup_dep = {
      'lnxgroup': lnxgroup,
      'edit': true
    };
    this.modalTitle = 'Edit Group';
    this.activateAddEditComponent = true;
  }

  deleteClick(lnxgroup: any) {
    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + lnxgroup.pk + '/').subscribe(data => {
        this.refreshLnxGroupsList(this.apiurl);
      });
    }
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshLnxGroupsList(this.apiurl);
    this.lnxgroup_dep = {};
  }

  FilterFn(){
    var lnxgroupsFilter = this.lnxgroupsFilter;

    this.lnxgroupList = this.lnxgroupsListWithoutFilter.filter(function (lnxgroup: any){
        return lnxgroup.groupname.toString().toLowerCase().includes(
          lnxgroupsFilter.toString().trim().toLowerCase()
        )||
        lnxgroup.gid_number.toString().toLowerCase().includes(
          lnxgroupsFilter.toString().trim().toLowerCase()
        )
    });
  }

}
