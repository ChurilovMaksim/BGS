// Fetch arXiv metadata + abstract by id list: node abs.js id1 id2 ...
const https = require('https');
const ids = process.argv.slice(2);
const url = 'https://export.arxiv.org/api/query?id_list=' + ids.join(',') + '&max_results=' + ids.length;
https.get(url, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    const ents = s.split('<entry>').slice(1).map(x => x.split('</entry>')[0]);
    for (const e of ents) {
      const g = re => { const m = e.match(re); return m ? m[1].replace(/\s+/g, ' ').trim() : ''; };
      const au = [...e.matchAll(/<name>(.*?)<\/name>/g)].map(m => m[1]).join(', ');
      console.log('================================================');
      console.log('T: ' + g(/<title>([\s\S]*?)<\/title>/));
      console.log('A: ' + au);
      console.log('ID: ' + g(/<id>(.*?)<\/id>/) + '   PUB: ' + g(/<published>(.*?)<\/published>/).slice(0, 10) + '  UPD: ' + g(/<updated>(.*?)<\/updated>/).slice(0, 10));
      const jr = g(/<arxiv:journal_ref[^>]*>([\s\S]*?)<\/arxiv:journal_ref>/);
      const doi = g(/<arxiv:doi[^>]*>([\s\S]*?)<\/arxiv:doi>/);
      const cm = g(/<arxiv:comment[^>]*>([\s\S]*?)<\/arxiv:comment>/);
      if (jr) console.log('J: ' + jr);
      if (doi) console.log('DOI: ' + doi);
      if (cm) console.log('COMMENT: ' + cm);
      console.log('ABS: ' + g(/<summary>([\s\S]*?)<\/summary>/));
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
