const fs = require('fs');
const vm = require('vm');
const assert = require('assert');
const cards = [
  {textContent:'Water and sanitation', hidden:false},
  {textContent:'Power outage and generators', hidden:false},
  {textContent:'Flood safety', hidden:false}
];
const listeners = {};
const input = {value:'', addEventListener:(name,fn)=>{listeners[name]=fn}};
const count = {textContent:'', dataset:{available:'{total} situation cards available.',found:'{shown} of {total} situation cards found.'}};
const document = {documentElement:{lang:'en-US'},getElementById:id=>id==='search'?input:count,querySelectorAll:()=>cards};
vm.runInNewContext(fs.readFileSync('assets/app.js','utf8'),{document});
assert.equal(count.textContent,'3 situation cards available.');
input.value='water'; listeners.input();
assert.deepEqual(cards.map(c=>c.hidden),[false,true,true]);
input.value='flood'; listeners.input();
assert.deepEqual(cards.map(c=>c.hidden),[true,true,false]);
input.value=''; listeners.input();
assert(cards.every(c=>!c.hidden));
console.log('Offline search filter passed.');
