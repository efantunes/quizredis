import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';


@Component({
  selector: 'app-login',
  standalone: true,
  imports: [FormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.css'
})
export class LoginComponent {
  username = '';

  constructor(private router: Router) {}

  login() {
    if (this.username) {
      // Salva o nome de usuário no localStorage ou serviço
      sessionStorage.setItem('username', this.username);
      this.router.navigate(['/quiz-selection']);
    }
  }
}
