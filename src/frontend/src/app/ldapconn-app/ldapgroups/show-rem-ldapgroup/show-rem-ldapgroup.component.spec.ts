import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemLdapgroupComponent } from './show-rem-ldapgroup.component';

describe('ShowRemLdapgroupComponent', () => {
  let component: ShowRemLdapgroupComponent;
  let fixture: ComponentFixture<ShowRemLdapgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemLdapgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemLdapgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
