// Mojeek HTML search: node mj.js "query"
const https = require('https');
const q = process.argv[2];
const opts = {
  hostname: 'www.mojeek.com', path: '/search?q=' + encodeURIComponent(q),
  headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124.0 Safari/537.36' }
};
https.get(opts, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    s = s.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '');
    const clean = t => t.replace(/<[^>]*>/g, '').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/\s+/g, ' ').trim();
    const blocks = s.split(/<li>/).slice(1);
    console.log('QUERY: ' + q + '  blocks=' + blocks.length);
    let n = 0;
    for (const b of blocks) {
      const a = b.match(/<a class="title"[^>]*href="(.*?)"[^>]*>([\s\S]*?)<\/a>/);
      const p = b.match(/<p class="s">([\s\S]*?)<\/p>/);
      if (!a) continue;
      n++;
      if (n > 15) break;
      console.log('---');
      console.log('TITLE: ' + clean(a[2]));
      console.log('URL:   ' + a[1]);
      if (p) console.log('SNIP:  ' + clean(p[1]).slice(0, 400));
    }
    if (n === 0) console.log('NO PARSED RESULTS len=' + s.length);
  });
}).on('error', e => console.log('ERR ' + e.message));
