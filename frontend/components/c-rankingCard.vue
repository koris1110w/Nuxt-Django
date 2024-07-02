<template>
  <div class="bg-white dark:bg-gray-800 rounded-md border border-gray-300 dark:border-gray-700 overflow-hidden w-44 pb-2 drop-shadow-md">
    <div class="flex flex-col">
      <a :href="`/list/${riddle.id}`" class="relative">
        <div class="w-44 h-44 bg-gray-100 dark:bg-gray-700 flex items-center overflow-hidden">
          <NuxtImg format="webp" :src="riddle.image" width="176" sizes="176px" fit="contain" :alt="riddle.name"/>
        </div>
        <!-- <el-image :src="riddle.image" sizes="176px" fit="contain" :alt="riddle.name" class="w-44 h-44 bg-gray-700"/> -->
        <div class="absolute top-2 left-2 text-white w-8 h-8 font-bold flex items-center justify-center" :class="getRankingColor(index)">{{ index + 1 }}</div>
        <div class="flex flex-wrap-reverse absolute bottom-2 left-0">
          <el-tag
            v-if="riddle.story >= 4"
            class="mt-1 ml-1"
            type="primary"
            effect="light"
            round
            size="small"
          >
            ストーリー◎
          </el-tag>
          <el-tag
            v-if="riddle.gimmick >= 4"
            class="mt-1 ml-1"
            type="primary"
            effect="light"
            round
            size="small"
          >
            ギミック◎
          </el-tag>
          <el-tag
            v-if="riddle.sukkiri >= 4"
            class="mt-1 ml-1"
            type="primary"
            effect="light"
            round
            size="small"
          >
            スッキリ◎
          </el-tag>
        </div>
        <!-- <div class="absolute inset-x-0 bottom-0 h-8 bg-black bg-opacity-70">
          <span class="flex items-center text-white absolute left-2 bottom-1">
            <el-icon :size="16" color="">
              <VideoPlay />
            </el-icon>
            <span class="ml-2">
              {{ riddle.playings }}
            </span>
          </span>
        </div> -->
      </a>
      <div class="mx-2 flex flex-col items-start">
        <a :href="`/list/${riddle.id}`" class="text-base lg:text-lg font-bold truncate w-40 text-left">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator.id}`" class="text-sm text-gray-700 dark:text-gray-300 hover:text-blue-400 dark:hover:text-blue-400 truncate w-40 text-left">{{ riddle.creator.name }}</a>
        <div class="flex items-center">
          <el-rate
            v-model="riddle.rating"
            disabled
            :size=rateSize
            disabled-void-color="#8D9095"
          />
          <h4 class="ml-1 text-base lg:text-xl text-gray-700 dark:text-gray-300 font-semibold">
            {{ riddle.rating }}
          </h4>
        </div>
        <el-button
          round
          type="primary"
          tag="a"
          size="small"
          class="text-sm font-semibold w-full"
          :href="riddle.url"
          target="_blank"
          rel="noopener noreferrer"
          @click="playingRiddle(riddle.id)"
        >謎解きサイトへ</el-button>
      </div>
    </div>
  </div>
</template>
<script setup lang="ts">
  import { useWindowSize } from '@vueuse/core';
  const { width } = useWindowSize();
  const rateSize = computed(() => {
    if (width.value < 1024) {
      return 'small'
    } else {
      return 'default'
    }
  })
  const iconSize = computed(() => {
    if (width.value < 1024) {
      return 16
    } else {
      return 20
    }
  })
  import {
    VideoPlay,
  } from '@element-plus/icons-vue'
  interface Props {
    riddle: object
    index: number
  }
  const props = defineProps<Props>()
  const runtimeConfig = useRuntimeConfig();
  const playingRiddle = async (id) => {
    const postData = {}
    const { data } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/playing/${id}/`, {
      method: 'POST',
      body: postData,
    });
  }
  const getRankingColor = (index) => {
    if(index == 0) {
      return "bg-yellow-400"
    }else if(index == 1) {
      return "bg-gray-400"
    }else if(index == 2) {
      return "bg-yellow-700"
    }else{
      return "bg-gray-800"
    }
  }
</script>
