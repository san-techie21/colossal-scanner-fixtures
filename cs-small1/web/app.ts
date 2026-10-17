// cs-small1 fixture: synthetic TypeScript written to be flagged. Never run.
function load(): void {
  console.log("loading");
}

export function start(): void {
  try { load(); } catch (e) {}
}
