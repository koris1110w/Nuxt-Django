<template>
  <div class="mx-4">
    <div>
      <p class="text-md text-gray-400">謎解きデータベースは、オンラインで無料で遊べる謎解きを検索できるまとめサイトです。</p>
    </div>
    <h1 class="text-xl font-bold text-white my-4">最新ランキング</h1>
    <Carousel
      v-bind="settings"
      :breakpoints="breakpoints"
      :wrapAround="true"
      snapAlign="start"
      :autoplay="5000"
    >
      <slide v-for="(riddle, index) in ranking" :key="riddle.id">
        <c-rankingCard :riddle="riddle" :index="index" class="relative"></c-rankingCard>
      </slide>
      <template #addons>
        <navigation />
        <pagination />
      </template>
    </carousel>
    <div class="flex justify-between">
      <h1 class="text-xl font-bold text-white my-4">新着一覧</h1>
      <el-link href="/list/" :underline="false">もっと見る</el-link>
    </div>
    <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-y-4 gap-4">
      <c-card v-for="riddle in riddles.results" :key="riddle.id" :riddle="riddle"></c-card>
    </div>
  </div>
</template>
<script setup>
  const runtimeConfig = useRuntimeConfig();
  const { data: ranking } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/ranking/`)
  const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
  const settings = {
    itemsToShow: 2,
  }
  // breakpoints are mobile first
  // any settings not specified will fallback to the carousel settings
  const breakpoints = {
    640: {
      itemsToShow: 3,
    },
    // 700px and up
    768: {
      itemsToShow: 3.5,
    },
    // 1024 and up
    1024: {
      itemsToShow: 5,
    },
    1280: {
      itemsToShow: 6,
    },
  }
  useSeoMeta({
    title: '謎解きデータベース',
    ogTitle: '謎解きデータベース',
    description: '無料で遊べるオンライン謎解きを探すなら、「謎解きデータベース」で検索。',
    ogDescription: '無料で遊べるオンライン謎解きを探すなら、「謎解きデータベース」で検索。',
    ogImage: 'https://***.***/images/ogp.png',
    twitterCard: 'summary_large_image',
  });
  onMounted(() => {
    (window.adsbygoogle = window.adsbygoogle || []).push({});
  });
</script>
<style>
.carousel__pagination-button::after {
  background-color: gray;
}
.carousel__icon {
  fill: black;
  stroke: white;
}
</style>