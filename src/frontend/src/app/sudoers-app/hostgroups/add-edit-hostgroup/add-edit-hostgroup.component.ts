import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-hostgroup',
  templateUrl: './add-edit-hostgroup.component.html',
  styleUrls: ['./add-edit-hostgroup.component.css']
})
export class AddEditHostgroupComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() hostgroups_dep: any;
  readonly url = 'http://localhost:8000/api/sudoers/netgroups/';
  hostgroup: any;
  putFrom = false;

  ngOnInit(): void {
    this.hostgroup = this.hostgroups_dep['hostgroup'];
    this.putFrom = this.hostgroups_dep['edit'];
  }

  updateRole(hostgroup: any){
  }

  addRole(hostgroup: any){
  }

  closeClick(){
    this.closeChild.emit(null);
  }
}
