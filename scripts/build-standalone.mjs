import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {build} from 'esbuild';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
const read=file=>fs.readFile(path.join(root,file),'utf8');
const result=await build({entryPoints:[path.join(root,'src/main.tsx')],absWorkingDir:root,bundle:true,format:'iife',platform:'browser',target:'es2022',write:false,minify:true,legalComments:'none',loader:{'.css':'empty'},define:{'process.env.NODE_ENV':'"production"'}});
let css=(await Promise.all(['src/styles.css','src/readability.css','src/birth-portrait.css','src/personal.css','src/learn.css'].map(read))).join('\n');
const fontNames=[...new Set([...css.matchAll(/url\(['"]?\/fonts\/([^'")]+)['"]?\)/g)].map(m=>m[1]))];
for(const file of fontNames){const bytes=await fs.readFile(path.join(root,'public/fonts',file));css=css.replaceAll(`/fonts/${file}`,`data:font/ttf;base64,${bytes.toString('base64')}`);}
const licenses={};
for(const name of ['react','react-dom','luxon','astronomy-engine','lucide-react']){const dir=path.join(root,'node_modules',name);const files=await fs.readdir(dir);for(const file of files.filter(n=>/^license(?:\.|$)/i.test(n)))licenses[`${name}/${file}`]=await fs.readFile(path.join(dir,file),'utf8');}
for(const file of ['public/fonts/DM-Sans-OFL.txt','public/fonts/Marcellus-OFL.txt','public/fonts/Noto-Sans-Runic-OFL.txt','public/data/GeoNames-attribution.txt'])licenses[file]=await read(file);
const safeJSON=x=>JSON.stringify(x).replace(/</g,'\\u003c').replace(/\u2028/g,'\\u2028').replace(/\u2029/g,'\\u2029');
const places=JSON.parse(await read('public/data/birthplaces.json'));
const javascript=result.outputFiles.find(f=>f.path.endsWith('.js'))?.text||result.outputFiles[0].text;
const doc=`<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#302638"><title>Astrology Atlas 4 · Your Personal Cosmos</title><meta name="description" content="A private, interactive astrology companion. Birth portraits, sky charts, calendar traditions, personal stones and colors."><style>${css}</style></head><body><div id="root"></div><script type="application/json" id="bundled-licenses">${safeJSON(licenses)}</script><script>globalThis.__ATLAS_BIRTHPLACES__=${safeJSON(places)};</script><script>${javascript.replace(/<\/script/gi,'<\\/script')}</script></body></html>`;
const output=path.join(root,'astrology-atlas-v4.html');await fs.writeFile(output,doc);console.log(`Standalone browser app: ${output} (${(Buffer.byteLength(doc)/1024/1024).toFixed(2)} MiB)`);
