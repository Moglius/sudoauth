import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemSudoroleComponent } from './show-rem-sudorole.component';

describe('ShowRemSudoroleComponent', () => {
  let component: ShowRemSudoroleComponent;
  let fixture: ComponentFixture<ShowRemSudoroleComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemSudoroleComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemSudoroleComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
