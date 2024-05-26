import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LnxusersComponent } from './lnxusers-app/lnxusers/lnxusers.component';
import { LnxgroupsComponent } from './lnxusers-app/lnxgroups/lnxgroups.component';
import { LnxshellsComponent } from './lnxusers-app/lnxshells/lnxshells.component';
import { LdapusersComponent } from './ldapconn-app/ldapusers/ldapusers.component';
import { LdapgroupsComponent } from './ldapconn-app/ldapgroups/ldapgroups.component';
import { RulesComponent } from './ldapconn-app/rules/rules.component';
import { SudorulesComponent } from './sudoers-app/sudorules/sudorules.component';
import { HostsComponent } from './sudoers-app/hosts/hosts.component';
import { CommandsComponent } from './sudoers-app/commands/commands.component';
import { SudorolesComponent } from './sudoers-app/sudoroles/sudoroles.component';
import { HostgroupsComponent } from './sudoers-app/hostgroups/hostgroups.component';
import { AddEditSudoroleComponent } from './sudoers-app/sudoroles/add-edit-sudorole/add-edit-sudorole.component';
import { DashboardAppComponent } from './dashboard-app/dashboard-app.component';
import { AddEditHostgroupComponent } from './sudoers-app/hostgroups/add-edit-hostgroup/add-edit-hostgroup.component';
import { AddEditSudorulesComponent } from './sudoers-app/sudorules/add-edit-sudorules/add-edit-sudorules.component';
import { LoginAppComponent } from './login-app/login-app.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
  {path: 'lnxusers', component: LnxusersComponent, canActivate: [authGuard]},
  {path: 'lnxgroups', component: LnxgroupsComponent, canActivate: [authGuard]},
  {path: 'lnxshells', component: LnxshellsComponent, canActivate: [authGuard]},
  {path: 'ldapusers', component: LdapusersComponent, canActivate: [authGuard]},
  {path: 'ldapgroups', component: LdapgroupsComponent, canActivate: [authGuard]},
  {path: 'ldaprules', component: RulesComponent, canActivate: [authGuard]},
  {path: 'sudorules', component: SudorulesComponent, canActivate: [authGuard]},
  {path: 'sudorules/create', component: AddEditSudorulesComponent, canActivate: [authGuard]},
  {path: 'sudorules/edit/:id', component: AddEditSudorulesComponent, canActivate: [authGuard]},
  {path: 'sudoroles', component: SudorolesComponent, canActivate: [authGuard]},
  {path: 'sudoroles/create', component: AddEditSudoroleComponent, canActivate: [authGuard]},
  {path: 'sudoroles/edit/:id', component: AddEditSudoroleComponent, canActivate: [authGuard]},
  {path: 'commands', component: CommandsComponent, canActivate: [authGuard]},
  {path: 'hosts', component: HostsComponent, canActivate: [authGuard]},
  {path: 'hostgroups', component: HostgroupsComponent, canActivate: [authGuard]},
  {path: 'hostgroups/create', component: AddEditHostgroupComponent, canActivate: [authGuard]},
  {path: 'hostgroups/edit/:id', component: AddEditHostgroupComponent, canActivate: [authGuard]},
  {path: '', component: DashboardAppComponent, canActivate: [authGuard]},
  {path: 'login', component: LoginAppComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
