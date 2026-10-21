const fs=require('fs'),katex=require('katex');
const a=JSON.parse(fs.readFileSync(__dirname+'/segments.json','utf8')),errors=[];
for(const x of a){try{katex.renderToString(x.latex,{displayMode:x.display,throwOnError:true,strict:false,trust:false});}catch(e){errors.push({...x,error:e.message});}}
fs.writeFileSync(__dirname+'/errors.json',JSON.stringify(errors,null,2));
console.log(JSON.stringify({segments:a.length,errors:errors.length}));
