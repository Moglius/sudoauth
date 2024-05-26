import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';
import { LnxuserService } from 'src/app/lnxuser.service';


@Component({
  selector: 'app-dashboard-app',
  standalone: true,
  imports: [RouterLink],
  templateUrl: './dashboard-app.component.html',
  styleUrl: './dashboard-app.component.css'
})
export class DashboardAppComponent {

  constructor(private service: LnxuserService) {}

  readonly api_url = 'http://localhost:8000/api/';

  hosts: number = 0;
  command_roles: number = 0;
  sudo_rules: number = 0;
  shells: number = 0;
  groups: number = 0;
  users: number = 0;

  ngOnInit(): void {
    this.refreshDashboard(this.api_url);
  }

  refreshDashboard(url: string) {
    this.service.getLnxUsersList(`${url}sudoers/hosts/`).subscribe(data=>{
      this.hosts = data.count;
    });
    this.service.getLnxUsersList(`${url}sudoers/roles/`).subscribe(data=>{
      this.command_roles = data.count;
    });
    this.service.getLnxUsersList(`${url}sudoers/rules/`).subscribe(data=>{
      this.sudo_rules = data.count;
    });
    this.service.getLnxUsersList(`${url}lnxusers/shells/`).subscribe(data=>{
      this.shells = data.count;
    });
    this.service.getLnxUsersList(`${url}lnxusers/groups/`).subscribe(data=>{
      this.groups = data.count;
    });
    this.service.getLnxUsersList(`${url}lnxusers/users/`).subscribe(data=>{
      this.users = data.count;
    });
  }

}
