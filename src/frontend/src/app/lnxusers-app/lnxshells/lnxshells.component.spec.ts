import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LnxshellsComponent } from './lnxshells.component';

describe('LnxshellsComponent', () => {
  let component: LnxshellsComponent;
  let fixture: ComponentFixture<LnxshellsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LnxshellsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LnxshellsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
