import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemLnxuserComponent } from './show-rem-lnxuser.component';

describe('ShowRemLnxuserComponent', () => {
  let component: ShowRemLnxuserComponent;
  let fixture: ComponentFixture<ShowRemLnxuserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemLnxuserComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemLnxuserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
