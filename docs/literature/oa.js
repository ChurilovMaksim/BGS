// OpenAlex search: node oa.js "query" [perpage] [filter]
const https = require('https');
const q = process.argv[2];
const per = process.argv[3] || 12;
const filter = process.argv[4] || '';
let url = 'https://api.openalex.org/works?search=' + encodeURIComponent(q) +
  '&per-page=' + per + '&mailto=lit@example.org';
if (filter) url += '&filter=' + encodeURIComponent(filter);
https.get(url, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    let j;
    try { j = JSON.parse(s); } catch (e) { console.log('RAW:' + s.slice(0, 1200)); return; }
    if (!j.results) { console.log(JSON.stringify(j).slice(0, 1200)); return; }
    console.log('QUERY: ' + q + '  count=' + (j.meta && j.meta.count));
    for (const p of j.results) {
      console.log('---');
      console.log('T: ' + p.title);
      console.log('A: ' + (p.authorships || []).map(a => a.author.display_name).join(', '));
      const loc = p.primary_location || {};
      const src = loc.source || {};
      console.log('Y: ' + p.publication_year + ' | ' + (src.display_name || '') + ' vol ' + (p.biblio && p.biblio.volume) + ' iss ' + (p.biblio && p.biblio.issue) + ' pp ' + (p.biblio && p.biblio.first_page) + '-' + (p.biblio && p.biblio.last_page));
      console.log('DOI: ' + p.doi + ' | type ' + p.type + ' | cited_by ' + p.cited_by_count);
      const ids = p.ids || {};
      if (ids.mag || ids.pmid) console.log('OTHERIDS: ' + JSON.stringify(ids));
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
