import { NgFor, NgIf } from '@angular/common';
import { Component, OnInit  } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { QuizService } from '../quiz.service';

@Component({
  selector: 'app-quiz-play',
  standalone: true,
  imports: [NgFor,NgIf],
  templateUrl: './quiz-play.component.html',
  styleUrl: './quiz-play.component.css'
})
export class QuizPlayComponent implements OnInit {
  quizId: string | null = null;
  quizName = '';
  questions: Array<any> =[];
  currentQuestionIndex = 0;
  currentQuestion :any = this.questions[0];
  score = 0;
  maxTimePerQuestion = 20;
  timeLeft = 20; // 60 segundos para o quiz

  timer: any;

  constructor(private route: ActivatedRoute, private router: Router,private quizService:QuizService) {}

  ngOnInit() {
    this.route.queryParams.subscribe((params) => {
      this.quizId = params['quizId'];
      this.quizName = `Quiz ${this.quizId}`;
      let a:string = params['quizId'];

      this.quizService.getQuestions(a.split(':')[1]).subscribe(questionss =>{ this.questions=questionss;this.currentQuestion=this.questions[0];});
    });

    this.startTimer();
  }

  resetTimer() {
    clearInterval(this.timer);
    this.timeLeft = this.maxTimePerQuestion
  }

  startTimer() {
    this.timer = setInterval(() => {
      this.timeLeft--;
      if (this.timeLeft <= 0) {
        let timeToAnswer = this.maxTimePerQuestion+1;
        let quiz_num:any = this.quizId?.split(':')[1];
        let question_num:any = this.currentQuestion.id.split(":")[3];
        let username:any = sessionStorage.getItem('username');
        this.quizService.submitAnswer(quiz_num,question_num,username,timeToAnswer,"invalid").subscribe(x=>x);
        // this.resetTimer();
        this.nextQuestion();
      }
    }, 1000);
  }

  selectAnswer(option: string) {
    let currentTime = this.timeLeft;
    let timeToAnswer = this.maxTimePerQuestion - currentTime;
    let quiz_num:any = this.quizId?.split(':')[1];
    let question_num:any = this.currentQuestion.id.split(":")[3];
    let username:any = sessionStorage.getItem('username');
    this.quizService.submitAnswer(quiz_num,question_num,username,timeToAnswer,option).subscribe(x=>x);
    if (this.currentQuestion.answer === option) {
      this.score++;
    }
    this.nextQuestion();
  }

  nextQuestion() {
    this.currentQuestionIndex++;
    if (this.currentQuestionIndex < this.questions.length) {
      
      this.resetTimer();
      this.startTimer();
      this.currentQuestion = this.questions[this.currentQuestionIndex];
    } else {
      this.endQuiz();
    }
  }

  endQuiz() {
    clearInterval(this.timer);
    this.currentQuestion = null; // Indica que o quiz terminou
  }
}
