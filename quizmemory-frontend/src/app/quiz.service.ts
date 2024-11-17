import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class QuizService {

  private apiUrl = 'http://localhost:5000'; // URL do backend

  constructor(private http: HttpClient) {}

  // Obter lista de quizzes
  getQuizzes(): Observable<any> {
    return this.http.get(`${this.apiUrl}/quiz`);
  }

  // Obter perguntas de um quiz específico
  getQuestions(quizId: string): Observable<any> {
    return this.http.get(`${this.apiUrl}/quiz/${quizId}/questions`);
  }

  // Obter perguntas de um quiz específico
  getLeaderboards(quizId: string,leaderboard_num:number): Observable<any> {
    return this.http.get(`${this.apiUrl}/quiz/${quizId}/leaderboards/${leaderboard_num}`);
  }

  // Enviar pontuação do usuário
  submitScore(quizId: number, score: number, username: string): Observable<any> {
    const payload = { quizId, score, username };
    return this.http.post(`${this.apiUrl}/scores`, payload);
  }

  // Enviar pontuação do usuário
  submitAnswer(quiz_num: number, question_num: number, student_id: string,time: number,selectedOption:string): Observable<any> {
    const payload = {
      time: time,
      student_id: student_id,
      answer: selectedOption
    };
    return this.http.post(`${this.apiUrl}/quiz/${quiz_num}/question/${question_num}/answer`, payload);
  }
}
