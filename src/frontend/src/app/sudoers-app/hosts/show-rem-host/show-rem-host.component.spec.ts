import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemHostComponent } from './show-rem-host.component';

describe('ShowRemHostComponent', () => {
  let component: ShowRemHostComponent;
  let fixture: ComponentFixture<ShowRemHostComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemHostComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemHostComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
