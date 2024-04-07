import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-rules',
  templateUrl: './add-edit-rules.component.html',
  styleUrls: ['./add-edit-rules.component.css']
})
export class AddEditRulesComponent implements OnInit{

  constructor(private service: LnxuserService) {  }

  @Output() closeChild = new EventEmitter();
  @Input() ldaprule_dep: any;
  readonly url: string = 'http://localhost:8000/api/ldapconn/rules/'
  ldaprule: any;
  addFrom = false;

  ngOnInit(): void {
    this.ldaprule = this.ldaprule_dep['ldaprule'];
    this.addFrom = this.ldaprule_dep['add'];
  }

}
