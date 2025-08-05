import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DiagramOverviewComponent } from './diagram-overview.component';
import { provideHttpClient } from '@angular/common/http';

describe('DiagramOverviewComponent', () => {
  let component: DiagramOverviewComponent;
  let fixture: ComponentFixture<DiagramOverviewComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DiagramOverviewComponent],
      providers: [
        provideHttpClient()
      ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DiagramOverviewComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
