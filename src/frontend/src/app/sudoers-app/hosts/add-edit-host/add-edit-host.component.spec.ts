import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddEditHostComponent } from './add-edit-host.component';

describe('AddEditHostComponent', () => {
  let component: AddEditHostComponent;
  let fixture: ComponentFixture<AddEditHostComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AddEditHostComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AddEditHostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
