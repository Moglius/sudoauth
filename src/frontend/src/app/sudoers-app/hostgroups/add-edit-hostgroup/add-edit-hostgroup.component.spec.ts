import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditHostgroupComponent } from './add-edit-hostgroup.component';

describe('AddEditHostgroupComponent', () => {
  let component: AddEditHostgroupComponent;
  let fixture: ComponentFixture<AddEditHostgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditHostgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditHostgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
