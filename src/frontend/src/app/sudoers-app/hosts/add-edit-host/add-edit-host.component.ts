import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-host',
  templateUrl: './add-edit-host.component.html',
  styleUrls: ['./add-edit-host.component.css']
})
export class AddEditHostComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() hosts_dep: any;
  readonly url = 'http://localhost:8000/api/sudoers/hosts/';
  host: any;
  putFrom = false;

  ngOnInit(): void {
    this.host = this.hosts_dep['host'];
    this.putFrom = this.hosts_dep['edit'];
  }

  updateHost(host: any){
    let val = { 'hostname': host.hostname }
    this.service.updateEntry(this.url + host.pk + '/', val).subscribe( () => {
      this.closeChild.emit(null);
    });
  }

  addHost(hostname: any){
    let val = { 'hostname': hostname }
    this.service.addEntry(this.url, val).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
