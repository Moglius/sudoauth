import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditLnxuserComponent } from './add-edit-lnxuser.component';

describe('AddEditLnxuserComponent', () => {
  let component: AddEditLnxuserComponent;
  let fixture: ComponentFixture<AddEditLnxuserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditLnxuserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditLnxuserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
