<template>
  <div class="bg-gray-800 rounded-md border border-gray-700 overflow-hidden h-80">
    <div class="flex flex-col">
      <a :href="`/list/${riddle.id}`" class="relative">
        <el-image :src="riddle.image" class="w-52 h-56" fit="cover"/>
        <div className="absolute inset-x-0 bottom-0 h-8 bg-black bg-opacity-70">
          <span className="flex items-center text-white absolute left-2 bottom-1">
            <el-icon :size="16" color="">
              <VideoPlay />
            </el-icon>
            <span class="ml-2">
              {{ riddle.playings }}
            </span>
          </span>
        </div>
      </a>
      <a :href="`/list/${riddle.id}`" class="text-2xl font-bold">{{ riddle.name }}</a>
      <a :href="`/creator/${riddle.creator.id}`" class="text-lg text-gray-300 hover:text-blue-400">{{ riddle.creator.name }}</a>
      <div class="flex items-center">
        <el-rate
          v-model="riddle.rating"
          disabled
          size=""
          disabled-void-color="#8D9095"
        />
        <h3 class="ml-1 text-xl text-gray-300 font-semibold">
          {{ riddle.rating }}
        </h3>
      </div>
      <el-button
        type="primary"
        tag="a"
        size="large"
        class="text-sm font-semibold mt-4 w-40"
        :href="riddle.url"
        target="_blank"
        rel="noopener noreferrer"
        @click="playingRiddle(riddle.id)"
      >謎解きサイトへ</el-button>
    </div>
  </div>
</template>
<script setup lang="ts">
  import {
    VideoPlay,
    Key,
    Location,
    Timer,
  } from '@element-plus/icons-vue'
  interface Props {
    riddle: object
  }
  const props = defineProps<Props>()
  const playingRiddle = async (id) => {
    const postData = {}
    const { data } = await useFetch(`http://localhost:80/api/v1/riddles/${id}`, {
      method: 'POST',
      body: postData,
    });
  }
</script>
