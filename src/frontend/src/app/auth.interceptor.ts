import { HttpInterceptorFn } from '@angular/common/http';

export const authInterceptor: HttpInterceptorFn = (request, next) => {
  console.log("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa");
  const token = localStorage.getItem('token') ?? '';
  request = request.clone({
    setHeaders: {
      Authorization: token ? `token ${token}` : '',
    },
  });

  return next(request);
};
