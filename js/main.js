/* Julieth Suárez Studio · interacciones de la página */
(function () {
  "use strict";

  // Menú móvil
  var btn = document.querySelector(".menu-btn");
  var menu = document.getElementById("menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var open = menu.classList.toggle("is-open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.addEventListener("click", function (ev) {
      if (ev.target.closest("a")) { menu.classList.remove("is-open"); btn.setAttribute("aria-expanded", "false"); }
    });
  }

  // Cambio de línea Nacional / Deluxe en cada sección de precios
  document.querySelectorAll("[data-pricing]").forEach(function (sec) {
    var buttons = sec.querySelectorAll(".line-toggle button");
    buttons.forEach(function (b) {
      b.addEventListener("click", function () {
        var line = b.getAttribute("data-line");
        buttons.forEach(function (x) {
          var on = x === b;
          x.classList.toggle("is-on", on);
          x.setAttribute("aria-pressed", on ? "true" : "false");
        });
        sec.querySelectorAll(".price").forEach(function (p) { p.textContent = p.getAttribute("data-" + line); });
        sec.querySelectorAll(".line-name").forEach(function (n) { n.textContent = line === "d" ? "Deluxe" : "Nacional"; });
        sec.setAttribute("data-line", line);
      });
    });
  });

  // Galería filtrable
  var chips = document.querySelectorAll(".chip");
  chips.forEach(function (c) {
    c.addEventListener("click", function () {
      var f = c.getAttribute("data-filter");
      chips.forEach(function (x) { var on = x === c; x.classList.toggle("is-on", on); x.setAttribute("aria-pressed", on ? "true" : "false"); });
      document.querySelectorAll(".g-item").forEach(function (g) { g.hidden = !(f === "todas" || g.getAttribute("data-cat") === f); });
    });
  });

  // Visor de fotos
  var lb = document.getElementById("lightbox");
  if (lb && typeof lb.showModal === "function") {
    var lbImg = lb.querySelector("img");
    document.querySelectorAll(".g-open").forEach(function (o) {
      o.addEventListener("click", function () {
        lbImg.src = o.getAttribute("data-src");
        lbImg.alt = o.getAttribute("data-alt");
        lb.showModal();
      });
    });
    lb.querySelector(".lb-close").addEventListener("click", function () { lb.close(); });
    lb.addEventListener("click", function (ev) { if (ev.target === lb) lb.close(); });
  }

  // Formulario de agenda → WhatsApp
  var form = document.getElementById("book-form");
  if (!form) return;
  var tipo = form.querySelector("#f-tipo");
  var paquete = form.querySelector("#f-paquete");
  var lineaField = document.getElementById("field-linea");
  var fecha = form.querySelector("#f-fecha");
  var hoy = new Date();
  fecha.min = new Date(hoy.getTime() - hoy.getTimezoneOffset() * 60000).toISOString().slice(0, 10);

  function fillPaquetes(sel) {
    var list = (window.PAQUETES || {})[tipo.value] || [];
    paquete.innerHTML = "";
    list.forEach(function (name) {
      var o = document.createElement("option");
      o.textContent = name; o.value = name;
      if (name === sel) o.selected = true;
      paquete.appendChild(o);
    });
  }
  tipo.addEventListener("change", function () { fillPaquetes(); });
  fillPaquetes();

  // Botones "Agendar" de cada paquete: preseleccionan el formulario
  document.querySelectorAll("[data-book]").forEach(function (a) {
    a.addEventListener("click", function () {
      var parts = a.getAttribute("data-book").split("|");
      tipo.value = parts[0];
      fillPaquetes(parts[1]);
      var sec = a.closest("[data-pricing]");
      if (sec && sec.getAttribute("data-line") === "d") form.querySelector("#f-linea").value = "Deluxe";
      setTimeout(function () { form.querySelector("#f-nombre").focus({ preventScroll: true }); }, 500);
    });
  });

  function fechaLarga(v) {
    if (!v) return "";
    var p = v.split("-");
    var d = new Date(+p[0], +p[1] - 1, +p[2]);
    return d.toLocaleDateString("es-CO", { weekday: "long", day: "numeric", month: "long", year: "numeric" });
  }

  form.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var err = document.getElementById("form-error");
    var nombre = form.nombre.value.trim();
    if (!nombre || !form.fecha.value) { err.hidden = false; (nombre ? form.fecha : form.nombre).focus(); return; }
    err.hidden = true;
    var ocasion = { novia: "mi boda", quince: "mis quince", social: "un maquillaje social" }[tipo.value];
    var lines = [
      "Hola, Julieth. Soy " + nombre + " y quiero agendar " + ocasion + ".",
      "",
      "• Paquete o servicio: " + paquete.value
    ];
    if (tipo.value !== "social") lines.push("• Línea: " + form.linea.value);
    lines.push("• Fecha: " + fechaLarga(form.fecha.value));
    if (form.hora.value) lines.push("• Debo estar lista a las: " + form.hora.value);
    if (form.lugar.value.trim()) lines.push("• Me arreglo en: " + form.lugar.value.trim());
    var extra = parseInt(form.extra.value, 10) || 0;
    if (extra > 0) lines.push("• Personas adicionales: " + extra);
    if (form.notas.value.trim()) lines.push("• Notas: " + form.notas.value.trim());
    lines.push("", "¿Tienes disponibilidad?");
    var url = "https://wa.me/" + window.WA + "?text=" + encodeURIComponent(lines.join("\n"));
    var link = document.createElement("a");
    link.href = url; link.target = "_blank"; link.rel = "noopener";
    document.body.appendChild(link); link.click(); link.remove();
  });
})();
