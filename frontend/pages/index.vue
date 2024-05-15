<template>
  <h1 class="text-xl font-bold text-white my-4">最新ランキング</h1>
  <Carousel
    v-bind="settings"
    :breakpoints="breakpoints"
    :wrapAround="true"
    snapAlign="start"
  >
    <slide v-for="(riddle, index) in ranking" :key="riddle.id">
      <c-rankingCard :riddle="riddle" class="relative"></c-rankingCard>
      <div class="absolute top-3 left-5 text-white w-8 h-8 font-bold flex items-center justify-center" :class="getRankingColor(index)">{{ index + 1 }}</div>
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
</template>
<script setup>
  const runtimeConfig = useRuntimeConfig();
  const { data: ranking } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/ranking/`)
  const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
  const getRankingColor = (index) => {
    if(index == 0) {
      return "bg-yellow-400"
    }else if(index == 1) {
      return "bg-gray-400"
    }else if(index == 2) {
      return "bg-yellow-700"
    }else{
      return "bg-gray-700"
    }
  }
  const settings = {
    itemsToShow: 2,
  }
  // breakpoints are mobile first
  // any settings not specified will fallback to the carousel settings
  const breakpoints = {
    640: {
      itemsToShow: 2.5,
    },
    // 700px and up
    768: {
      itemsToShow: 3,
    },
    // 1024 and up
    1024: {
      itemsToShow: 4,
    },
    1280: {
      itemsToShow: 5,
    },
  }
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