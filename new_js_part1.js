// ===== THEME TOGGLE =====
function toggleTheme() {
  const root = document.getElementById('root');
  const isLight = root.getAttribute('data-theme') === 'light';
  root.setAttribute('data-theme', isLight ? 'dark' : 'light');
  document.getElementById('theme-btn').textContent = isLight ? '\u2600' : '\u263d';
  localStorage.setItem('cmhk-theme', isLight ? 'dark' : 'light');
  setTimeout(() => { Object.values(charts).forEach(ch => { if(ch && ch.update) ch.update(); }); }, 80);
}
(function(){
  const saved = localStorage.getItem('cmhk-theme');
  if(saved) {
    document.getElementById('root').setAttribute('data-theme', saved);
    const btn = document.getElementById('theme-btn');
    if(btn) btn.textContent = saved === 'light' ? '\u263d' : '\u2600';
  }
})();

// ===== SEARCH NAV =====
function searchNav(q) {
  q = q.toLowerCase().trim();
  document.querySelectorAll('#main-nav .ni').forEach(item => {
    item.style.display = (!q || item.textContent.toLowerCase().includes(q)) ? '' : 'none';
  });
}

// ===== NOTIFICATIONS =====
function toggleNotif() {
  const p = document.getElementById('notif-panel');
  p.style.display = p.style.display === 'none' ? 'block' : 'none';
}
function clearNotifs() {
  document.getElementById('notif-dot').style.display = 'none';
  document.querySelectorAll('.notif-item').forEach(el => el.style.opacity = '0.45');
  document.getElementById('notif-panel').style.display = 'none';
}
document.addEventListener('click', e => {
  const wrap = document.getElementById('notif-wrap');
  if(wrap && !wrap.contains(e.target)) {
    const p = document.getElementById('notif-panel');
    if(p) p.style.display = 'none';
  }
});
