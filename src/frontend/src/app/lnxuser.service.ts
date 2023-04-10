import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LnxuserService {

  constructor(private http: HttpClient) { }

  getLnxUsersList(url: string): Observable<any>{
    return this.http.get<any>(url);
  }

  addEntry(url: string, val: any){
    return this.http.post(url, val)
  }

  updateEntry(url: string, val: any){
    return this.http.put(url, val)
  }

  deleteEntry(url: string, val: any){
    return this.http.delete(url + val)
  }
}
