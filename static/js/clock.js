function updateClock() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, "0");
  const m = String(now.getMinutes()).padStart(2, "0");
  const s = String(now.getSeconds()).padStart(2, "0");

  const d = String(now.getDate()).padStart(2, "0");
  const mo = String(now.getMonth() + 1).padStart(2, "0");
  const y = now.getFullYear();

  // Met à jour toutes les horloges
  document.querySelectorAll(".clock").forEach(el => {
    el.textContent = `${h}:${m}:${s}`;
  });

  // Met à jour toutes les dates
  document.querySelectorAll(".date").forEach(el => {
    el.textContent = `${d}/${mo}/${y}`;
  });
}

// mise à jour toutes les secondes
updateClock();
setInterval(updateClock, 1000);

// update la page toutes les 30s
setInterval(() => {
  window.location.reload();
}, 30000);