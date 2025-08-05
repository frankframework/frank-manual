import { afterRender, Component, computed, effect, ElementRef, input, OnChanges, OnInit, SimpleChanges, ViewChild } from "@angular/core";
import mermaid from 'mermaid'
import { v4 as uuidv4 } from 'uuid'

@Component({
  selector: 'mermaid-diagram',
  template: '<div class="{{ is_mermaid() }}" #mermaidElement>{{ innerHtml() }}</div>'
})
export class DiagramComponent implements OnInit {
  inputMermaid = input.required<string | null>()
  is_mermaid = computed<string>(() => this.inputMermaid() === null ? '' : 'mermaid')
  innerHtml = computed<string>(() => this.inputMermaid() === null ? 'Loading...' : this.inputMermaid()!)

  @ViewChild('mermaidElement')
  mermaidEl: ElementRef<HTMLElement> | undefined

  element: HTMLElement | undefined

  constructor() {
    effect(() => {
      // Without this line, changes of the input are not properly seen.
      this.inputMermaid();
      this.updateMermaid();
    })
  }

  ngOnInit(): void {
    this.updateMermaid();
  }

  updateMermaid(): void {
    this.element = this.mermaidEl?.nativeElement;
    if (this.element !== undefined) {
      if (this.is_mermaid().length > 0) {
        const uid = `m${uuidv4()}`;
        void mermaid.render(uid, this.innerHtml(), this.element).then(({svg}) => {
          this.element!.innerHTML = svg
        })
      } else {
        this.element.innerHTML = this.innerHtml();
      }
    }
  }
}
