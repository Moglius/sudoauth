import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LnxgroupsComponent } from './lnxgroups.component';

describe('LnxgroupsComponent', () => {
  let component: LnxgroupsComponent;
  let fixture: ComponentFixture<LnxgroupsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LnxgroupsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LnxgroupsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
