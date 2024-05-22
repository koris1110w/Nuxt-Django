<template>
  <div class="bg-gray-800 rounded-md border border-gray-700 h-56 overflow-hidden">
    <div class="flex flex-row w-44 h-56 relative">
      <a :href="`/list/${riddle.id}`">
        <el-image :src="riddle.image" class="w-44 h-56" fit="cover"/>
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
        <a :href="`/list/${riddle.id}`" class="text-xl font-bold truncate w-40">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator.id}`" class="text-md text-gray-400 hover:text-blue-400 truncate w-40">{{ riddle.creator.name }}</a>
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
        <div class="grid grid-cols-1">
          <div class="flex items-center">
            <el-icon :size="20" color="">
              <Location />
            </el-icon>
            <span class="mx-2 text-md text-gray-300">{{ riddle.type_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size="20" color="">
              <Timer />
            </el-icon>
            <span class="mx-2 text-md text-gray-300">{{ riddle.time_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size="20" color="">
              <Key />
            </el-icon>
            <span class="mx-2 text-md text-gray-300">{{ riddle.level_str }}</span>
          </div>
        </div>
        <el-button
          round
          type="primary"
          tag="a"
          size="default"
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
