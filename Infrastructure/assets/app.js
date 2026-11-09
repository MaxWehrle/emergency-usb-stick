(() => {
  const input = document.getElementById('search');
  const clear = document.getElementById('clear-search');
  const count = document.getElementById('count');
  const cards = [...document.querySelectorAll('[data-card]')];
  if (!input || !count) return;
  const locale = document.documentElement.lang || 'en-US';
  const normal = value => value.toLocaleLowerCase(locale).normalize('NFD').replace(/[\u0300-\u036f]/g, '');
  function update() {
    const query = normal(input.value.trim());
    let shown = 0;
    cards.forEach(card => {
      card.hidden = !!query && !normal(card.textContent).includes(query);
      if (!card.hidden) shown++;
    });
    const template = query ? count.dataset.found : count.dataset.available;
    count.textContent = template.replace('{shown}', shown).replace('{total}', cards.length);
  }
  input.addEventListener('input', update);
  if (clear) clear.addEventListener('click', () => { input.value = ''; update(); input.focus(); });
  update();
})();
