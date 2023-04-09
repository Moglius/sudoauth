import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditLdapgroupComponent } from './add-edit-ldapgroup.component';

describe('AddEditLdapgroupComponent', () => {
  let component: AddEditLdapgroupComponent;
  let fixture: ComponentFixture<AddEditLdapgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditLdapgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditLdapgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
