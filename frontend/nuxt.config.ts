// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss",
    "@element-plus/nuxt",
    'nuxt-gtag',
    '@nuxtjs/sitemap',
    "@nuxt/image",
    "@nuxt/content"
  ],
  runtimeConfig: {
    public: {
        apiUrl: process.env.NUXT_PUBLIC_API_URL,
    }
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
  gtag: {
    id: 'G-PQJVM68CW4' // 測定ID
  },
  image: {
    domains: ["nazotokidb.com", "localhost", "localhost:3000"],
  },
  sitemap: {
    path: '/sitemap.xml'
  },
})