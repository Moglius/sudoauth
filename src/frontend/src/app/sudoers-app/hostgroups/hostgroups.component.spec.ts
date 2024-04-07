import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HostgroupsComponent } from './hostgroups.component';

describe('HostgroupsComponent', () => {
  let component: HostgroupsComponent;
  let fixture: ComponentFixture<HostgroupsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HostgroupsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HostgroupsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
