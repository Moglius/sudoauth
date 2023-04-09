import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditLdapuserComponent } from './add-edit-ldapuser.component';

describe('AddEditLdapuserComponent', () => {
  let component: AddEditLdapuserComponent;
  let fixture: ComponentFixture<AddEditLdapuserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditLdapuserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditLdapuserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
