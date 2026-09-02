// arXiv API query helper: node ax.js "<search_query>" [max] [abs]
const https = require('https');
const q = process.argv[2];
const max = process.argv[3] || 40;
const showAbs = process.argv[4] === 'abs';
const url = 'https://export.arxiv.org/api/query?search_query=' + encodeURIComponent(q) +
  '&start=0&max_results=' + max + '&sortBy=relevance&sortOrder=descending';
https.get(url, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    const ents = s.split('<entry>').slice(1).map(x => x.split('</entry>')[0]);
    console.log('QUERY: ' + q + '   N=' + ents.length);
    for (const e of ents) {
      const g = re => { const m = e.match(re); return m ? m[1].replace(/\s+/g, ' ').trim() : ''; };
      const au = [...e.matchAll(/<name>(.*?)<\/name>/g)].map(m => m[1]).join(', ');
      const jr = g(/<arxiv:journal_ref[^>]*>([\s\S]*?)<\/arxiv:journal_ref>/);
      const doi = g(/<arxiv:doi[^>]*>([\s\S]*?)<\/arxiv:doi>/);
      console.log('---');
      console.log('T: ' + g(/<title>([\s\S]*?)<\/title>/));
      console.log('A: ' + au);
      console.log('D: ' + g(/<published>(.*?)<\/published>/).slice(0, 10) + '  ID: ' + g(/<id>(.*?)<\/id>/));
      if (jr) console.log('J: ' + jr);
      if (doi) console.log('DOI: ' + doi);
      if (showAbs) console.log('ABS: ' + g(/<summary>([\s\S]*?)<\/summary>/));
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
