// OpenAlex full search with abstract: node oa2.js "search terms" [perpage] [extraFilter]
const https = require('https');
const q = process.argv[2];
const per = process.argv[3] || 25;
const extra = process.argv[4] || '';
let filter = 'abstract.search:' + q;
if (extra) filter += ',' + extra;
const url = 'https://api.openalex.org/works?filter=' + encodeURIComponent(filter) +
  '&per-page=' + per + '&mailto=lit@example.org&select=id,doi,title,display_name,publication_year,authorships,primary_location,biblio,type,cited_by_count,abstract_inverted_index';
https.get(url, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    let j;
    try { j = JSON.parse(s); } catch (e) { console.log('RAW:' + s.slice(0, 800)); return; }
    if (!j.results) { console.log(JSON.stringify(j).slice(0, 800)); return; }
    console.log('FILTER: ' + filter + '  count=' + j.meta.count);
    for (const p of j.results) {
      const src = (p.primary_location && p.primary_location.source) || {};
      let abs = '';
      if (p.abstract_inverted_index) {
        const arr = [];
        for (const [w, pos] of Object.entries(p.abstract_inverted_index)) for (const i of pos) arr[i] = w;
        abs = arr.join(' ').replace(/\s+/g, ' ').slice(0, 900);
      }
      console.log('---');
      console.log('T: ' + p.title);
      console.log('A: ' + (p.authorships || []).map(a => a.author.display_name).join(', '));
      console.log('Y: ' + p.publication_year + ' | ' + (src.display_name || '') + ' vol ' + (p.biblio && p.biblio.volume) + ' pp ' + (p.biblio && p.biblio.first_page) + '-' + (p.biblio && p.biblio.last_page) + ' | ' + p.doi);
      if (abs) console.log('ABS: ' + abs);
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
