import { TestBed } from '@angular/core/testing';

import { DiagramService } from './diagram.service';
import { provideHttpClient } from '@angular/common/http';
import { HttpTestingController, provideHttpClientTesting } from '@angular/common/http/testing';
import { Signal } from '@angular/core';
import { firstValueFrom, Observable } from 'rxjs';

describe('DiagramService', () => {
  let service: DiagramService;
  let httpTesting: HttpTestingController;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        DiagramService,
        provideHttpClient(),
        provideHttpClientTesting()
      ]
    });
    httpTesting = TestBed.inject(HttpTestingController);
    service = TestBed.inject(DiagramService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('when a diagram exists, its template can be retrieved', (done) => {
    const template$: Observable<string> = service.getTemplate('myTemplate')
    firstValueFrom(template$).then((response) => {
      expect(response).toEqual('My template')
      done()
    })
    let req = httpTesting.expectOne(() => true);
    req.flush('My template');
  })

  it('when the requested diagram does not exist, an error is thrown', (done) => {
    const template$: Observable<string> = service.getTemplate('myTemplate')
    firstValueFrom(template$).catch((error) => {
      expect(error).not.toEqual(undefined);
      done()
    })
    let req = httpTesting.expectOne(() => true);
    req.flush('Something went wrong', {status: 500, statusText: 'Internal server error'});
  })
});
