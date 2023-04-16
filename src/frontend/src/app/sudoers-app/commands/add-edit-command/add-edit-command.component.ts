import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-command',
  templateUrl: './add-edit-command.component.html',
  styleUrls: ['./add-edit-command.component.css']
})
export class AddEditCommandComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() commands_dep: any;
  readonly url = 'http://localhost:8000/api/sudoers/commands/';
  command: any;
  putFrom = false;

  ngOnInit(): void {
    this.command = this.commands_dep['command'];
    this.putFrom = this.commands_dep['edit'];
  }

  updateHost(command: any){
    let val = {
      'diggest': command.diggest,
      'command': command.command,
      'args': command.args,
    }
    this.service.updateEntry(this.url + command.pk + '/', val).subscribe( () => {
      this.closeChild.emit(null);
    });
  }

  addHost(command: any){
    let val = {
      'diggest': command.diggest,
      'command': command.command,
      'args': command.args
    }
    this.service.addEntry(this.url, val).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
