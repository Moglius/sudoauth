import { Component } from '@angular/core';
import { LnxuserService } from './lnxuser.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  constructor(private service: LnxuserService, private router: Router) {  }

  title = 'frontend';
  isLogIn = false;

  ngOnInit(): void {
    this.isLogIn = this.service.isAuthenticated();
  }

  logout(){
    localStorage.clear();
    this.isLogIn = false;
    this.router.navigateByUrl("/login");
  }
}
