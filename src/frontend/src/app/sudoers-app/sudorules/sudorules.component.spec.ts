import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SudorulesComponent } from './sudorules.component';

describe('SudorulesComponent', () => {
  let component: SudorulesComponent;
  let fixture: ComponentFixture<SudorulesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SudorulesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SudorulesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
