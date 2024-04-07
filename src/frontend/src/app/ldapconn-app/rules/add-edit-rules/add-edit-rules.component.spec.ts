import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditRulesComponent } from './add-edit-rules.component';

describe('AddEditRulesComponent', () => {
  let component: AddEditRulesComponent;
  let fixture: ComponentFixture<AddEditRulesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditRulesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditRulesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
