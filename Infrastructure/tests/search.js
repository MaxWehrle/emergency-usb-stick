const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const cards = [
  {textContent:'Water and sanitation',hidden:false},
  {textContent:'Power outage',hidden:false},
  {textContent:'Flood safety',hidden:false}
];
const listeners = {};
const input = {value:'',addEventListener:(name,fn)=>{listeners[`input:${name}`]=fn},focus:()=>{}};
const clear = {addEventListener:(name,fn)=>{listeners[`clear:${name}`]=fn}};
const count = {textContent:'',dataset:{available:'{total} situations available.',found:'{shown} of {total} situations found.'}};
const document = {documentElement:{lang:'en-US'},getElementById:id=>id==='search'?input:id==='clear-search'?clear:count,querySelectorAll:()=>cards};
vm.runInNewContext(fs.readFileSync('assets/app.js','utf8'),{document});
assert.equal(count.textContent,'3 situations available.');
input.value='water'; listeners['input:input']();
assert.deepEqual(cards.map(c=>c.hidden),[false,true,true]);
input.value='flood'; listeners['input:input']();
assert.deepEqual(cards.map(c=>c.hidden),[true,true,false]);
listeners['clear:click']();
assert(cards.every(c=>!c.hidden));
console.log('Offline search and clear passed.');
