// Usage: node ax.mjs "<query>" max [abs|list]
const q = process.argv[2], max = parseInt(process.argv[3]||"10"), mode = process.argv[4]||"list";
const url = "https://export.arxiv.org/api/query?search_query=" + encodeURIComponent(q) + "&start=0&max_results=" + max;
const r = await fetch(url);
const x = await r.text();
const entries = x.split("<entry>").slice(1);
for (const b of entries) {
  const g = (re) => { const m = b.match(re); return m ? m[1].trim() : ""; };
  const id = g(/<id>([^<]+)/);
  const title = g(/<title>([\s\S]*?)<\/title>/).replace(/\s+/g, " ");
  const pub = g(/<published>([^<]+)<?/);
  const au = [...b.matchAll(/<name>([^<]+)</g)].map(m=>m[1]).join("; ");
  if (mode === "abs") {
    console.log("=".repeat(70));
    console.log(id, "| pub:", pub);
    console.log("T:", title);
    console.log("A:", au);
    console.log("S:", g(/<summary>([\s\S]*?)<\/summary>/).replace(/\s+/g, " ").slice(0, 1700));
    console.log();
  } else {
    console.log(id + " | " + pub.slice(0,10) + " | " + au + " | " + title);
  }
}
