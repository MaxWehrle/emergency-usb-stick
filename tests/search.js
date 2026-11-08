const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const cards = [
  {textContent:'Wasser und Hygiene', hidden:false},
  {textContent:'Stromausfall und Wärme', hidden:false},
  {textContent:'Hochwasser', hidden:false}
];
const listeners = {};
const input = {value:'', addEventListener:(name,fn)=>{listeners[name]=fn}};
const count = {textContent:''};
const document = {getElementById:id=>id==='search'?input:count,querySelectorAll:()=>cards};
vm.runInNewContext(fs.readFileSync('assets/app.js','utf8'),{document});
assert.equal(count.textContent,'3 Lagekarten verfügbar.');
input.value='warme'; listeners.input();
assert.deepEqual(cards.map(c=>c.hidden),[true,false,true]);
input.value='Hochwasser'; listeners.input();
assert.deepEqual(cards.map(c=>c.hidden),[true,true,false]);
input.value=''; listeners.input();
assert(cards.every(c=>!c.hidden));
console.log('Offline search filter passed.');
