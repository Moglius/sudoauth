import { CanActivateFn, Router } from '@angular/router';
import { LnxuserService } from './lnxuser.service';
import { inject } from '@angular/core';

export const authGuard: CanActivateFn = (route, state) => {
  const service: LnxuserService = inject(LnxuserService);
  const router: Router = inject(Router);

  if (service.isAuthenticated()) {
    return true;
  }else{
    router.navigateByUrl("/login");
    return false;
  }
};
