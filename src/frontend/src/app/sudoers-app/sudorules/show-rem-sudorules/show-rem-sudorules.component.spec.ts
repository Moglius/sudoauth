import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemSudorulesComponent } from './show-rem-sudorules.component';

describe('ShowRemSudorulesComponent', () => {
  let component: ShowRemSudorulesComponent;
  let fixture: ComponentFixture<ShowRemSudorulesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemSudorulesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemSudorulesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
