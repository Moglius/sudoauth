import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SudorolesComponent } from './sudoroles.component';

describe('SudorolesComponent', () => {
  let component: SudorolesComponent;
  let fixture: ComponentFixture<SudorolesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SudorolesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SudorolesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
