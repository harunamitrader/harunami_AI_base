const statsRoot = document.querySelector("#site-stats");
const todayRoot = document.querySelector("#today-articles");
const archiveRoot = document.querySelector("#archive-list");
const starredStorageKey = "harunami-ai-base-starred-articles";

const categoryFilter = document.currentScript?.getAttribute("data-category") ?? null;

load();

async function load() {
  const response = await fetch("./data/articles.json", { cache: "no-store" });
  const payload = await response.json();
  const starredSlugs = loadStarredSlugs();
  const allArticles = [...payload.articles].sort((left, right) => {
    return right.publishedAt.localeCompare(left.publishedAt);
  });
  const articles = categoryFilter
    ? allArticles.filter((a) => a.category === categoryFilter)
    : allArticles;

  const latestDate = articles[0]?.publishedAt ?? null;
  const todayArticles = latestDate
    ? articles.filter((article) => article.publishedAt === latestDate)
    : [];
  const archiveArticles = latestDate
    ? articles.filter((article) => article.publishedAt !== latestDate)
    : [];

  renderStats(articles, latestDate);
  renderToday(todayArticles, latestDate, starredSlugs);
  renderArchive(archiveArticles, starredSlugs);
}

function renderStats(articles, latestDate) {
  const items = [
    { label: "記事数", value: String(articles.length) },
    { label: "最終投稿日", value: latestDate ?? "-" },
    { label: "運用", value: "Codex manual" },
  ];

  statsRoot.innerHTML = items
    .map((item) => {
      return `
        <div class="stat-box">
          <span>${item.label}</span>
          <strong>${item.value}</strong>
        </div>
      `;
    })
    .join("");
}

function renderToday(articles, latestDate, starredSlugs) {
  if (articles.length === 0) {
    todayRoot.innerHTML = `
      <div class="latest-box">
        <h3>まだ記事がありません。</h3>
        <p>Codex に「今日の記事作って」と頼むと、この欄に最新投稿日の記事が並びます。</p>
      </div>
    `;
    return;
  }

  todayRoot.innerHTML = articles
    .map((article) => {
      const deckText = article.dek ?? article.summary;
      const isStarred = starredSlugs.has(article.slug);
      return `
        <div class="latest-box article-card">
          <div class="article-card-head">
            <a class="card-link-box article-card-link" href="${article.articleUrl}">
              <h3>${article.title}</h3>
              <div class="article-meta">
                <span>${latestDate}</span>
                <span>${article.repoName}</span>
              </div>
              <p>${deckText}</p>
              <span class="link-button">記事を読む</span>
            </a>
            ${renderStarButton(article.slug, isStarred)}
          </div>
        </div>
      `;
    })
    .join("");

  attachStarHandlers(todayRoot);
}

function renderArchive(articles, starredSlugs) {
  if (articles.length === 0) {
    archiveRoot.innerHTML = `
      <div class="archive-item">
        <h3>まだ過去記事はありません。</h3>
        <p>次回以降の更新から、この欄に当日分以外の記事が並びます。</p>
      </div>
    `;
    return;
  }

  archiveRoot.innerHTML = articles
    .map((article) => {
      const deckText = article.dek ?? article.summary;
      const isStarred = starredSlugs.has(article.slug);
      return `
        <div class="archive-item article-card">
          <div class="article-card-head">
            <a class="card-link-box article-card-link" href="${article.articleUrl}">
              <h3>${article.title}</h3>
              <div class="archive-meta">
                <span>${article.publishedAt}</span>
                <span>${article.repoName}</span>
              </div>
              <p>${deckText}</p>
            </a>
            ${renderStarButton(article.slug, isStarred)}
          </div>
        </div>
      `;
    })
    .join("");

  attachStarHandlers(archiveRoot);
}

function renderStarButton(slug, isStarred) {
  const label = isStarred ? "★" : "☆";
  const pressed = isStarred ? "true" : "false";
  const title = isStarred ? "スターを外す" : "スターを付ける";
  const activeClass = isStarred ? " is-active" : "";
  return `
    <button
      class="star-toggle${activeClass}"
      type="button"
      data-star-slug="${slug}"
      aria-pressed="${pressed}"
      title="${title}"
    >${label}</button>
  `;
}

function loadStarredSlugs() {
  try {
    const raw = window.localStorage.getItem(starredStorageKey);
    const parsed = raw ? JSON.parse(raw) : [];
    return new Set(Array.isArray(parsed) ? parsed : []);
  } catch {
    return new Set();
  }
}

function saveStarredSlugs(starredSlugs) {
  window.localStorage.setItem(
    starredStorageKey,
    JSON.stringify([...starredSlugs].sort())
  );
}

function attachStarHandlers(root) {
  root.querySelectorAll("[data-star-slug]").forEach((button) => {
    button.addEventListener("click", async (event) => {
      event.preventDefault();
      event.stopPropagation();
      toggleArticleStar(button.dataset.starSlug);
      await load();
    });
  });
}

function toggleArticleStar(slug) {
  const starredSlugs = loadStarredSlugs();
  if (starredSlugs.has(slug)) {
    starredSlugs.delete(slug);
  } else {
    starredSlugs.add(slug);
  }
  saveStarredSlugs(starredSlugs);
}
