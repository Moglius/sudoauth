import { ActivatedRoute, Router } from '@angular/router';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';
import { catchError } from 'rxjs';

@Component({
  selector: 'app-add-edit-hostgroup',
  templateUrl: './add-edit-hostgroup.component.html',
  styleUrls: ['./add-edit-hostgroup.component.css']
})
export class AddEditHostgroupComponent implements OnInit{

  constructor(
    private service: LnxuserService,
    private route: ActivatedRoute,
    private router: Router) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() hostgroups_dep: any;
  readonly hostgroup_url = 'http://localhost:8000/api/sudoers/netgroups/';
  readonly host_url = 'http://localhost:8000/api/sudoers/hosts/';
  hostgroup_name: any = "";
  hosts: any[] = [];
  targetHosts: any[] = [];
  id: string = "0";

  selectedHosts: any[] = [];
  selectedSelectedHosts: any[] = [];

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.refreshHostList(this.host_url, this.id);
  }

  refreshHostList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hosts = data.results;
      if (id !== "0") {
        this.service.getLnxUsersList(this.hostgroup_url + this.id + '/').pipe(
          catchError(() => [this.router.navigate(["/hostgroups"])]),
        ).subscribe(data => {
          this.hostgroup_name = data.name;
          this.selectedHosts = data.servers;
          this.moveSelectedHosts(this.selectedHosts);
        });
      }
    });
  }

  updateHostGroup(id: string, targetHosts: any[]){
    let hosts: Number[] = [];

    targetHosts.forEach(element => {
      hosts.push(element["pk"]);
    });

    let hostgroup = {
      "servers": hosts
    };

    this.service.updateEntry(this.hostgroup_url + id + "/", hostgroup).subscribe(() => {
      this.router.navigate(["/hostgroups"]);
    });
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

  moveSelectedHosts(sourceHosts: any[]) {

    const selectedHosts = [...sourceHosts.filter(option => this.selectedHosts.includes(option))];
    this.hosts = this.hosts.filter( host_elem => !selectedHosts.find(
      sel_elem => (host_elem.pk === sel_elem.pk)
    ));
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
