import { TestBed } from '@angular/core/testing';

import { LnxuserService } from './lnxuser.service';

describe('LnxuserService', () => {
  let service: LnxuserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LnxuserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
