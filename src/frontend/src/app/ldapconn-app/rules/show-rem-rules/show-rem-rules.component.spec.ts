import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemRulesComponent } from './show-rem-rules.component';

describe('ShowRemRulesComponent', () => {
  let component: ShowRemRulesComponent;
  let fixture: ComponentFixture<ShowRemRulesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemRulesComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemRulesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
