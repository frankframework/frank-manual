import { Component, inject, input, OnDestroy, OnInit } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { DiagramService } from '../../services/diagram.service';
import { catchError, Observable, Subscription } from 'rxjs';
import { Router, RouterLink } from '@angular/router';
import { HttpErrorResponse } from '@angular/common/http';

type NEW_STATE = "new" | "existing";

@Component({
  selector: 'app-edit-diagram',
  imports: [ReactiveFormsModule, RouterLink],
  templateUrl: './edit-diagram.component.html',
  styleUrl: './edit-diagram.component.css'
})
export class EditDiagramComponent implements OnInit, OnDestroy {
  private router = inject(Router);
  public diagramName = input.required<string>();
  public newState = input.required<NEW_STATE>();
  private diagramService = inject(DiagramService);
  public diagramText = new FormControl<string>({ value: '', disabled: true });
  public canSubmit = false;
  private originalTextSubscription: Subscription | undefined;
  private submitTemplateSubscription: Subscription | undefined;

  ngOnInit(): void {
    if (this.newState() === "new") {
      this.enable();
    } else {
      this.originalTextSubscription = this.diagramService.getTemplate(this.diagramName()).subscribe((text) => {
        this.diagramText.setValue(text);
        this.enable();
      })
    }
  }

  private enable(): void {
    this.diagramText.enable();
    this.canSubmit = true;
  }

  private disable(): void {
    this.diagramText.disable();
    this.canSubmit = false;
  }

  ngOnDestroy(): void {
    if (this.originalTextSubscription !== undefined) {
      this.originalTextSubscription.unsubscribe();
    }
    if (this.submitTemplateSubscription !== undefined) {
      this.submitTemplateSubscription.unsubscribe();
    }
  }

  public submit(): void {
    this.disable();
    this.submitTemplateSubscription = this.diagramService.setTemplate(this.diagramName(), this.getDiagramTextToSubmit())
      .subscribe({
        next: () => { this.router.navigateByUrl('/diagrams') },
        error: (err) => { alert(err) }
    })
  }

  private getDiagramTextToSubmit(): string {
    return this.diagramText.value === null ? '' : this.diagramText.value;
  }
}
