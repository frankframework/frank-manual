import { Component, computed, inject, OnInit, Signal } from '@angular/core';
import { DiagramNamesService } from '../../services/diagram-names.service';
import { Router, RouterLink } from '@angular/router';
import { FormControl, ReactiveFormsModule } from '@angular/forms';

@Component({
  selector: 'app-diagram-overview',
  imports: [RouterLink, ReactiveFormsModule],
  templateUrl: './diagram-overview.component.html',
  styleUrl: './diagram-overview.component.css'
})
export class DiagramOverviewComponent implements OnInit {
  private diagramNamesService = inject(DiagramNamesService)
  private router = inject(Router);
  private diagramNames: Signal<String[] | undefined> = this.diagramNamesService.diagramNames;
  public cannotDownloadNames: Signal<boolean> = computed(() => this.diagramNames() === undefined);
  public shownNames: Signal<String[]> = computed(
    () => this.cannotDownloadNames() === true ? [] : this.diagramNames()!
  );
  public newDiagramName = new FormControl<string>({ value: '', disabled: false})

  ngOnInit(): void {
    this.reload();
  }

  public reload() {
    this.diagramNamesService.reload();
  }

  newDiagram() {
    if (this.newDiagramName.value?.length === 0) {
      alert('Please enter a name for the diagram you want to create.')
    } else {
      this.router.navigateByUrl(`edit-diagram/${this.newDiagramName.value}/new`)
    }
  }
}
