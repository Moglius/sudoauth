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

const routes: Routes = [
  {path: 'lnxusers', component: LnxusersComponent},
  {path: 'lnxgroups', component: LnxgroupsComponent},
  {path: 'lnxshells', component: LnxshellsComponent},
  {path: 'ldapusers', component: LdapusersComponent},
  {path: 'ldapgroups', component: LdapgroupsComponent},
  {path: 'ldaprules', component: RulesComponent},
  {path: 'sudorules', component: SudorulesComponent},
  {path: 'sudoroles', component: SudorolesComponent},
  {path: 'sudoroles/create', component: AddEditSudoroleComponent},
  {path: 'commands', component: CommandsComponent},
  {path: 'hosts', component: HostsComponent},
  {path: 'hostgroups', component: HostgroupsComponent},
  {path: '', component: DashboardAppComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
