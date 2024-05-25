// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },
  modules: [
    "@nuxtjs/tailwindcss", 
    "@element-plus/nuxt", 
  ],
  runtimeConfig: {
    public: {
        apiUrl: process.env.NUXT_PUBLIC_API_URL,
        apiUrlOnServer: process.env.NUXT_PUBLIC_API_URL_ON_SERVER,
    }
  },
  app:{
    head: {
      title: "謎解きデータベース",
      meta: [
        { charset: "utf-8" },
        { name: "viewport", content: "width=device-width, initial-scale=1" },
      ],
      link: [
        { rel: "icon", type: "image/png", href: "/favicon.ico" }, // これを追記する
      ],
    },
  }
})