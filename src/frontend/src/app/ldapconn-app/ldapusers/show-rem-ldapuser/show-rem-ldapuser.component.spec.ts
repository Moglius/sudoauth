import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemLdapuserComponent } from './show-rem-ldapuser.component';

describe('ShowRemLdapuserComponent', () => {
  let component: ShowRemLdapuserComponent;
  let fixture: ComponentFixture<ShowRemLdapuserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemLdapuserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemLdapuserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
