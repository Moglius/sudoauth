import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-command',
  templateUrl: './show-rem-command.component.html',
  styleUrls: ['./show-rem-command.component.css']
})
export class ShowRemCommandComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/commands/';
  commandsList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  commands_dep = {};

  commandsFilter: string = "";
  commandsListWithoutFilter: any = [];
  addButtonText = 'Add Command';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshCommandsList(this.apiurl);
  }

  refreshCommandsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.commandsList = data.results;
      this.commandsListWithoutFilter = data.results;

      if (data.next) {
        this.next = data.next;
      }else{
        this.next = '';
      }

      if (data.previous) {
        this.previous = data.previous;
      }else{
        this.previous = '';
      }

    });

  }

  fetchNext() {
    this.refreshCommandsList(this.next);
  }

  fetchPrevious() {
    this.refreshCommandsList(this.previous);
  }

  addClick(){
    this.commands_dep = {
      'command': {
        'diggest': '',
        'command': '',
        'args': ''
      },
      'edit': false
    };
    this.modalTitle = 'Add Command';
    this.activateAddEditComponent = true;
  }

  editClick(command: any){
    this.commands_dep = {
      'command': command,
      'edit': true
    };
    this.modalTitle = 'Edit Command';
    this.activateAddEditComponent = true;
  }

  deleteClick(command: any) {
    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + command.pk + '/').subscribe(data => {
        this.refreshCommandsList(this.apiurl);
      });
    }
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshCommandsList(this.apiurl);
    this.commands_dep = {};
  }

  FilterFn(){
    var commandsFilter = this.commandsFilter;

    this.commandsList = this.commandsListWithoutFilter.filter(function (command: any){
        return command.full_command.toString().toLowerCase().includes(
          commandsFilter.toString().trim().toLowerCase()
        )
    });

  }

}
