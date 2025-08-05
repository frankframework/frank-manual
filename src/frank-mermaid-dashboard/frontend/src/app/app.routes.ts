import { Routes } from '@angular/router';
import { DiagramOverviewComponent } from './components/diagram-overview/diagram-overview.component';
import { RetrievedDiagramComponent } from './components/retrieved-diagram/retrieved-diagram.component';
import { EditDiagramComponent } from './components/edit-diagram/edit-diagram.component';

export const routes: Routes = [
  { path: 'diagram/:diagramName', component: RetrievedDiagramComponent, pathMatch: 'full' },
  { path: 'diagrams', component: DiagramOverviewComponent, pathMatch: 'full'},
  { path: 'edit-diagram/:diagramName/:isNew', component: EditDiagramComponent, pathMatch: 'full' },
  { path: '' , redirectTo: 'diagrams', pathMatch: 'full' }
];
