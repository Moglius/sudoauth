import { Router } from '@angular/router';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-sudorole',
  templateUrl: './add-edit-sudorole.component.html',
  styleUrls: ['./add-edit-sudorole.component.css']
})
export class AddEditSudoroleComponent implements OnInit{

  constructor(private service: LnxuserService, private router: Router) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  readonly commandsUrl = 'http://localhost:8000/api/sudoers/commands/';
  readonly rolesUrl = 'http://localhost:8000/api/sudoers/roles/';
  role_name: any;
  commands: any[] = [];
  targetCommands: any[] = [];

  selectedCommands: any[] = [];
  selectedSelectedCommands: any[] = [];

  updateRole(role: any){
  }

  addRole(role_name: string, selectedCommands: any[]){

    let commands: Number[] = [];

    selectedCommands.forEach(element => {
      commands.push(element["pk"]);
    });

    let role = {
      "name": role_name,
      "commands": commands
    };

    this.service.addEntry(this.rolesUrl, role).subscribe(() => {
      this.closeChild.emit(null);
      this.router.navigate(["/sudoroles"]);
    });
  }

  ngOnInit(): void {
    this.refreshCommandList(this.commandsUrl);
  }

  refreshCommandList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commands = data.results;
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

}
