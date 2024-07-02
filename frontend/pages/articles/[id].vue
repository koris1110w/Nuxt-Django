<template>
  <article class="mx-4 flex justify-center">
    <div class="lg:w-3/4">
      <div class="flex">
        <NuxtImg :src="response.image" :width="img_w" :height="img_h" :alt="response.title"/>
        <!-- <el-image :src="response.image" :alt="response.title" class="w-40 h-44" fit="contain"/> -->
        <div class="ml-4">
          <h1 class="text-lg lg:text-2xl font-bold">{{ response.title }}</h1>
          <p class="text-sm lg:text-md mt-4 text-gray-700 dark:text-gray-300">{{ response.description }}</p>
          <div class="mt-2 flex items-center">
            <el-icon size="small" color="">
              <Clock />
            </el-icon>
            <p class="ml-2 text-sm text-gray-700 dark:text-gray-300">{{ response.created_at.slice(0, 10) }}</p>
          </div>
        </div>
      </div>
      <div v-for="(riddle, index) in response.riddles" :key="riddle.id" class="mt-16">
        <div class="">
          <a :href="`/list/${riddle.id}/`" class="hover:opacity-80">
            <div class="flex items-center">
              <span class="text-5xl lg:text-6xl">0{{ index + 1 }}</span>
              <div class="ml-2">
                <span class="text-sm lg:text-lg text-blue-500">{{ riddle.creator.name }}</span>
                <h1 class="text-xl lg:text-2xl font-bold">{{ riddle.name }}</h1>
              </div>
            </div>
            <div class="flex mt-2 flex-col lg:flex-row">
              <div class="lg:w-1/3 lg:h-48 bg-gray-200 dark:bg-gray-800 w-full max-h-48 flex items-center justify-center overflow-hidden">
                <NuxtImg :src="riddle.image" height="192" fit="contain" :alt="riddle.name" />
              </div>
              <div class="mt-4 lg:mt-0 lg:ml-4 lg:w-2/3">
                <div v-if="riddle.review != null" v-html="md.render(riddle.review)" class="text-gray-700 dark:text-gray-300 text-md leading-relaxed"></div>
                <div v-else class="text-gray-700 dark:text-gray-300 text-md leading-relaxed">情報なし</div>
              </div>
            </div>
          </a>
          <div class="mt-8">
            <el-descriptions
              direction="vertical"
              :column="columns"
              size="large"
              border
            >
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Location />
                    </el-icon>
                    タイプ
                  </div>
                </template>
                {{ riddle.type_str }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Timer />
                    </el-icon>
                    所要時間
                  </div>
                </template>
                {{ riddle.time_str }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Key />
                    </el-icon>
                    難易度
                  </div>
                </template>
                {{ riddle.level_str }}
              </el-descriptions-item>
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Opportunity/>
                    </el-icon>
                    スッキリ
                  </div>
                </template>
                {{ riddle.sukkiri }} / 5点
              </el-descriptions-item>
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Notebook />
                    </el-icon>
                    ストーリー
                  </div>
                </template>
                {{ riddle.story }} / 5点
              </el-descriptions-item>
              <el-descriptions-item>
                <template #label>
                  <div class="flex items-center">
                    <el-icon :style="iconStyle">
                      <Setting/>
                    </el-icon>
                    ギミック
                  </div>
                </template>
                {{ riddle.gimmick }} / 5点
              </el-descriptions-item>
            </el-descriptions>
          </div>
        </div>
      </div>
    </div>
  </article>
</template>

<script setup>
  const runtimeConfig = useRuntimeConfig();
  const url = ref(runtimeConfig.public.apiUrl)
  const id = useRoute().params.id
  const { data: response } = await useFetch(`${url.value}/api/v1/articles/${id}/`)

  import { useWindowSize } from '@vueuse/core';
  const { width } = useWindowSize();
  const columns = computed(() => {
    if (width.value < 1024) {
      return 3
    } else {
      return 6
    }
  })

  const img_w = computed(() => {
    if (width.value < 768) {
      return 150
    } else if (width.value < 1024) {
      return 150
    } else {
      return 200
    }
  })

  const img_h = computed(() => {
    if (width.value < 768) {
      return 120
    } else if (width.value < 1024) {
      return 120
    } else {
      return 160
    }
  })

  import {
    Key,
    Location,
    Timer,
    Clock,
    Opportunity,
    Notebook,
    Setting,
  } from '@element-plus/icons-vue'

  import MarkdownIt from 'markdown-it'
  const md = new MarkdownIt()

  useSeoMeta({
    title: () => `${response.value.title} | 謎解きデータベース`,
    ogTitle: () => `${response.value.title} | 謎解きデータベース`,
    description: () => response.value.description,
    ogDescription: () => response.value.description,
  });
</script>

<style>
  h2 {
    font-size:larger;
    font-weight: bold;
    color: #409eff;
    margin-bottom: 16px;
  }
  strong {
    font-weight:100;
    background: linear-gradient(transparent 80%, #F39900 80%);
  }
</style>