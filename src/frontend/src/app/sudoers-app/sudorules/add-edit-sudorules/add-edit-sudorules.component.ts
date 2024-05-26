import { Component, EventEmitter, Output } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { catchError } from 'rxjs';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-sudorules',
  templateUrl: './add-edit-sudorules.component.html',
  styleUrls: ['./add-edit-sudorules.component.css']
})
export class AddEditSudorulesComponent {

  constructor(
    private service: LnxuserService,
    private route: ActivatedRoute,
    private router: Router) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  readonly commandsUrl = 'http://localhost:8000/api/sudoers/commands/';
  readonly sudo_rules_url = 'http://localhost:8000/api/sudoers/rules/';
  sudo_rule_name: any;
  commands: any[] = [];
  targetCommands: any[] = [];

  selectedCommands: any[] = [];
  selectedSelectedCommands: any[] = [];

  readonly roles_url = 'http://localhost:8000/api/sudoers/roles/';
  roles: any[] = [];
  targetRoles: any[] = [];

  selectedRoles: any[] = [];
  selectedSelectedRoles: any[] = [];

  readonly host_url = 'http://localhost:8000/api/sudoers/hosts/';
  readonly hostgroups_url = 'http://localhost:8000/api/sudoers/netgroups/';
  hosts: any[] = [];
  targetHosts: any[] = [];
  hostgroups: any[] = [];
  targetHostGroups: any[] = [];

  selectedHosts: any[] = [];
  selectedSelectedHosts: any[] = [];
  selectedHostGroups: any[] = [];
  selectedSelectedHostGroups: any[] = [];

  readonly users_url = 'http://localhost:8000/api/lnxusers/users/';
  readonly groups_url = 'http://localhost:8000/api/lnxusers/groups/';
  users: any[] = [];
  users_dropdown: any[] = [];
  groups: any[] = [];
  groups_dropdown: any[] = [];
  targetUsers: any[] = [];
  targetGroups: any[] = [];
  id: string = "0";

  selectedUsers: any[] = [];
  selectedSelectedUsers: any[] = [];
  selectedGroups: any[] = [];
  selectedSelectedGroups: any[] = [];

