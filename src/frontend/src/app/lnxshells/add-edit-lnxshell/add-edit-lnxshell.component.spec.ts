import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditLnxshellComponent } from './add-edit-lnxshell.component';

describe('AddEditLnxshellComponent', () => {
  let component: AddEditLnxshellComponent;
  let fixture: ComponentFixture<AddEditLnxshellComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditLnxshellComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditLnxshellComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
