// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@element-plus/nuxt",
    'nuxt-gtag',
    '@nuxtjs/sitemap',
    "@nuxt/image",
    "@nuxt/content",
    '@nuxtjs/color-mode',
  ],
  runtimeConfig: {
    public: {
        apiUrl: process.env.NUXT_PUBLIC_API_URL,
    }
  },
  site: {
    url: 'https://nazotokidb.com',
  },
  app:{
    head: {
      title: "謎解きデータベース",
      htmlAttrs: {  
        lang: 'ja-JP',
      },
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
      ],
      link: [
        { rel: "icon", type: "image/png", href: "/favicon.ico" }, // これを追記する
      ],
      script: [
        {
          async: true,
          src: "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7081501069094845",
          crossorigin: "anonymous",
          tagPosition: "bodyClose",
        },
      ],
    },
  },
  nitro:{
    prerender: {
      failOnError: false,
    },
  },
  gtag: {
    id: 'G-PQJVM68CW4' // 測定ID
  },
  image: {
    domains: ["nazotokidb.com", "localhost", "localhost:3000"],
  },
  sitemap: {
    path: '/sitemap.xml',
    async routes() {
      const { data: articleList } = await useFetch(`https://nazotokidb.com/api/v1/articles/`)
        return articleList.map(
          (article) =>
            `articles/${article.id}`
      );
    },
  },
  colorMode: {
    preference: 'dark',
    classSuffix: '',
  }
})