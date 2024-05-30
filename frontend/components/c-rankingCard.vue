<template>
  <div class="bg-gray-800 rounded-md border border-gray-700 overflow-hidden w-48 h-76 pb-2">
    <div class="flex flex-col">
      <a :href="`/list/${riddle.id}`" class="relative">
        <el-image :src="riddle.image" class="w-48 h-44 bg-white" fit="contain"/>
        <div class="absolute top-2 left-2 text-white w-8 h-8 font-bold flex items-center justify-center" :class="getRankingColor(index)">{{ index + 1 }}</div>
        <div class="flex flex-wrap-reverse absolute bottom-9 left-0">
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
      <div class="mx-2 flex flex-col items-start">
        <a :href="`/list/${riddle.id}`" class="text-lg font-bold truncate w-44 text-left">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator.id}`" class="text-sm text-gray-300 hover:text-blue-400 truncate w-44 text-left">{{ riddle.creator.name }}</a>
        <div class="flex items-center">
          <el-rate
            v-model="riddle.rating"
            disabled
            size="default"
            disabled-void-color="#8D9095"
          />
          <h3 class="ml-1 text-xl text-gray-300 font-semibold">
            {{ riddle.rating }}
          </h3>
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
      return "bg-gray-700"
    }
  }
</script>
