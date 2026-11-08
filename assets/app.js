(() => {
  const input = document.getElementById('search');
  const cards = [...document.querySelectorAll('[data-card]')];
  const count = document.getElementById('count');
  if (!input) return;
  const locale = document.documentElement.lang || 'en-US';
  const normal = s => s.toLocaleLowerCase(locale).normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  function update(){
    const q = normal(input.value.trim());
    let shown = 0;
    cards.forEach(card => { const hit = !q || normal(card.textContent).includes(q); card.hidden = !hit; if(hit) shown++; });
    const template = q ? count.dataset.found : count.dataset.available;
    count.textContent = template.replace('{shown}', shown).replace('{total}', cards.length);
  }
  input.addEventListener('input', update);
  update();
})();
