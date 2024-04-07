import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-lnxgroup',
  templateUrl: './add-edit-lnxgroup.component.html',
  styleUrls: ['./add-edit-lnxgroup.component.css']
})
export class AddEditLnxgroupComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();
  @Input() lnxgroup_dep: any;
  readonly url: string = 'http://localhost:8000/api/lnxusers/groups/'
  lnxgroup: any;
  putFrom = false;

  ngOnInit(): void {
    this.lnxgroup = this.lnxgroup_dep['lnxgroup'];
    this.putFrom = this.lnxgroup_dep['edit'];
  }

  updateLnxGroup(lnxgroup: any){
    let val = { 'gid_number': lnxgroup.gid_number }
    this.service.updateEntry(this.url + lnxgroup.pk + '/', val).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
