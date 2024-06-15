<template>
  <div class="bg-gray-800 rounded-md border border-gray-700 h-48 lg:h-56 overflow-hidden">
    <div class="flex flex-row w-40 h-48 lg:w-44 lg:h-56 relative">
      <a :href="`/list/${riddle.id}`">
        <div class="w-40 lg:w-44 h-48 lg:h-56 bg-gray-700 flex items-center">
          <NuxtImg format="webp" :src="riddle.image" width="176" height="224" sizes="160px lg:176px" fit="contain" :alt="riddle.name"/>
        </div>
        <!-- <el-image :src="riddle.image" fit="contain" :alt="riddle.name" class="w-40 lg:w-44 h-48 lg:h-56 bg-gray-700"/> -->
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
      <div class="mx-4 my-2 flex flex-col">
        <a :href="`/list/${riddle.id}`" class="text-base lg:text-lg font-bold truncate w-40">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator.id}`" class="text-sm lg:text-base text-gray-400 hover:text-blue-400 truncate w-40">{{ riddle.creator.name }}</a>
        <div class="flex items-center">
          <el-rate
            v-model="riddle.rating"
            disabled
            :size=rateSize
            disabled-void-color="#8D9095"
          />
          <h4 class="ml-1 text-base lg:text-xl text-gray-300 font-semibold">
            {{ riddle.rating }}
          </h4>
        </div>
        <div class="grid grid-cols-1">
          <div class="flex items-center">
            <el-icon :size=iconSize color="">
              <Location />
            </el-icon>
            <span class="mx-2 text-sm lg:text-base text-gray-300">{{ riddle.type_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size=iconSize color="">
              <Timer />
            </el-icon>
            <span class="mx-2 text-sm lg:text-base text-gray-300">{{ riddle.time_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size=iconSize color="">
              <Key />
            </el-icon>
            <span class="mx-2 text-sm lg:text-base text-gray-300">{{ riddle.level_str }}</span>
          </div>
        </div>
        <el-button
          round
          type="primary"
          tag="a"
          :size=rateSize
          class="text-sm font-semibold mt-2 w-32"
          @click="playingRiddle(riddle.id)"
          :href="riddle.url"
          target="_blank"
          rel="noopener noreferrer"
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
    Key,
    Location,
    Timer,
  } from '@element-plus/icons-vue'
  interface Props {
    riddle: object
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
</script>
