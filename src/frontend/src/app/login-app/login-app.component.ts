import { Component } from '@angular/core';
import { LnxuserService } from '../lnxuser.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login-app',
  templateUrl: './login-app.component.html',
  styleUrl: './login-app.component.css'
})
export class LoginAppComponent {

  constructor(private service: LnxuserService, private router: Router) {  }

  username : string = "";
  password : string = "";

  ngOnInit(): void {
    this.username = "";
    this.password = "";
    console.log(this.service.currentUserSig());
    if (this.service.isAuthenticated()) {
      this.router.navigate([""]);
    }
  }

  login(username: string, password: string){
    console.log(username, password);
    this.service.loginUser(username, password);
  }
}
