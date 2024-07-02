<template>
  <div class="grid lg:grid-cols-3 gap-4">
    <div class="flex justify-center">
      <span class="relative"> 
        <div class="flex items-center h-96 bg-gray-100 dark:bg-gray-700 overflow-hidden">
          <NuxtImg :src="riddle.image" width="384" sizes="384px" fit="contain" :alt="riddle.name"/>
        </div>
        <!-- <div class="absolute inset-x-0 bottom-0 h-10 bg-black bg-opacity-70">
          <span class="flex items-center text-white absolute left-3 bottom-2">
            <el-icon :size="16" color="">
              <VideoPlay />
            </el-icon>
            <span class="ml-2">
              {{ riddle.playings }}
            </span>
          </span>
        </div> -->
      </span>
    </div>
    <div class="ml-4 flex flex-col items-start">
      <a class="text-xl font-bold break-words">{{ riddle.name }}</a>
      <a :href="`/creator/${riddle.creator.id}`" class="text-lg text-gray-600 dark:text-gray-400 hover:text-blue-400 dark:hover:text-blue-400 break-words">{{ riddle.creator.name }}</a>
      <div class="flex items-center mt-1">
        <el-rate
          v-model="riddle.rating"
          disabled
          size="large"
        />
        <h3 class="ml-3 text-xl text-gray-700 dark:text-gray-300 font-semibold">
          {{ riddle.rating }}
        </h3>
      </div>
      <div class="grid grid-cols-1 gap-1">
        <div class="mt-1 flex items-center">
          <el-icon :size="24" color="">
            <Location />
          </el-icon>
          <span class="ml-2 text-gray-700 dark:text-gray-300 font-semibold">タイプ</span>
          <span class="ml-10 text-gray-700 dark:text-gray-300">{{ riddle.type_str }}</span>
        </div>
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="">
            <Timer />
          </el-icon>
          <span class="ml-2 text-gray-700 dark:text-gray-300 font-semibold">所要時間</span>
          <span class="mx-10 text-gray-700 dark:text-gray-300">{{ riddle.time_str }}</span>
        </div>
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="">
            <Key />
          </el-icon>
          <span class="ml-2 text-gray-700 dark:text-gray-300 font-semibold">難易度</span>
          <span class="mx-10 text-gray-700 dark:text-gray-300">{{ riddle.level_str }}</span>
        </div>
        <!-- <div class="flex items-center mt-1">
          <el-icon :size="24" color="">
            <VideoPlay />
          </el-icon>
          <span class="ml-2 text-gray-700 dark:text-gray-300 font-semibold">プレイ回数</span>
          <span class="mx-10 text-gray-700 dark:text-gray-300">{{ riddle.playings }}回</span>
        </div> -->
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="">
            <Calendar />
          </el-icon>
          <span class="ml-2 text-gray-700 dark:text-gray-300 font-semibold">ゲーム期間</span>
          <span v-if="riddle.start_date || riddle.end_date" class="mx-10 text-gray-700 dark:text-gray-300">{{ riddle.start_date }} ~ {{ riddle.end_date }}</span>
          <span v-else class="mx-10 text-gray-700 dark:text-gray-300">情報なし</span>
        </div>
      </div>
      <el-button
        round
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
    <div>
      <c-radarchart 
        :chartId="'my-radar-chart'"
        :cssClasses="'my-radar-chart-container'"
        :riddle="riddle"
         />
    </div>
  </div>
  <div class="container mt-10 px-4 sm:px-0">
    <el-collapse v-model="activeName">
      <el-collapse-item title="説明" name="1">
        <div v-if="riddle.description == ''" class="text-lg">
          説明なし
        </div>
        <div v-else class="text-lg">
          {{ riddle.description }}
        </div>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>
<script setup lang="ts">
  // import type { Riddle } from "~~/types/type"
  import {
    VideoPlay,
    Key,
    Location,
    Timer,
    Calendar,
  } from '@element-plus/icons-vue'
  const activeName = ref('1')
  const id = useRoute().params.id
  const runtimeConfig = useRuntimeConfig();
  const { data: riddle, error } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/${id}`)
  const playingRiddle = async (id: number) => {
    const postData = {}
    const { data } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/playing/${id}/`, {
      method: 'POST',
      body: postData,
    });
  }

  import MarkdownIt from 'markdown-it'
  const md = new MarkdownIt()

  useSeoMeta({
    title: () => `${riddle.value.name} | 謎解きデータベース`,
    ogTitle: () => `${riddle.value.name} | 謎解きデータベース`,
    description: () => riddle.value.description,
    ogDescription: () => riddle.value.description,
  });
</script>