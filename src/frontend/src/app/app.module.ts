import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LnxusersComponent } from './lnxusers-app/lnxusers/lnxusers.component';
import { LnxgroupsComponent } from './lnxusers-app/lnxgroups/lnxgroups.component';
import { ShowRemLnxuserComponent } from './lnxusers-app/lnxusers/show-rem-lnxuser/show-rem-lnxuser.component';
import { AddEditLnxuserComponent } from './lnxusers-app/lnxusers/add-edit-lnxuser/add-edit-lnxuser.component';
import { ShowRemLnxgroupComponent } from './lnxusers-app/lnxgroups/show-rem-lnxgroup/show-rem-lnxgroup.component';
import { AddEditLnxgroupComponent } from './lnxusers-app/lnxgroups/add-edit-lnxgroup/add-edit-lnxgroup.component';
import { LnxuserService } from './lnxuser.service';

import { HttpClientModule, provideHttpClient, withInterceptors } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { LnxshellsComponent } from './lnxusers-app/lnxshells/lnxshells.component';
import { AddEditLnxshellComponent } from './lnxusers-app/lnxshells/add-edit-lnxshell/add-edit-lnxshell.component';
import { ShowRemLnxshellComponent } from './lnxusers-app/lnxshells/show-rem-lnxshell/show-rem-lnxshell.component';
import { LdapusersComponent } from './ldapconn-app/ldapusers/ldapusers.component';
import { LdapgroupsComponent } from './ldapconn-app/ldapgroups/ldapgroups.component';
import { RulesComponent } from './ldapconn-app/rules/rules.component';
import { AddEditLdapuserComponent } from './ldapconn-app/ldapusers/add-edit-ldapuser/add-edit-ldapuser.component';
import { ShowRemLdapuserComponent } from './ldapconn-app/ldapusers/show-rem-ldapuser/show-rem-ldapuser.component';
import { ShowRemLdapgroupComponent } from './ldapconn-app/ldapgroups/show-rem-ldapgroup/show-rem-ldapgroup.component';
import { AddEditLdapgroupComponent } from './ldapconn-app/ldapgroups/add-edit-ldapgroup/add-edit-ldapgroup.component';
import { AddEditRulesComponent } from './ldapconn-app/rules/add-edit-rules/add-edit-rules.component';
import { ShowRemRulesComponent } from './ldapconn-app/rules/show-rem-rules/show-rem-rules.component';
import { SudorulesComponent } from './sudoers-app/sudorules/sudorules.component';
import { CommandsComponent } from './sudoers-app/commands/commands.component';
import { HostsComponent } from './sudoers-app/hosts/hosts.component';
import { ShowRemSudorulesComponent } from './sudoers-app/sudorules/show-rem-sudorules/show-rem-sudorules.component';
import { AddEditSudorulesComponent } from './sudoers-app/sudorules/add-edit-sudorules/add-edit-sudorules.component';
import { AddEditHostComponent } from './sudoers-app/hosts/add-edit-host/add-edit-host.component';
import { ShowRemHostComponent } from './sudoers-app/hosts/show-rem-host/show-rem-host.component';
import { ShowRemCommandComponent } from './sudoers-app/commands/show-rem-command/show-rem-command.component';
import { AddEditCommandComponent } from './sudoers-app/commands/add-edit-command/add-edit-command.component';
import { SudorolesComponent } from './sudoers-app/sudoroles/sudoroles.component';
import { ShowRemSudoroleComponent } from './sudoers-app/sudoroles/show-rem-sudorole/show-rem-sudorole.component';
import { AddEditSudoroleComponent } from './sudoers-app/sudoroles/add-edit-sudorole/add-edit-sudorole.component';
import { HostgroupsComponent } from './sudoers-app/hostgroups/hostgroups.component';
import { AddEditHostgroupComponent } from './sudoers-app/hostgroups/add-edit-hostgroup/add-edit-hostgroup.component';
import { ShowRemHostgroupComponent } from './sudoers-app/hostgroups/show-rem-hostgroup/show-rem-hostgroup.component';
import { LoginAppComponent } from './login-app/login-app.component';
import { authInterceptor } from './auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    LnxusersComponent,
    LnxgroupsComponent,
    ShowRemLnxuserComponent,
    AddEditLnxuserComponent,
    ShowRemLnxgroupComponent,
    AddEditLnxgroupComponent,
    LnxshellsComponent,
    AddEditLnxshellComponent,
    ShowRemLnxshellComponent,
    LdapusersComponent,
    LdapgroupsComponent,
    RulesComponent,
    AddEditLdapuserComponent,
    ShowRemLdapuserComponent,
    ShowRemLdapgroupComponent,
    AddEditLdapgroupComponent,
    AddEditRulesComponent,
    ShowRemRulesComponent,
    SudorulesComponent,
    CommandsComponent,
    HostsComponent,
    ShowRemSudorulesComponent,
    AddEditSudorulesComponent,
    AddEditHostComponent,
    ShowRemHostComponent,
    ShowRemCommandComponent,
    AddEditCommandComponent,
    SudorolesComponent,
    ShowRemSudoroleComponent,
    AddEditSudoroleComponent,
    HostgroupsComponent,
    AddEditHostgroupComponent,
    ShowRemHostgroupComponent,
    LoginAppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [
    LnxuserService,
    provideHttpClient(withInterceptors([authInterceptor]))
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
