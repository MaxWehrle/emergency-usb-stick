const fs = require('fs');
const path = require('path');
const vm = require('vm');
const assert = require('assert');
const cards = [
  {textContent:'Wasser und Hygiene',hidden:false},
  {textContent:'Stromausfall und Wärme',hidden:false},
  {textContent:'Hochwasser',hidden:false}
];
const listeners = {};
const input = {value:'',addEventListener:(name,fn)=>{listeners[`input:${name}`]=fn},focus:()=>{}};
const clear = {addEventListener:(name,fn)=>{listeners[`clear:${name}`]=fn}};
const count = {textContent:'',dataset:{available:'{total} Themen verfügbar.',found:'{shown} von {total} Themen gefunden.'}};
const document = {documentElement:{lang:'de-DE'},getElementById:id=>id==='search'?input:id==='clear-search'?clear:count,querySelectorAll:()=>cards};
vm.runInNewContext(fs.readFileSync(path.resolve(__dirname,'../assets/app.js'),'utf8'),{document});
assert.equal(count.textContent,'3 Themen verfügbar.');
input.value='warme'; listeners['input:input']();
assert.deepEqual(cards.map(c=>c.hidden),[true,false,true]);
input.value='Wasser'; listeners['input:input']();
assert.deepEqual(cards.map(c=>c.hidden),[false,true,false]);
listeners['clear:click']();
assert(cards.every(c=>!c.hidden));
console.log('Offline search and clear passed.');
