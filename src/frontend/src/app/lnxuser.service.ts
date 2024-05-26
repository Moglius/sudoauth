import { Injectable, signal } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { UserInterface } from './user.interface';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class LnxuserService {

  constructor(private http: HttpClient, private router: Router) { }

  currentUserSig = signal<UserInterface | undefined | null>(undefined);

  getLnxUsersList(url: string): Observable<any>{
    return this.http.get<any>(url);
  }

  addEntry(url: string, val: any){
    return this.http.post(url, val)
  }

  updateEntry(url: string, val: any){
    return this.http.patch(url, val);
  }

  deleteEntry(url: string){
    return this.http.delete(url);
  }

  loginUser(username: string, password: string){
    this.http.post<UserInterface>('http://localhost:8000/api/accounts/auth/',
      { "username": username, "password": password }).subscribe((response) => {
        console.log('response', response);
        localStorage.setItem('token', response.token);
        this.currentUserSig.set(response);
        this.router.navigate([""]);
        window.location.reload();
    });
  }

  public isAuthenticated() : boolean {
    const token = localStorage.getItem('token');
    return token != null;
  }
}
