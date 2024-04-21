import { ActivatedRoute, Router } from '@angular/router';
import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';
import { catchError } from 'rxjs';

@Component({
  selector: 'app-add-edit-sudorole',
  templateUrl: './add-edit-sudorole.component.html',
  styleUrls: ['./add-edit-sudorole.component.css']
})
export class AddEditSudoroleComponent implements OnInit{

  constructor(
    private service: LnxuserService,
    private route: ActivatedRoute,
    private router: Router
  ) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  readonly commandsUrl = 'http://localhost:8000/api/sudoers/commands/';
  readonly rolesUrl = 'http://localhost:8000/api/sudoers/roles/';
  role_name: any;
  commands: any[] = [];
  targetCommands: any[] = [];
  id: string = "0";

  selectedCommands: any[] = [];
  selectedSelectedCommands: any[] = [];

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.refreshCommandList(this.commandsUrl, this.id);
  }

  refreshCommandList(url: string, id: string = '0') {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commands = data.results;
      if (id !== "0") {
        this.service.getLnxUsersList(this.rolesUrl + this.id + '/').pipe(
          catchError(() => [this.router.navigate(["/sudoroles"])]),
        ).subscribe(data => {
          this.role_name = data.name;
          this.selectedCommands = data.commands;
          this.moveSelectedCommands(this.selectedCommands);
        });
      }
    });
  }

  updateRole(id: string, targetCommands: any[]){
    let commands: Number[] = [];

    targetCommands.forEach(element => {
      commands.push(element["pk"]);
    });

    let role = {
      "commands": commands
    };

    this.service.updateEntry(this.rolesUrl + id + "/", role).subscribe(() => {
      this.router.navigate(["/sudoroles"]);
    });
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

}
