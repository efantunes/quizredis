import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { QuizPlayComponent } from './quiz-play/quiz-play.component';
import { QuizSelectionComponent } from './quiz-selection/quiz-selection.component';

export const routes: Routes = [
    { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'quiz-selection', component: QuizSelectionComponent },
  { path: 'quiz-play', component: QuizPlayComponent },
];
