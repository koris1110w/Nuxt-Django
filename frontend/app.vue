<template>
  <html class="dark bg-gray-900">
    <body>
      <NuxtLayout>
        <NuxtPage />
      </NuxtLayout>
    </body>
  </html>
</template>
<script setup>
  import 'element-plus/theme-chalk/dark/css-vars.css'
  import './assets/styles/main.css'
  useHead({
    title: "Nuxt3",
    link: [
      {rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap"}
    ]
  })
</script>