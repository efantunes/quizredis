import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { QuizPlayComponent } from './quiz-play/quiz-play.component';
import { QuizSelectionComponent } from './quiz-selection/quiz-selection.component';
import { ActionSelectionComponent } from './action-selection/action-selection.component';
import { QuizLeaderboardsComponent } from './quiz-leaderboards/quiz-leaderboards.component';

export const routes: Routes = [
    { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'quiz-selection', component: QuizSelectionComponent },
  { path: 'quiz-play', component: QuizPlayComponent },
  { path: 'action-selection', component: ActionSelectionComponent },
  { path: 'quiz-leaderboards', component: QuizLeaderboardsComponent },
];
