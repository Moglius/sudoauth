import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditCommandComponent } from './add-edit-command.component';

describe('AddEditCommandComponent', () => {
  let component: AddEditCommandComponent;
  let fixture: ComponentFixture<AddEditCommandComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditCommandComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditCommandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
