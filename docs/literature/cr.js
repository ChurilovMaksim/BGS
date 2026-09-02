// Crossref search: node cr.js "query" [rows]
const https = require('https');
const q = process.argv[2];
const rows = process.argv[3] || 8;
const url = 'https://api.crossref.org/works?query.bibliographic=' + encodeURIComponent(q) +
  '&rows=' + rows + '&mailto=lit@example.org';
https.get(url, { headers: { 'User-Agent': 'lit-survey/1.0 (mailto:lit@example.org)' } }, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    let j;
    try { j = JSON.parse(s); } catch (e) { console.log('RAW:' + s.slice(0, 1000)); return; }
    const items = (j.message && j.message.items) || [];
    console.log('QUERY: ' + q);
    for (const p of items) {
      console.log('---');
      console.log('T: ' + (p.title || []).join(' / '));
      console.log('A: ' + (p.author || []).map(a => (a.given || '') + ' ' + (a.family || '')).join(', '));
      console.log('J: ' + (p['container-title'] || []).join(' / ') + ' | vol ' + p.volume + ' iss ' + p.issue + ' pp ' + p.page + ' | year ' + ((p.issued && p.issued['date-parts'] && p.issued['date-parts'][0][0]) || ''));
      console.log('DOI: ' + p.DOI + ' | type ' + p.type);
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
