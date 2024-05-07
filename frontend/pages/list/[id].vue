<template>
  <div class="grid lg:grid-cols-3">
    <el-image :src="riddle.image" class="h-80 mx-auto"/>
    <div class="ml-4 flex flex-col">
      <a :href="`/list/${riddle.id}`" class="text-xl font-bold">{{ riddle.name }}</a>
      <a :href="`/creator/${riddle.creator}`" class="text-lg hover:text-blue-400">{{ riddle.creator }}</a>
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
      <div class="flex items-center mt-3">
        <!-- <el-icon :size="24" color="white">
          <Location></Location>
        </el-icon> -->
        <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.type }}</span>
      </div>
      <div class="flex items-center mt-1">
        <!-- <el-icon :size="24" color="white">
          <Timer></Timer>
        </el-icon> -->
        <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.time }}</span>
      </div>
      <div class="flex items-center mt-1">
        <!-- <el-icon :size="24" color="white">
          <Opportunity></Opportunity>
        </el-icon> -->
        <span class="mx-4 text-gray-700 dark:text-gray-300">{{ riddle.level }}</span>
      </div>
      <div class="flex items-center mt-1">
        <!-- <el-icon :size="24" color="white">
          <Calendar></Calendar>
        </el-icon> -->
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
  const id = useRoute().params.id
  const { data: riddle, error } = await useFetch(`http://localhost:80/api/v1/riddles/${id}`)
</script>