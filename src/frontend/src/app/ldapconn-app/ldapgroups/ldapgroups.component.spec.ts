import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LdapgroupsComponent } from './ldapgroups.component';

describe('LdapgroupsComponent', () => {
  let component: LdapgroupsComponent;
  let fixture: ComponentFixture<LdapgroupsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LdapgroupsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LdapgroupsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
