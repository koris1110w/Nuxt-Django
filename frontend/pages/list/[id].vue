<template>
  <div class="grid lg:grid-cols-3 gap-4">
    <div class="flex justify-center">
      <span class="relative"> 
        <el-image :src="riddle.image" class="h-80" fit="cover"/>
        <div className="absolute inset-x-0 bottom-0 h-10 bg-black bg-opacity-70">
          <span className="flex items-center text-white absolute left-4 bottom-3">
            <el-icon :size="16" color="">
              <Key />
            </el-icon>
            <span class="ml-2">
              {{ riddle.playings }}
            </span>
          </span>
        </div>
      </span>
    </div>
    <div class="ml-4 flex flex-col">
      <a :href="`/list/${riddle.id}`" class="text-xl font-bold">{{ riddle.name }}</a>
      <a :href="`/creator/${riddle.creator.id}`" class="text-lg hover:text-blue-400">{{ riddle.creator.name }}</a>
      <div class="flex items-center mt-1">
        <el-rate
          v-model="riddle.rating"
          disabled
          size="large"
        />
        <h3 class="ml-3 text-xl text-gray-300 font-semibold">
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
              <Opportunity />
            </el-icon>
            <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.level_str }}</span>
          </div>
          <div class="flex items-center mt-1">
            <el-icon :size="24" color="">
              <Calendar />
            </el-icon>
            <span
              class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.release_date }} ~ {{ riddle.end_date }}</span>
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
    <div>
      <c-radarchart 
        :chartId="'my-radar-chart'"
        :cssClasses="'my-radar-chart-container'"
        :riddle="riddle"
         />
    </div>
  </div>
  <el-collapse>
    <el-collapse-item title="説明">
      <div>
        {{ riddle.description }}
      </div>
    </el-collapse-item>
  </el-collapse>
</template>
<script setup>
  import {
    Key,
    Location,
    Timer,
    Opportunity,
    Calendar,
  } from '@element-plus/icons-vue'
  const id = useRoute().params.id
  const { data: riddle, error } = await useFetch(`http://localhost:80/api/v1/riddles/${id}`)
</script>