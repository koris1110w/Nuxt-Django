<template>
  <div>
    <div v-for="n in articles" :key="n._path">
      <nuxt-link :to="n._path">{{n.title}} {{n.date}}</nuxt-link>
    </div>
  </div>
</template>

<script setup>
const { data: articles } = await useAsyncData("articles", () =>
  queryContent("articles").limit(15).find()
)
useHead({
  title: "記事一覧",
})
</script>