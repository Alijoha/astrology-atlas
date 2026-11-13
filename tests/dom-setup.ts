import {JSDOM} from 'jsdom';
import {readFileSync} from 'node:fs';
const dom=new JSDOM('<!doctype html><html><body></body></html>',{url:'http://atlas.test/'});
for(const key of ['window','document','navigator','HTMLElement','HTMLAnchorElement','Node','MutationObserver','localStorage','history','location','Event','MouseEvent','KeyboardEvent','getComputedStyle'])Object.defineProperty(globalThis,key,{value:(dom.window as unknown as Record<string,unknown>)[key],configurable:true,writable:true});
Object.defineProperty(globalThis,'IS_REACT_ACT_ENVIRONMENT',{value:true,writable:true});
dom.window.scrollTo=()=>{};
dom.window.HTMLElement.prototype.scrollTo=()=>{};
export const downloads:{filename:string;blob?:Blob}[]=[];
let lastBlob:Blob|undefined;
URL.createObjectURL=(blob:Blob)=>{lastBlob=blob;return 'blob:atlas-test';};
URL.revokeObjectURL=()=>{};
dom.window.HTMLAnchorElement.prototype.click=function(){downloads.push({filename:this.download,blob:lastBlob});};

const birthplaces=readFileSync(new URL('../public/data/birthplaces.json',import.meta.url),'utf8');
const originalFetch=globalThis.fetch.bind(globalThis);
globalThis.fetch=async(input,init)=>typeof input==='string'&&input==='/data/birthplaces.json'?new Response(birthplaces,{status:200,headers:{'content-type':'application/json'}}):originalFetch(input,init);
