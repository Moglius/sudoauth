import { Component, EventEmitter, Input, Output } from '@angular/core';
import { catchError } from 'rxjs';
import { LnxuserService } from 'src/app/lnxuser.service';

@Component({
  selector: 'app-add-edit-lnxuser',
  templateUrl: './add-edit-lnxuser.component.html',
  styleUrls: ['./add-edit-lnxuser.component.css']
})
export class AddEditLnxuserComponent {

  constructor(private service: LnxuserService) {  }

  @Output() closeChild: EventEmitter<any> = new EventEmitter();
  @Input() lnxuser_dep: any;
  readonly url: string = 'http://localhost:8000/api/lnxusers/users/'
  readonly groups_url = 'http://localhost:8000/api/lnxusers/groups/';
  readonly shells_url = 'http://localhost:8000/api/lnxusers/shells/';
  lnxuser: any;
  putFrom = false;

  groups: any[] = [];
  primary_group: number = 0;

  shells: any[] = [];
  shell: number = 0;

  ngOnInit(): void {
    this.lnxuser = this.lnxuser_dep['lnxuser'];
    this.putFrom = this.lnxuser_dep['edit'];
    this.primary_group = this.lnxuser.primary_group.pk;
    this.shell = this.lnxuser.login_shell.pk;
    this.refreshGroupsList(this.groups_url);
    this.refreshShellList(this.shells_url);
  }

  refreshGroupsList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.groups = data.results;
    });
  }

  refreshShellList(url: string) {
    this.service.getLnxUsersList(url).subscribe(data=>{
      this.shells = data.results;
    });
  }

  updateLnxUser(lnxuser: any, primary_group: number, shell: number){
    console.log(primary_group);
    let val = {
      "uid_number": lnxuser.uid_number,
      "home_dir": lnxuser.home_dir,
      "primary_group": primary_group,
      "login_shell": shell
    };
    this.service.updateEntry(this.url + lnxuser.pk + '/', val).pipe(
      catchError(() => [this.closeChild.emit(null)]),
    ).subscribe(() => {
      this.closeChild.emit(null);
    });
  }

  closeClick(){
    this.closeChild.emit(null);
  }

}
