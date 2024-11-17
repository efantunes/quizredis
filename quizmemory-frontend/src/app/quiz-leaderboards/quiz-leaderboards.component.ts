import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { LeaderboardComponent } from '../leaderboard/leaderboard.component';

@Component({
  selector: 'app-quiz-leaderboards',
  standalone: true,
  imports: [LeaderboardComponent],
  templateUrl: './quiz-leaderboards.component.html',
  styleUrl: './quiz-leaderboards.component.css'
})
export class QuizLeaderboardsComponent implements OnInit {
  quizId:any;
  quizName:any;
  quizNum:any;
  constructor(private route: ActivatedRoute, private router: Router){}
  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      this.quizId = params['quizId'];
      this.quizName = `Quiz ${this.quizId}`;
      this.quizNum=this.quizId.split(":")[1];
    });
  }

}
