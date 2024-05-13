<template>
  <div class="bg-gray-800 rounded-md border border-gray-700 h-64 overflow-hidden">
    <div class="flex flex-row">
      <a :href="`/list/${riddle.id}`" class="relative">
        <el-image :src="riddle.image" class="h-64" fit="cover"/>
        <div className="absolute inset-x-0 bottom-0 h-9 bg-black bg-opacity-70">
          <span className="flex items-center text-white absolute left-2 bottom-2">
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
        <a :href="`/list/${riddle.id}`" class="text-2xl font-bold truncate w-52">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator.id}`" class="text-lg text-gray-300 hover:text-blue-400 truncate w-52">{{ riddle.creator.name }}</a>
        <div class="flex items-center">
          <el-rate
            v-model="riddle.rating"
            disabled
            size=""
            disabled-void-color="#8D9095"
          />
          <!-- <star-rating
            :increment="0.01"
            :rating="riddle.rating"
            :read-only="true"
            v-bind:star-size="20"
            :show-rating="false"
            inactive-color="#9ca3af"
            active-color="#ffa503"
            :inline="true"
            class="pb-1.5"
          ></star-rating> -->
          <h3 class="ml-1 text-xl text-gray-300 font-semibold">
            {{ riddle.rating }}
          </h3>
        </div>
        <div class="grid grid-cols-1">
          <div class="mt-1 flex items-center">
            <el-icon :size="24" color="">
              <Location />
            </el-icon>
            <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.type_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size="24" color="">
              <Timer />
            </el-icon>
            <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.time_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size="24" color="">
              <Key />
            </el-icon>
            <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.level_str }}</span>
          </div>
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
