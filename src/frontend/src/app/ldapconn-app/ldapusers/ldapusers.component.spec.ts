import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LdapusersComponent } from './ldapusers.component';

describe('LdapusersComponent', () => {
  let component: LdapusersComponent;
  let fixture: ComponentFixture<LdapusersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LdapusersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LdapusersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
