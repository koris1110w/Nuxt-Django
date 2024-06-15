<template>
  <el-header class="mb-6 border-b border-gray-600">
    <div class="flex justify-between items-center h-full mx-auto container">
      <div class="flex items-center">
        <a href="/" class="text-xl font-600 mr-3 flex  items-center"> 
          <NuxtImg src="/favicon.png" width="36" height="36" alt="謎解きデータベース"/>
          <p class="ml-1">謎解きデータベース</p>
        </a>
        <el-link href="/list/" :underline="false">謎解き一覧</el-link>
      </div>
      <!-- <div class="flex items-center">
        <el-button bg v-if="$colorMode.preference == 'dark'" type="" :icon="Moon" @click="$colorMode.preference = 'light'"/>
        <el-button bg v-else type="" :icon="Sunny" @click="$colorMode.preference = 'dark'"/>
        <el-link href="/list/" :underline="false">log in</el-link>
      </div> -->
    </div>
  </el-header>
</template>
<script setup>
import {
  Sunny,
  Moon,
} from '@element-plus/icons-vue'
</script>