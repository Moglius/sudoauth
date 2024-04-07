import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowRemHostgroupComponent } from './show-rem-hostgroup.component';

describe('ShowRemHostgroupComponent', () => {
  let component: ShowRemHostgroupComponent;
  let fixture: ComponentFixture<ShowRemHostgroupComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ShowRemHostgroupComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ShowRemHostgroupComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
