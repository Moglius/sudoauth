import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LnxusersComponent } from './lnxusers.component';

describe('LnxusersComponent', () => {
  let component: LnxusersComponent;
  let fixture: ComponentFixture<LnxusersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LnxusersComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LnxusersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
