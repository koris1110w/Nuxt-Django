<template>
  <html class="dark">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </html>
</template>
<script setup>
  useHead({
    title: "Nuxt3",
    link: [
      {rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap"}
    ]
  })
</script>