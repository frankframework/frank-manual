import { interval, switchMap } from 'rxjs';
import { Component, inject, input, InputSignal, OnDestroy, OnInit } from '@angular/core';
import { Observable, Subscription } from 'rxjs';
import { DiagramService, LineStatuses } from '../../services/diagram.service';
import { buildShownMermaid } from '../../build-shown-mermaid';
import { DiagramComponent } from '../diagram/diagram.component';
import { RouterLink } from '@angular/router';

const POLLING_INTERVAl = 5000;

@Component({
  selector: 'app-retrieved-diagram',
  imports: [DiagramComponent, RouterLink],
  templateUrl: './retrieved-diagram.component.html',
  styleUrl: './retrieved-diagram.component.css'
})
export class RetrievedDiagramComponent implements OnInit, OnDestroy {
  public diagramName: InputSignal<string> = input.required<string>();
  public mermaid: string | null = null;
  service = inject(DiagramService);
  private body: string | undefined = undefined;
  private statuses: LineStatuses | undefined = undefined
  private body$: Observable<string> | undefined;
  private bodySubscription: Subscription | undefined;

  ngOnInit(): void {
    this.body$ = this.service.getBody(this.diagramName());
    interval(POLLING_INTERVAl)
      .pipe(switchMap(() => this.service.getLineStatuses(this.diagramName())))
      .subscribe(
        (statuses) => this.statusesReceived(statuses));
    this.bodySubscription = this.body$.subscribe((body) => this.bodyReceived(body));
  }

  ngOnDestroy(): void {
    if (this.bodySubscription) {
      this.bodySubscription.unsubscribe();
    }
  }
 
  private bodyReceived(body: string) {
    this.body = body;
    this.setOutputIfComplete();
  }

  private statusesReceived(statuses: LineStatuses) {
    this.statuses = statuses;
    this.setOutputIfComplete();
  }

  private setOutputIfComplete() {
    if (this.body !== undefined && this.statuses !== undefined) {
      this.mermaid = buildShownMermaid(this.body, this.statuses);
    }
  }
}
