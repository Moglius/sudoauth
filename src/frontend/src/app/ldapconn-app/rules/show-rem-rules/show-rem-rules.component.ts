import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-rules',
  templateUrl: './show-rem-rules.component.html',
  styleUrls: ['./show-rem-rules.component.css']
})
export class ShowRemRulesComponent implements OnInit {

  readonly apiurl = 'http://localhost:8000/api/ldapconn/rules/';
  ldaprulesList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  ldaprule_dep = {};

  ldaprulesFilter: string = "";
  ldaprulesListWithoutFilter: any = [];

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshLdapRulesList(this.apiurl);
  }

  refreshLdapRulesList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.ldaprulesList = data.results;
      this.ldaprulesListWithoutFilter = data.results;

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
    this.refreshLdapRulesList(this.next);
  }

  fetchPrevious() {
    this.refreshLdapRulesList(this.previous);
  }

  showClick(ldaprule: any){
    this.ldaprule_dep = {
      'ldaprule': ldaprule,
      'add': false
    };
    this.modalTitle = 'Show Sudo Rule';
    this.activateAddEditComponent = true;
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshLdapRulesList(this.apiurl);
  }

  FilterFn(event: any){

    if (!event.target || event.target.value.length > 2) {
      this.refreshLdapRulesList(`${this.apiurl}?name=${event.target.value}`);
    } else {
      this.refreshLdapRulesList(this.apiurl);
    }
  }

}
