<template>
  <div class="mx-4">
    <h1 class="text-xl font-bold my-4">厳選謎解き</h1>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      <div v-for="article in response" :key="article.id" class="mt-6 col-span-1">
        <a :href="`/articles/${article.id}`" class="group hover:opacity-80">
          <div class="">
            <div class="w-full h-52 overflow-hidden drop-shadow">
              <el-image :src="article.image" :alt="article.title" fit="cover"/>
            </div>
            <div class="">
              <h1 class="mt-2 text-lg group-hover:underline">{{ article.title }}</h1>
              <div class="flex items-center">
                <el-icon size="small" color="">
                  <Clock />
                </el-icon>
                <p class="ml-2 text-sm text-gray-700 dark:text-gray-300">{{ article.created_at.slice(0, 10) }}</p>
              </div>
            </div>
          </div>
        </a>
      </div>
    </div>
    <c-adcards></c-adcards>
  </div>
</template>

<script setup>
  useSeoMeta({
    title: '厳選謎解き | 謎解きデータベース',
    ogTitle: '厳選謎解き | 謎解きデータベース',
  });

  import {
    Clock,
  } from '@element-plus/icons-vue'

  const runtimeConfig = useRuntimeConfig();
  const url = ref(runtimeConfig.public.apiUrl)
  const { data: response } = await useFetch(`${url.value}/api/v1/articles/`)
</script>