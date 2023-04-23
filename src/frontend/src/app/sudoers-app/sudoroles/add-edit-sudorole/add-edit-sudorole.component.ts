import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-sudorole',
  templateUrl: './add-edit-sudorole.component.html',
  styleUrls: ['./add-edit-sudorole.component.css']
})
export class AddEditSudoroleComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();

  @Input() roles_dep: any;
  readonly url = 'http://localhost:8000/api/sudoers/roles/';
  role: any;
  putFrom = false;

  ngOnInit(): void {
    this.role = this.roles_dep['role'];
    this.putFrom = this.roles_dep['edit'];
  }

  updateRole(role: any){
  }

  addRole(role: any){
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
