<template>
  <el-affix>
    <el-header class="mb-6 border-b border-gray-600 bg-white dark:bg-gray-900">
      <div class="flex items-center h-full mx-auto container">
        <a href="/" class="text-xl font-600 mr-3 flex items-center"> 
          <NuxtImg v-if="$colorMode.preference == 'dark'" src="/logo_dark.png" fit="contain" :height="img_h" alt="謎解きデータベース"/>
          <NuxtImg v-else src="/logo_light.png" fit="contain" :height="img_h" alt="謎解きデータベース"/>
        </a>
        <div class="flex justify-between w-full">
        <!-- <div v-if="width > 768" class="flex justify-between w-full"> -->
          <div class="flex items-center">
            <div class="ml-4">
              <el-link href="/list/" :underline="false">謎解き一覧</el-link>
            </div>
            <div class="ml-8">
              <el-link href="/articles/" :underline="false">厳選謎解き</el-link>
            </div>
          </div>
          <div class="flex items-center">
            <!-- <div class="">
              <el-input
                v-model="header_input"
                style="max-width: 600px"
                placeholder="謎解きを検索"
                class=""
              >
                <template #append>
                  <el-button :icon="Search" />
                </template>
              </el-input>
            </div> -->
            <!-- <div class="ml-4">
              <el-button bg v-if="$colorMode.preference == 'dark'" type="" :icon="Moon" @click="$colorMode.preference = 'light'"/>
              <el-button bg v-else type="" :icon="Sunny" @click="$colorMode.preference = 'dark'"/>
            </div> -->
            <!-- <el-link href="/list/" :underline="false">log in</el-link> -->
          </div>
        </div>
        <!-- <div v-else class="flex justify-end w-full">
          <el-button :icon="More" link @click="drawer = true" size="large"/>
          <el-drawer
            v-model="drawer"
          >
            <div class="flex flex-col gap-4 items-center">
              <el-link href="/list/" :underline="false" class="">謎解き一覧</el-link>
              <el-link href="/articles/" :underline="false" class="">厳選謎解き</el-link>
              <div class="">
                <el-button bg v-if="$colorMode.preference == 'dark'" type="" :icon="Moon" @click="$colorMode.preference = 'light'"/>
                <el-button bg v-else type="" :icon="Sunny" @click="$colorMode.preference = 'dark'" />
              </div>
            </div>
          </el-drawer>
        </div> -->
      </div>
    </el-header>
  </el-affix>
</template>
<script setup>
  import {
    Sunny,
    Moon,
    Search,
    More,
  } from '@element-plus/icons-vue'

  const header_input = ref("")
  const drawer = ref(false)

  import { useWindowSize } from '@vueuse/core';
  const { width } = useWindowSize();
  const img_h = computed(() => {
    if (width.value < 1024) {
      return 28
    } else {
      return 36
    }
  })
</script>