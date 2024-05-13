<template>
  <el-carousel type="card" trigger="click" indicator-position="outside">
    <el-carousel-item v-for="(riddle, index) in ranking" :key="riddle.id">
      <c-rankingCard :riddle="riddle" class="relative"></c-rankingCard>
      <div class="absolute top-3 left-3 text-white w-8 h-8 font-bold flex items-center justify-center" :class="getRankingColor(index)">{{ index + 1 }}</div>
    </el-carousel-item>
  </el-carousel>
  <div class="grid lg:grid-cols-2 lg:gap-y-16 gap-10">
    <c-card v-for="riddle in riddles.results" :key="riddle.id" :riddle="riddle"></c-card>
  </div>
</template>
<script setup>
  const { data: ranking } = await useFetch("http://localhost/api/v1/ranking/")
  const { data: riddles } = await useFetch("http://localhost/api/v1/riddles/")
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
</script>