import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditLnxgroupComponent } from './add-edit-lnxgroup.component';

describe('AddEditLnxgroupComponent', () => {
  let component: AddEditLnxgroupComponent;
  let fixture: ComponentFixture<AddEditLnxgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditLnxgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditLnxgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
