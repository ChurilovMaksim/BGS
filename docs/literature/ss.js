// Semantic Scholar search: node ss.js "query" [limit]
const https = require('https');
const q = process.argv[2];
const limit = process.argv[3] || 10;
const fields = 'title,authors,year,venue,journal,externalIds,abstract,citationCount,publicationTypes';
const url = 'https://api.semanticscholar.org/graph/v1/paper/search?query=' + encodeURIComponent(q) +
  '&limit=' + limit + '&fields=' + fields;
https.get(url, { headers: { 'User-Agent': 'lit-survey/1.0' } }, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    let j;
    try { j = JSON.parse(s); } catch (e) { console.log('RAW:' + s.slice(0, 1500)); return; }
    if (!j.data) { console.log(JSON.stringify(j).slice(0, 1500)); return; }
    console.log('QUERY: ' + q + '  total=' + j.total);
    for (const p of j.data) {
      console.log('---');
      console.log('T: ' + p.title);
      console.log('A: ' + (p.authors || []).map(a => a.name).join(', '));
      console.log('Y: ' + p.year + ' | VENUE: ' + (p.venue || '') + ' | J: ' + JSON.stringify(p.journal || {}));
      console.log('IDS: ' + JSON.stringify(p.externalIds || {}) + ' | cites=' + p.citationCount);
      if (p.abstract) console.log('ABS: ' + p.abstract.replace(/\s+/g, ' ').slice(0, 1200));
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
