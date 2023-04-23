import { Component, OnInit } from '@angular/core';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-show-rem-sudorole',
  templateUrl: './show-rem-sudorole.component.html',
  styleUrls: ['./show-rem-sudorole.component.css']
})
export class ShowRemSudoroleComponent implements OnInit{

  readonly apiurl = 'http://localhost:8000/api/sudoers/roles/';
  rolesList: any = [];
  next: string = '';
  previous: string = '';
  modalTitle: string = '';
  activateAddEditComponent: boolean = false;
  roles_dep = {};

  rolesFilter: string = "";
  roleListWithoutFilter: any = [];
  addButtonText = 'Add Role';

  constructor(private service: LnxuserService) {}

  ngOnInit(): void {
    this.refreshRolesList(this.apiurl);
  }

  refreshRolesList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.rolesList = data.results;
      this.roleListWithoutFilter = data.results;

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
    this.refreshRolesList(this.next);
  }

  fetchPrevious() {
    this.refreshRolesList(this.previous);
  }

  addClick(){
    this.roles_dep = {
      'role': '',
      'edit': false
    };
    this.modalTitle = 'Add Role';
    this.activateAddEditComponent = true;
  }

  editClick(role: any){
    this.roles_dep = {
      'role': role,
      'edit': true
    };
    this.modalTitle = 'Edit Role';
    this.activateAddEditComponent = true;
  }

  deleteClick(role: any) {
    if (confirm('are you sure?')) {
      this.service.deleteEntry(this.apiurl + role.id + '/').subscribe(data => {
        this.refreshRolesList(this.apiurl);
      });
    }
  }

  closeClick(){
    this.activateAddEditComponent = false;
    this.refreshRolesList(this.apiurl);
    this.roles_dep = {};
  }

  FilterFn(){
    var lnxRolesFilter = this.rolesFilter;

    this.rolesList = this.roleListWithoutFilter.filter(function (role: any){
        return role.name.toString().toLowerCase().includes(
          lnxRolesFilter.toString().trim().toLowerCase()
        )
    });

  }

  get_commands(sudorole: any){
    return sudorole.commands.map((obj: { full_command: string; }) => obj.full_command).join(', ');
  }

}
