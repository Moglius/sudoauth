import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditSudorulesComponent } from './add-edit-sudorules.component';

describe('AddEditSudorulesComponent', () => {
  let component: AddEditSudorulesComponent;
  let fixture: ComponentFixture<AddEditSudorulesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditSudorulesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditSudorulesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
