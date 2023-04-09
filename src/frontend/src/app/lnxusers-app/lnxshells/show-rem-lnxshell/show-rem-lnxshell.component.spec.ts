import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemLnxshellComponent } from './show-rem-lnxshell.component';

describe('ShowRemLnxshellComponent', () => {
  let component: ShowRemLnxshellComponent;
  let fixture: ComponentFixture<ShowRemLnxshellComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemLnxshellComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemLnxshellComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
