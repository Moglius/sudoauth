import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemCommandComponent } from './show-rem-command.component';

describe('ShowRemCommandComponent', () => {
  let component: ShowRemCommandComponent;
  let fixture: ComponentFixture<ShowRemCommandComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemCommandComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemCommandComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