  run_as_user: number = 0;
  run_as_group: number = 0;

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.refreshCommandList(this.commandsUrl, this.id);
    this.refreshRolesList(this.roles_url, this.id);
    this.refreshUsersList(this.users_url, this.id);
    this.refreshGroupsList(this.groups_url, this.id);
    this.refreshHostGroupsList(this.hostgroups_url, this.id);
    this.refreshHostList(this.host_url, this.id);
  }

  refreshHostList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hosts = data.results;
      if (id !== "0") {
        this.service.getLnxUsersList(this.sudo_rules_url + this.id + '/').pipe(
          catchError(() => [this.router.navigate(["/sudoroles"])]),
        ).subscribe(data => {
          this.sudo_rule_name = data.name;
          this.selectedHosts = data.sudo_host_servers;
          this.moveSelectedHosts(this.selectedHosts);
          this.selectedHostGroups = data.sudo_host_groups;
          this.moveSelectedHostGroups(this.selectedHostGroups);
          this.selectedCommands = data.sudo_command;
          this.moveSelectedCommands(this.selectedCommands);
          this.selectedRoles = data.sudo_command_role;
          this.moveSelectedRoles(this.selectedRoles);
          this.selectedUsers = data.sudo_user_users;
          this.moveSelectedUsers(this.selectedUsers);
          this.selectedGroups = data.sudo_user_groups;
          this.moveSelectedGroups(this.selectedGroups);
          this.run_as_user = data.run_as_user.pk;
          this.run_as_group = data.run_as_group.pk;
        });
      }
    });
  }

  refreshCommandList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commands = data.results;
    });
  }

  refreshRolesList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.roles = data.results;
    });
  }

  refreshUsersList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.users = data.results;
      this.users_dropdown = data.results;
    });
  }

  refreshHostGroupsList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.hostgroups = data.results;
    });
  }

  refreshGroupsList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.groups = data.results;
      this.groups_dropdown = data.results;
    });
  }

  updateSudoRule(id: string, targetCommands: any[], selectedRoles: any[], targetHosts: any[], targetHostGroups: any[], targetUsers: any[], targetGroups: any[], run_as_user: number, run_as_group: number){
    let commands: Number[] = [];
    let roles: Number[] = [];
    let hosts: Number[] = [];
    let hostgroups: Number[] = [];
    let users: Number[] = [];
    let groups: Number[] = [];

    targetCommands.forEach(element => {
      commands.push(element["pk"]);
    });

    selectedRoles.forEach(element => {
      roles.push(element["id"]);
    });

    targetHostGroups.forEach(element => {
      hostgroups.push(element["id"]);
    });

    targetHosts.forEach(element => {
      hosts.push(element["pk"]);
    });

    targetUsers.forEach(element => {
      users.push(element["pk"]);
    });

    targetGroups.forEach(element => {
      groups.push(element["pk"]);
    });

    let sudo_rule = {
      "sudo_command": commands,
      "sudo_command_role": roles,
      "sudo_host_servers": hosts,
      "sudo_host_groups": hostgroups,
      "sudo_user_users": users,
      "sudo_user_groups": groups,
      "run_as_user": run_as_user,
      "run_as_group": run_as_group
    };

    this.service.updateEntry(this.sudo_rules_url + id + "/", sudo_rule).subscribe(() => {
      this.router.navigate(["/sudorules"]);
    });
  }

  addSudoRule(role_name: string, selectedCommands: any[], selectedRoles: any[], selectedHosts: any[], selectedHostGroups: any[], selectedUsers: any[], selectedGroups: any[], run_as_user: number, run_as_group: number){

    let commands: Number[] = [];
    let roles: Number[] = [];
    let hosts: Number[] = [];
    let hostgroups: Number[] = [];
    let users: Number[] = [];
    let groups: Number[] = [];

    selectedCommands.forEach(element => {
      commands.push(element["pk"]);
    });

    selectedRoles.forEach(element => {
      roles.push(element["id"]);
    });

    selectedHosts.forEach(element => {
      hosts.push(element["pk"]);
    });

    selectedHostGroups.forEach(element => {
      hostgroups.push(element["id"]);
    });

    selectedUsers.forEach(element => {
      users.push(element["pk"]);
    });

    selectedGroups.forEach(element => {
      groups.push(element["pk"]);
    });

    let sudo_rule = {
      "name": role_name,
      "sudo_command": commands,
      "sudo_command_role": roles,
      "sudo_host_servers": hosts,
      "sudo_host_groups": hostgroups,
      "sudo_user_users": users,
      "sudo_user_groups": groups,
      "run_as_user": run_as_user,
      "run_as_group": run_as_group
    };

    this.service.addEntry(this.sudo_rules_url, sudo_rule).subscribe(() => {
      this.router.navigate(["/sudorules"]);
    });
  }

  moveSelectedCommands(sourceCommands: any[]) {

    const selectedCommands = [...sourceCommands.filter(option => this.selectedCommands.includes(option))];
    this.commands = this.commands.filter( host_elem => !selectedCommands.find(
      sel_elem => (host_elem.pk === sel_elem.pk)
    ));
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

  moveSelectedRoles(sourceRoles: any[]) {

    const selectedRoles = [...sourceRoles.filter(option => this.selectedRoles.includes(option))];
    this.roles = this.roles.filter( host_elem => !selectedRoles.find(
      sel_elem => (host_elem.id === sel_elem.id)
    ));
    this.targetRoles = [...new Set([...this.targetRoles, ...selectedRoles])];
  }

  removeSelectedRoles(sourceRoles: any[]) {
    const selectedRoles = [...sourceRoles.filter(option => this.selectedSelectedRoles.includes(option))];
    this.targetRoles = this.targetRoles.filter( function( el ) {
      return !selectedRoles.includes( el );
    });
    this.roles = [...new Set([...this.roles, ...selectedRoles])];
  }

  moveAllRoles() {
    this.targetRoles = [...new Set([...this.targetRoles, ...this.roles])];
    this.roles = [];
  }

  removeAllRoles() {
    this.roles = [...new Set([...this.roles, ...this.targetRoles])];
    this.targetRoles = [];
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

  moveSelectedHostGroups(sourceHostGroups: any[]) {
    const selectedHostGroups = [...sourceHostGroups.filter(option => this.selectedHostGroups.includes(option))];
    this.hostgroups = this.hostgroups.filter( host_elem => !selectedHostGroups.find(
      sel_elem => (host_elem.id === sel_elem.id)
    ));
    this.targetHostGroups = [...new Set([...this.targetHostGroups, ...selectedHostGroups])];
  }

  removeSelectedHostGroups(sourceHostGroups: any[]) {
    const selectedHostGroups = [...sourceHostGroups.filter(option => this.selectedSelectedHostGroups.includes(option))];
    this.targetHostGroups = this.targetHostGroups.filter( function( el ) {
      return !selectedHostGroups.includes( el );
    });
    this.hostgroups = [...new Set([...this.hostgroups, ...selectedHostGroups])];
  }

  moveAllHostGroups() {
    this.targetHostGroups = [...new Set([...this.targetHostGroups, ...this.hostgroups])];
    this.hostgroups = [];
  }

  removeAllHostGroups() {
    this.hostgroups = [...new Set([...this.hostgroups, ...this.targetHostGroups])];
    this.targetHostGroups = [];
  }

  moveSelectedUsers(sourceUsers: any[]) {

    const selectedUsers = [...sourceUsers.filter(option => this.selectedUsers.includes(option))];
    this.users = this.users.filter( host_elem => !selectedUsers.find(
      sel_elem => (host_elem.pk === sel_elem.pk)
    ));
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

  moveSelectedGroups(sourceGroups: any[]) {

    const selectedGroups = [...sourceGroups.filter(option => this.selectedGroups.includes(option))];
    this.groups = this.groups.filter( host_elem => !selectedGroups.find(
      sel_elem => (host_elem.pk === sel_elem.pk)
    ));
    this.targetGroups = [...new Set([...this.targetGroups, ...selectedGroups])];
  }

  removeSelectedGroups(sourceGroups: any[]) {
    const selectedGroups = [...sourceGroups.filter(option => this.selectedSelectedGroups.includes(option))];
    this.targetGroups = this.targetGroups.filter( function( el ) {
      return !selectedGroups.includes( el );
    });
    this.groups = [...new Set([...this.groups, ...selectedGroups])];
  }

  moveAllGroups() {
    this.targetGroups = [...new Set([...this.targetGroups, ...this.groups])];
    this.groups = [];
  }

  removeAllGroups() {
    this.groups = [...new Set([...this.groups, ...this.targetGroups])];
    this.targetGroups = [];
  }

}
