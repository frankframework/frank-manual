import { TestBed } from '@angular/core/testing';
import { HttpClient, provideHttpClient } from '@angular/common/http';
import { DiagramNamesService } from './diagram-names.service';
import { HttpTestingController, provideHttpClientTesting, TestRequest } from '@angular/common/http/testing';

describe('DiagramNamesService', () => {
  let httpTesting: HttpTestingController;
  let service: DiagramNamesService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [
        DiagramNamesService,
        provideHttpClient(),
        provideHttpClientTesting(),
      ]
    });
    httpTesting = TestBed.inject(HttpTestingController);
    service = TestBed.inject(DiagramNamesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('When server returns list of diagram names, then names are returned as string[]', () => {
    const req: TestRequest = httpTesting.expectOne(() => true);
    req.flush(['first', 'second']);
    const value: String[] | undefined = service.diagramNames();
    expect(value).toEqual(['first', 'second']);
  })

  it('When server returns error, then an exception is thrown', () => {
    const req: TestRequest = httpTesting.expectOne(() => true);
    req.flush('Something went wrong', {status: 500, statusText: 'Internal server error'});
    let caught = false;
    try {
      service.diagramNames();
    }
    catch(_) {
      caught = true
    }
    expect(caught).toBeTrue();
  })

  it('When reload() is called, then the diagram names are refreshed', () => {
    const req: TestRequest = httpTesting.expectOne(() => true);
    req.flush(['first', 'second']);
    const value: String[] | undefined = service.diagramNames();
    expect(value).toEqual(['first', 'second']);
    httpTesting.expectNone(() => true);
    const secondValue = service.diagramNames();
    expect(secondValue).toEqual(value);
    service.reload();
    const reqAfterTrigger: TestRequest = httpTesting.expectOne(() => true);
    reqAfterTrigger.flush(['first']);
    const valueAfter = service.diagramNames();
    expect(valueAfter).toEqual(['first']);
    httpTesting.verify();
  })
});
