import { HttpClient } from '@angular/common/http';
import { inject, Injectable, Signal } from '@angular/core';
import { Observable } from 'rxjs';

export interface LineStatus {
  lineNumber: number,
  isOk: boolean
}

export interface LineStatuses {
  diagramName: string,
  line: LineStatus[]
}

@Injectable({
  providedIn: 'root'
})
export class DiagramService {
  private http = inject(HttpClient)

  constructor() { }

  public getTemplate(name: string): Observable<string> {
    const url = `../../api/data/diagramTemplate/${name}`;
    return this.http.get(url, {responseType: 'text'});
  }

  public getBody(name: string): Observable<string> {
    const url = `../../api/data/diagramBody/${name}`;
    return this.http.get(url, {responseType: 'text'});
  }

  public getLineStatuses(name: string): Observable<LineStatuses> {
    const url = `../../api/data/diagramLineStatuses/${name}`;
    return this.http.get<LineStatuses>(url);
  }

  public setTemplate(diagramName: string, text: string): Observable<string> {
    const url = `../../api/data/diagram/${diagramName}`;
    return this.http.put(url, text, { responseType: 'text' });
  }
}
