import { Router } from '@angular/router';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-hostgroup',
  templateUrl: './add-edit-hostgroup.component.html',
  styleUrls: ['./add-edit-hostgroup.component.css']
})
export class AddEditHostgroupComponent implements OnInit{

  constructor(private service: LnxuserService, private router: Router) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() hostgroups_dep: any;
  readonly hostgroup_url = 'http://localhost:8000/api/sudoers/netgroups/';
  readonly host_url = 'http://localhost:8000/api/sudoers/hosts/';
  hostgroup_name: any;
  hosts: any[] = [];
  targetHosts: any[] = [];

  selectedHosts: any[] = [];
  selectedSelectedHosts: any[] = [];

  updateRole(hostgroup: any){
  }

  addHostGroup(hostgroup_name: string, selectedHosts: any[]){

    let hosts: Number[] = [];

    selectedHosts.forEach(element => {
      hosts.push(element["pk"]);
    });

    let hostgroup = {
      "name": hostgroup_name,
      "servers": hosts
    };

    this.service.addEntry(this.hostgroup_url, hostgroup).subscribe(() => {
      this.closeChild.emit(null);
      this.router.navigate(["/hostgroups"]);
    });
  }

  ngOnInit(): void {
    this.refreshHostList(this.host_url);
  }

  refreshHostList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hosts = data.results;
    });
  }

  moveSelectedHosts(sourceHosts: any[]) {

    const selectedHosts = [...sourceHosts.filter(option => this.selectedHosts.includes(option))];
    this.hosts = this.hosts.filter( function( el ) {
      return !selectedHosts.includes( el );
    });
    this.targetHosts = [...new Set([...this.targetHosts, ...selectedHosts])];
  }

  removeSelectedHosts(sourceHosts: any[]) {
    const selectedHosts = [...sourceHosts.filter(option => this.selectedSelectedHosts.includes(option))];
    this.targetHosts = this.targetHosts.filter( function( el ) {
      return !selectedHosts.includes( el );
    });
    this.hosts = [...new Set([...this.hosts, ...selectedHosts])];
  }

  moveAllHosts() {
    this.targetHosts = [...new Set([...this.targetHosts, ...this.hosts])];
    this.hosts = [];
  }

  removeAllHosts() {
    this.hosts = [...new Set([...this.hosts, ...this.targetHosts])];
    this.targetHosts = [];
  }
}
