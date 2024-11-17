import { ComponentFixture, TestBed } from '@angular/core/testing';

import { QuizLeaderboardsComponent } from './quiz-leaderboards.component';

describe('QuizLeaderboardsComponent', () => {
  let component: QuizLeaderboardsComponent;
  let fixture: ComponentFixture<QuizLeaderboardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [QuizLeaderboardsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(QuizLeaderboardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
