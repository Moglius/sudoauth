import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LnxusersComponent } from './lnxusers/lnxusers.component';
import { LnxgroupsComponent } from './lnxgroups/lnxgroups.component';
import { ShowRemLnxuserComponent } from './lnxusers/show-rem-lnxuser/show-rem-lnxuser.component';
import { AddEditLnxuserComponent } from './lnxusers/add-edit-lnxuser/add-edit-lnxuser.component';
import { ShowRemLnxgroupComponent } from './lnxgroups/show-rem-lnxgroup/show-rem-lnxgroup.component';
import { AddEditLnxgroupComponent } from './lnxgroups/add-edit-lnxgroup/add-edit-lnxgroup.component';
import { LnxuserService } from './lnxuser.service';

import { HttpClientModule } from '@angular/common/http';
import { FormsModule,ReactiveFormsModule } from '@angular/forms';
import { LnxshellsComponent } from './lnxshells/lnxshells.component';
import { AddEditLnxshellComponent } from './lnxshells/add-edit-lnxshell/add-edit-lnxshell.component';
import { ShowRemLnxshellComponent } from './lnxshells/show-rem-lnxshell/show-rem-lnxshell.component';

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
    ShowRemLnxshellComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
  ],
  providers: [LnxuserService],
  bootstrap: [AppComponent]
})
export class AppModule { }
