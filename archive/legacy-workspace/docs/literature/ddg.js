// DuckDuckGo HTML search: node ddg.js "query"
const https = require('https');
const q = process.argv[2];
const opts = {
  hostname: 'html.duckduckgo.com', path: '/html/?q=' + encodeURIComponent(q),
  headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)' }
};
https.get(opts, res => {
  let s = '';
  res.on('data', d => s += d);
  res.on('end', () => {
    s = s.replace(/<script[\s\S]*?<\/script>/g, '').replace(/<style[\s\S]*?<\/style>/g, '');
    const blocks = s.split('result__body').slice(1);
    console.log('QUERY: ' + q + '  hits=' + blocks.length);
    for (const b of blocks.slice(0, 15)) {
      const a = b.match(/result__a[^>]*href="(.*?)"[^>]*>([\s\S]*?)<\/a>/);
      const sn = b.match(/result__snippet[^>]*>([\s\S]*?)<\/a>/);
      const clean = t => t.replace(/<[^>]*>/g, '').replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#x27;/g, "'").replace(/\s+/g, ' ').trim();
      if (!a) continue;
      let u = a[1];
      const m = u.match(/uddg=([^&]*)/);
      if (m) u = decodeURIComponent(m[1]);
      console.log('---');
      console.log('TITLE: ' + clean(a[2]));
      console.log('URL:   ' + u);
      if (sn) console.log('SNIP:  ' + clean(sn[1]).slice(0, 400));
    }
  });
}).on('error', e => console.log('ERR ' + e.message));
