import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { QuizService } from '../quiz.service';
import { KeyValuePipe, NgFor, NgIf } from '@angular/common';

@Component({
  selector: 'app-leaderboard',
  standalone: true,
  imports: [NgFor,KeyValuePipe,NgIf],
  templateUrl: './leaderboard.component.html',
  styleUrl: './leaderboard.component.css'
})
export class LeaderboardComponent implements OnInit {

  @Input() leaderboardId: number = 0;
  @Input() quizNum: string = "";

  positions:Array<any>=[];

  constructor(private route: ActivatedRoute, private router: Router,private quizService:QuizService){}

  ngOnInit() {
    this.quizService.getLeaderboards(this.quizNum,this.leaderboardId).subscribe(x => {this.positions = x;})
  }
}
