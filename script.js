/* ============================================================
   PORTFOLIO — script.js
   ============================================================ */

/* ── THEME ──────────────────────────────────────────────── */
const sunIco  = document.getElementById('ico-sun');
const moonIco = document.getElementById('ico-moon');

function applyTheme(t) {
  if (t === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.body.style.background = '#181715';
    sunIco.style.display  = '';
    moonIco.style.display = 'none';
  } else {
    document.documentElement.removeAttribute('data-theme');
    document.body.style.background = '#faf9f5';
    sunIco.style.display  = 'none';
    moonIco.style.display = '';
  }
}

let theme = 'light';
try { const s = localStorage.getItem('myweb-theme'); if (s === 'dark' || s === 'light') theme = s; } catch (e) {}
applyTheme(theme);

document.getElementById('theme-btn').addEventListener('click', () => {
  theme = theme === 'dark' ? 'light' : 'dark';
  applyTheme(theme);
  try { localStorage.setItem('myweb-theme', theme); } catch (e) {}
});

/* ── NAVBAR SCROLL ──────────────────────────────────────── */
const nav = document.getElementById('nav');
const btt = document.getElementById('btt');
const mob = document.getElementById('mob-menu');

function onScroll() {
  const y = window.scrollY;
  nav.classList.toggle('scrolled', y > 24 || mob.classList.contains('open'));
  btt.classList.toggle('on', y > 400);
}
window.addEventListener('scroll', onScroll, { passive: true });
onScroll();

/* ── HAMBURGER ──────────────────────────────────────────── */
const ham    = document.getElementById('ham');
const hamIco = document.getElementById('ico-ham');
const xIco   = document.getElementById('ico-x');

ham.addEventListener('click', () => {
  const open = mob.classList.toggle('open');
  hamIco.style.display = open ? 'none' : '';
  xIco.style.display   = open ? ''     : 'none';
  nav.classList.toggle('scrolled', open || window.scrollY > 24);
});

mob.querySelectorAll('a').forEach(a => a.addEventListener('click', () => {
  mob.classList.remove('open');
  hamIco.style.display = '';
  xIco.style.display   = 'none';
  onScroll();
}));

/* ── SCROLL FADE ────────────────────────────────────────── */
/*
  rootMargin '0px 0px 80px 0px' pre-triggers the observer
  80px before each element reaches the bottom of the viewport.
  threshold:0 fires as soon as a single pixel is visible.
*/
const scrollObs = new IntersectionObserver(
  entries => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('on');
        scrollObs.unobserve(e.target);
      }
    });
  },
  { threshold: 0, rootMargin: '0px 0px 80px 0px' }
);

document.querySelectorAll('.sf').forEach(el => scrollObs.observe(el));

/* ── RIGHT PANEL TOGGLE ─────────────────────────────────── */
const btnTerminal  = document.getElementById('btn-terminal');
const btnPhoto     = document.getElementById('btn-photo');
const rpTerminal   = document.getElementById('rp-terminal');
const rpPhotoPanel = document.getElementById('rp-photo-panel');

function switchRightPanel(which) {
  const toTerminal = which === 'terminal';
  rpTerminal.classList.toggle('active', toTerminal);
  rpPhotoPanel.classList.toggle('active', !toTerminal);
  btnTerminal.classList.toggle('active', toTerminal);
  btnPhoto.classList.toggle('active', !toTerminal);
}

btnTerminal.addEventListener('click', () => switchRightPanel('terminal'));
btnPhoto.addEventListener('click',    () => switchRightPanel('photo'));

/* ── PHOTO SLOTS (left circle + right panel, share one upload) ── */
const slotL     = document.getElementById('photo-slot');
const hintL     = document.getElementById('photo-hint');
const photoImgL = document.getElementById('photo-img');
const slotLg    = document.getElementById('photo-slot-lg');
const hintLg    = document.getElementById('photo-hint-lg');
const photoImgR = document.getElementById('photo-img-r');
const fileIn    = document.getElementById('photo-file');

function setPhoto(src) {
  /* left circle */
  photoImgL.src           = src;
  photoImgL.style.display = 'block';
  hintL.style.display     = 'none';
  slotL.style.background  = 'transparent';
  /* right panel */
  photoImgR.src           = src;
  photoImgR.style.display = 'block';
  hintLg.style.display    = 'none';
}

/* clicking either slot opens the same file picker */
// slotL.addEventListener('click',  () => fileIn.click());
// slotLg.addEventListener('click', () => fileIn.click());

fileIn.addEventListener('change', e => {
  const f = e.target.files[0];
  if (!f) return;
  const reader = new FileReader();
  reader.onload = ev => {
    setPhoto(ev.target.result);
    try { localStorage.setItem('myweb-photo', ev.target.result); } catch (err) {}
  };
  reader.readAsDataURL(f);
});

try {
  const saved = localStorage.getItem('myweb-photo');
  if (saved) setPhoto(saved);
} catch (e) {}

/* ── BACK TO TOP ────────────────────────────────────────── */
btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

/* ── CONTACT FORM FALLBACK ──────────────────────────────── */
/*
  If the Formspree ID hasn't been swapped yet, fall back to mailto.
  Replace 'yourFormId' in index.html with your real Formspree ID to
  use the hosted form instead.
*/
document.querySelector('.cform').addEventListener('submit', function (e) {
  if (this.action.includes('yourFormId')) {
    e.preventDefault();
    const name    = document.getElementById('f-name').value;
    const subject = document.getElementById('f-subject').value || 'Portfolio enquiry';
    const message = document.getElementById('f-message').value;
    window.location.href =
      'mailto:prince880211@gmail.com'
      + '?subject=' + encodeURIComponent(subject)
      + '&body='    + encodeURIComponent('From: ' + name + '\n\n' + message);
  }
});
