<template>
  <el-card body-class="">
    <div class="flex flex-row">
      <a :href="`/list/${riddle.id}`">
        <el-image :src="riddle.image" class="w-40"/>
      </a>
      <div class="ml-4 flex flex-col">
        <a :href="`/list/${riddle.id}`" class="text-xl font-bold">{{ riddle.name }}</a>
        <a :href="`/creator/${riddle.creator}`" class="text-lg hover:text-blue-400">{{ riddle.creator }}</a>
        <div class="flex items-center mt-1">
          <el-rate
            v-model="riddle.rating"
            disabled
            size="large"
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
          <h3 class="ml-3 text-xl text-gray-300 font-semibold">
            {{ riddle.rating }}
          </h3>
        </div>
        <div class="flex items-center mt-3">
          <el-icon :size="24" color="black">
            <Location />
          </el-icon>
          <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.type }}</span>
        </div>
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="black">
            <Timer />
          </el-icon>
          <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.time }}</span>
        </div>
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="black">
            <Opportunity />
          </el-icon>
          <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.level }}</span>
        </div>
        <div class="flex items-center mt-1">
          <el-icon :size="24" color="black">
            <Calendar />
          </el-icon>
          <span
            class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.release_date }} ~ {{ riddle.end_date }}</span>
        </div>
        <el-button
          type="primary"
          tag="a"
          size="large"
          class="text-sm font-semibold mt-4"
          :href="riddle.url"
          target="_blank"
          rel="noopener noreferrer"
          @click="playingRiddle(riddle.id)"
        >謎解きサイトへ</el-button>
      </div>
    </div>
  </el-card>
</template>
<script setup lang="ts">
  import {
    Location,
    Timer,
    Opportunity,
    Calendar,
  } from '@element-plus/icons-vue'
  interface Props {
    riddle: object
  }
  const props = defineProps<Props>()
</script>
