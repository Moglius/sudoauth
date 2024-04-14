import { Component, EventEmitter, Output } from '@angular/core';
import { Router } from '@angular/router';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-sudorules',
  templateUrl: './add-edit-sudorules.component.html',
  styleUrls: ['./add-edit-sudorules.component.css']
})
export class AddEditSudorulesComponent {

  constructor(private service: LnxuserService, private router: Router) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  readonly commandsUrl = 'http://localhost:8000/api/sudoers/commands/';
  readonly sudo_rules_url = 'http://localhost:8000/api/sudoers/rules/';
  sudo_rule_name: any;
  commands: any[] = [];
  targetCommands: any[] = [];

  selectedCommands: any[] = [];
  selectedSelectedCommands: any[] = [];

  readonly host_url = 'http://localhost:8000/api/sudoers/hosts/';
  hosts: any[] = [];
  targetHosts: any[] = [];

  selectedHosts: any[] = [];
  selectedSelectedHosts: any[] = [];

  readonly users_url = 'http://localhost:8000/api/lnxusers/users/';
  readonly groups_url = 'http://localhost:8000/api/lnxusers/groups/';
  users: any[] = [];
  groups: any[] = [];
  targetUsers: any[] = [];

  selectedUsers: any[] = [];
  selectedSelectedUsers: any[] = [];

  run_as_user: number = 0;
  run_as_group: number = 0;

  addSudoRule(role_name: string, selectedCommands: any[], selectedHosts: any[], selectedUsers: any[], run_as_user: number, run_as_group: number){

    let commands: Number[] = [];
    let hosts: Number[] = [];
    let users: Number[] = [];

    selectedCommands.forEach(element => {
      commands.push(element["pk"]);
    });

    selectedHosts.forEach(element => {
      hosts.push(element["pk"]);
    });

    selectedUsers.forEach(element => {
      users.push(element["pk"]);
    });

    let sudo_rule = {
      "name": role_name,
      "sudo_command": commands,
      "sudo_host_servers": hosts,
      "sudo_user_users": users,
      "run_as_user": run_as_user,
      "run_as_group": run_as_group
    };

    this.service.addEntry(this.sudo_rules_url, sudo_rule).subscribe(() => {
      this.closeChild.emit(null);
      this.router.navigate(["/sudorules"]);
    });
  }

  ngOnInit(): void {
    this.refreshCommandList(this.commandsUrl);
    this.refreshHostList(this.host_url);
    this.refreshUsersList(this.users_url);
    this.refreshGroupsList(this.groups_url);
  }

  refreshHostList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hosts = data.results;
    });
  }

  refreshCommandList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commands = data.results;
    });
  }

  refreshUsersList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.users = data.results;
    });
  }

  refreshGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.groups = data.results;
    });
  }

  moveSelectedCommands(sourceCommands: any[]) {

    const selectedCommands = [...sourceCommands.filter(option => this.selectedCommands.includes(option))];
    this.commands = this.commands.filter( function( el ) {
      return !selectedCommands.includes( el );
    });
    this.targetCommands = [...new Set([...this.targetCommands, ...selectedCommands])];
  }

  removeSelectedCommands(sourceCommands: any[]) {
    const selectedCommands = [...sourceCommands.filter(option => this.selectedSelectedCommands.includes(option))];
    this.targetCommands = this.targetCommands.filter( function( el ) {
      return !selectedCommands.includes( el );
    });
    this.commands = [...new Set([...this.commands, ...selectedCommands])];
  }

  moveAllCommands() {
    this.targetCommands = [...new Set([...this.targetCommands, ...this.commands])];
    this.commands = [];
  }

  removeAllCommands() {
    this.commands = [...new Set([...this.commands, ...this.targetCommands])];
    this.targetCommands = [];
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

  moveSelectedUsers(sourceUsers: any[]) {

    const selectedUsers = [...sourceUsers.filter(option => this.selectedUsers.includes(option))];
    this.users = this.users.filter( function( el ) {
      return !selectedUsers.includes( el );
    });
    this.targetUsers = [...new Set([...this.targetUsers, ...selectedUsers])];
  }

  removeSelectedUsers(sourceUsers: any[]) {
    const selectedUsers = [...sourceUsers.filter(option => this.selectedSelectedUsers.includes(option))];
    this.targetUsers = this.targetUsers.filter( function( el ) {
      return !selectedUsers.includes( el );
    });
    this.users = [...new Set([...this.users, ...selectedUsers])];
  }

  moveAllUsers() {
    this.targetUsers = [...new Set([...this.targetUsers, ...this.users])];
    this.users = [];
  }

  removeAllUsers() {
    this.users = [...new Set([...this.users, ...this.targetUsers])];
    this.targetUsers = [];
  }


}
