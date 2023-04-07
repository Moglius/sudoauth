import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LnxusersComponent } from './lnxusers/lnxusers.component';
import { LnxgroupsComponent } from './lnxgroups/lnxgroups.component';
import { LnxshellsComponent } from './lnxshells/lnxshells.component';

const routes: Routes = [
  {path: 'lnxusers', component: LnxusersComponent},
  {path: 'lnxgroups', component: LnxgroupsComponent},
  {path: 'lnxshells', component: LnxshellsComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
