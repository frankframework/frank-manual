import { LineStatuses } from "./services/diagram.service";

export function buildShownMermaid(body: string, statuses: LineStatuses): string {
  if (statuses.line === undefined) {
    return body;
  }
  const good: string = statuses.line
    .filter((line) => line.isOk)
    .map((line) => `${line.lineNumber}`)
    .map((lineNumber) => `linkStyle ${lineNumber} stroke:lightgreen\n`)
    .join('')
  const bad: string = statuses.line
    .filter((line) => ! line.isOk)
    .map((line) => `${line.lineNumber}`)
    .map((lineNumber) => `linkStyle ${lineNumber} stroke:red\n`)
    .join('');
  return `${body}\n${good}\n${bad}`;
}