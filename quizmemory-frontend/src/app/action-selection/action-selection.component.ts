import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-action-selection',
  standalone: true,
  imports: [],
  templateUrl: './action-selection.component.html',
  styleUrl: './action-selection.component.css'
})
export class ActionSelectionComponent implements OnInit {
  constructor(private route: ActivatedRoute, private router: Router){}

  quizId : any;
  quizName:any;

  gotoPlay(){
    let quizId = this.quizId;
    this.router.navigate(['/quiz-play'], { queryParams: { quizId } });
  }
  gotoLeaderBoards(){
    let quizId = this.quizId;
    this.router.navigate(['/quiz-leaderboards'], { queryParams: { quizId } });
  }
  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      this.quizId = params['quizId'];
      this.quizName = `Quiz ${this.quizId}`;
    });
  }
}
