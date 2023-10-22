import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-sudorole',
  templateUrl: './add-edit-sudorole.component.html',
  styleUrls: ['./add-edit-sudorole.component.css']
})
export class AddEditSudoroleComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  readonly commandsUrl = 'http://localhost:8000/api/sudoers/commands/';
  commands: any[] = [];
  targetCommands: any[] = [];

  selectedCommands: any[] = [];
  selectedSelectedCommands: any[] = [];

  updateRole(role: any){
  }

  addRole(role: any){
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
