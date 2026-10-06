// Buscador client-side y conmutador de tema de la bóveda 1DAM.
(() => {
  // ---- Tema claro / oscuro ----
  const applyTheme = () => {
    const dark = localStorage.getItem("t") === "dark";
    document.documentElement.dataset.theme = dark ? "dark" : "";
    const btn = document.getElementById("theme");
    if (btn) btn.textContent = dark ? "Tema claro" : "Tema oscuro";
  };
  const themeBtn = document.getElementById("theme");
  if (themeBtn) {
    themeBtn.addEventListener("click", () => {
      localStorage.setItem("t", localStorage.getItem("t") === "dark" ? "light" : "dark");
      applyTheme();
    });
  }
  applyTheme();

  const input = document.getElementById("q");
  const results = document.getElementById("results");
  if (!input || !results) return;

  let index = [];

  fetch("index.json")
    .then((r) => r.json())
    .then((data) => { index = data; })
    .catch(() => {});

  const esc = (s) => s.replace(/[&<>"]/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  const highlight = (text, terms) => {
    let out = esc(text);
    terms.forEach((t) => {
      const re = new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "gi");
      out = out.replace(re, "<b>$1</b>");
    });
    return out;
  };

  const render = (items) => {
    results.innerHTML = "";
    if (!items.length) {
      const d = document.createElement("div");
      d.className = "empty";
      d.textContent = "Sin resultados.";
      results.appendChild(d);
      return;
    }
    items.forEach((it) => {
      const a = document.createElement("a");
      a.href = it.u;
      const sec = document.createElement("span");
      sec.className = "r-sec";
      sec.textContent = it.s;
      const t = document.createElement("span");
      t.textContent = it.t;
      a.appendChild(t);
      a.appendChild(sec);
      results.appendChild(a);
    });
  };

  input.addEventListener("input", () => {
    const q = input.value.trim();
    if (!q || !index.length) {
      results.classList.remove("open");
      render([]);
      return;
    }
    const terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    const hits = index
      .map((it) => {
        const hay = (it.t + " " + it.s + " " + it.g.join(" ") + " " + it.x).toLowerCase();
        let score = 0;
        let ok = true;
        terms.forEach((t) => {
          const n = hay.split(t).length - 1;
          if (!n) ok = false;
          score += n;
        });
        return { it, score };
      })
      .filter((h) => h.ok)
      .sort((a, b) => b.score - a.score)
      .slice(0, 12)
      .map((h) => h.it);
    results.classList.add("open");
    render(hits);
  });

  document.addEventListener("click", (e) => {
    if (!results.contains(e.target) && e.target !== input) results.classList.remove("open");
  });
})();