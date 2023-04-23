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

  moveSelectedCommands(sourceCommands: any[], targetCommands: any[]) {

    /*const selectedCommands = [...sourceCommands.filter(option => this.selectedCommands.includes(option))];
    this.selectedCommands = this.selectedCommands.filter(option => !selectedCommands.includes(option));
    this.selectedSelectedCommands = [...this.selectedSelectedCommands, ...selectedCommands];*/

    console.log(targetCommands);
    this.selectedSelectedCommands = [...this.selectedSelectedCommands, ...targetCommands];
  }

  moveAllCommands() {

    /*const selectedCommands = [...sourceCommands.filter(option => this.selectedCommands.includes(option))];
    this.selectedCommands = this.selectedCommands.filter(option => !selectedCommands.includes(option));
    this.selectedSelectedCommands = [...this.selectedSelectedCommands, ...selectedCommands];*/

    this.selectedSelectedCommands = [...this.commands];
    this.commands = [];
  }

  removeAllCommands() {

    /*const selectedCommands = [...sourceCommands.filter(option => this.selectedCommands.includes(option))];
    this.selectedCommands = this.selectedCommands.filter(option => !selectedCommands.includes(option));
    this.selectedSelectedCommands = [...this.selectedSelectedCommands, ...selectedCommands];*/

    this.commands = [...this.selectedSelectedCommands];
    this.selectedSelectedCommands = [];
  }

}
