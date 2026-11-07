(() => {
  "use strict";
  const comics = JSON.parse(document.getElementById("comic-data").textContent);
  const gallery = document.getElementById("gallery");
  const reader = document.getElementById("reader");
  const title = document.getElementById("reader-title");
  const image = document.getElementById("reader-image");
  const shareStatus = document.getElementById("share-status");
  const fallback = document.getElementById("share-fallback");
  const shareInput = document.getElementById("share-url");
  let activeIndex = -1;
  let galleryScroll = 0;
  let opener = null;

  function render({ focus = false } = {}) {
    const match = location.hash.match(/^#comic-(\d{3})$/);
    activeIndex = match ? comics.findIndex(comic => comic.id === match[1]) : -1;
    const comic = comics[activeIndex];
    reader.hidden = !comic;
    gallery.hidden = Boolean(comic);
    shareStatus.textContent = "";
    fallback.hidden = true;
    if (!comic) {
      document.title = "AI Vehicle Comics · KKLL";
      document.getElementById("gallery-notice").textContent =
        match ? "That comic is not in the gallery yet. Browse the collection below." : "";
      if (focus) {
        (opener || document.getElementById("gallery-title")).focus({ preventScroll: true });
        window.scrollTo(0, galleryScroll);
      }
      return;
    }
    title.textContent = comic.title;
    document.getElementById("reader-number").textContent = "COMIC " + comic.id;
    document.getElementById("reader-position").textContent = (activeIndex + 1) + " of " + comics.length;
    document.getElementById("reader-caption").textContent = comic.message;
    image.src = comic.image;
    image.alt = "Comic " + comic.id + ": " + comic.title + ". " + comic.message;
    image.width = comic.width;
    image.height = comic.height;
    const original = document.getElementById("reader-original");
    original.href = comic.image;
    original.setAttribute("aria-label", "Open " + comic.title + " at full resolution in a new tab");
    document.title = comic.title + " · AI Vehicle Comics";
    if (focus) {
      title.focus({ preventScroll: true });
      window.scrollTo(0, 0);
    }
  }

  function navigate(index) {
    const next = comics[(index + comics.length) % comics.length];
    history.pushState(null, "", "#comic-" + next.id);
    render({ focus: true });
  }

  function closeReader() {
    history.pushState(null, "", location.pathname + location.search);
    render({ focus: true });
  }

  document.querySelectorAll("[data-comic]").forEach(link => {
    link.addEventListener("click", event => {
      if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      event.preventDefault();
      galleryScroll = window.scrollY;
      opener = link;
      navigate(comics.findIndex(comic => comic.id === link.dataset.comic));
    });
  });
  document.getElementById("back-to-gallery").addEventListener("click", closeReader);
  document.getElementById("previous-comic").addEventListener("click", () => navigate(activeIndex - 1));
  document.getElementById("next-comic").addEventListener("click", () => navigate(activeIndex + 1));
  document.getElementById("share-comic").addEventListener("click", async () => {
    const comic = comics[activeIndex];
    if (!comic) return;
    const url = location.href;
    try {
      if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(url);
        shareStatus.textContent = "Comic link copied.";
        return;
      }
    } catch {
      // Keep the link available when clipboard access is unavailable or denied.
    }
    shareInput.value = url;
    fallback.hidden = false;
    shareInput.focus();
    shareInput.select();
    shareStatus.textContent = "Copy this link to share the comic.";
  });
  window.addEventListener("popstate", () => render({ focus: true }));
  window.addEventListener("hashchange", () => render({ focus: true }));
  document.addEventListener("keydown", event => {
    if (reader.hidden || event.altKey || event.ctrlKey || event.metaKey ||
        ["INPUT", "TEXTAREA", "SELECT"].includes(document.activeElement.tagName)) return;
    if (event.key === "Escape") { event.preventDefault(); closeReader(); }
    if (event.key === "ArrowLeft") { event.preventDefault(); navigate(activeIndex - 1); }
    if (event.key === "ArrowRight") { event.preventDefault(); navigate(activeIndex + 1); }
  });
  render();
})();
