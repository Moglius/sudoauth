import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditSudoroleComponent } from './add-edit-sudorole.component';

describe('AddEditSudoroleComponent', () => {
  let component: AddEditSudoroleComponent;
  let fixture: ComponentFixture<AddEditSudoroleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditSudoroleComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditSudoroleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
