import { Component,OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { QuizService } from '../quiz.service';
import { AsyncPipe, NgFor } from '@angular/common';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-quiz-selection',
  standalone: true,
  imports: [NgFor,AsyncPipe],
  templateUrl: './quiz-selection.component.html',
  styleUrl: './quiz-selection.component.css'
})
export class QuizSelectionComponent implements OnInit {
  quizzes!: Array<any> ;

  constructor(private router: Router, private quizService:QuizService) {}
  
  ngOnInit(): void {
    console.log('HEY')
    this.quizService.getQuizzes().subscribe(quizz =>{ this.quizzes=quizz});
  }

  selectQuiz(quizId: string) {
    this.router.navigate(['/quiz-play'], { queryParams: { quizId } });
  }
}
