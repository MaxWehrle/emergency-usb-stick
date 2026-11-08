(() => {
  const input = document.getElementById('search');
  const cards = [...document.querySelectorAll('[data-card]')];
  const count = document.getElementById('count');
  if (!input) return;
  const normal = s => s.toLocaleLowerCase('de-DE').normalize('NFD').replace(/[\u0300-\u036f]/g,'');
  function update(){
    const q = normal(input.value.trim());
    let shown = 0;
    cards.forEach(card => { const hit = !q || normal(card.textContent).includes(q); card.hidden = !hit; if(hit) shown++; });
    count.textContent = q ? `${shown} von ${cards.length} Lagekarten gefunden.` : `${cards.length} Lagekarten verfügbar.`;
  }
  input.addEventListener('input', update);
  update();
})();
