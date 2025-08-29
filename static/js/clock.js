function updateClock() {
  const now = new Date();
  const h = String(now.getHours()).padStart(2, "0");
  const m = String(now.getMinutes()).padStart(2, "0");
  const s = String(now.getSeconds()).padStart(2, "0");

  const d = String(now.getDate()).padStart(2, "0");
  const mo = String(now.getMonth() + 1).padStart(2, "0");
  const y = now.getFullYear();

  document.getElementById("clock").textContent = `${h}:${m}:${s}`;
  document.getElementById("date").textContent = `${d}/${mo}/${y}`;
}

// mise à jour toutes les secondes
updateClock();
setInterval(updateClock, 1000);
