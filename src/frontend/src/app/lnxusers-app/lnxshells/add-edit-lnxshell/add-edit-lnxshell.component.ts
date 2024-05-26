import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-lnxshell',
  templateUrl: './add-edit-lnxshell.component.html',
  styleUrls: ['./add-edit-lnxshell.component.css']
})
export class AddEditLnxshellComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() lnxshell_dep: any;
  readonly url: string = 'http://localhost:8000/api/lnxusers/shells/'
  lnxshell: any;
  putFrom = false;

  ngOnInit(): void {
    this.lnxshell = this.lnxshell_dep['lnxshell'];
    this.putFrom = this.lnxshell_dep['edit'];
  }

  updateLnxShell(lnxshell: any){
    let val = { 'shell': lnxshell.shell }
    this.service.updateEntry(this.url + lnxshell.pk + '/', val).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  addLnxShell(lnxshell: any){
    let val = { 'shell': lnxshell }
    this.service.addEntry(this.url, val).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
