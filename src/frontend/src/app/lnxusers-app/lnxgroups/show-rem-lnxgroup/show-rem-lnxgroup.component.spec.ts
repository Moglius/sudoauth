import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemLnxgroupComponent } from './show-rem-lnxgroup.component';

describe('ShowRemLnxgroupComponent', () => {
  let component: ShowRemLnxgroupComponent;
  let fixture: ComponentFixture<ShowRemLnxgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemLnxgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemLnxgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
