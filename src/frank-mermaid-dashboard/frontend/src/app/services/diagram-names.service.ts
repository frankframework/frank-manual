import { HttpClient } from '@angular/common/http';
import { inject, Injectable, input, Input, OnInit, Signal } from '@angular/core';
import { BehaviorSubject, Observable, switchMap } from 'rxjs'
import { toSignal } from '@angular/core/rxjs-interop';

@Injectable({
  providedIn: 'root'
})
export class DiagramNamesService {
  private static URL = '../../api/data/diagramNames'

  private http = inject(HttpClient)

  private trigger = new BehaviorSubject(0);

  public diagramNames: Signal<String[] | undefined> = toSignal(
    this.trigger.pipe(switchMap(() =>
      this.http.get<String[]>(DiagramNamesService.URL)
    ))
  );

  constructor() { }

  public reload() {
    this.trigger.next(0);
  }
}
