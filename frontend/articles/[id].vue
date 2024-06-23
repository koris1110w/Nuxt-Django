<template>
  <article>
    <div class="flex justify-center items-center">
      <NuxtImg src="/favicon.png" width="100" height="100" alt="謎解きデータベース"/>
      <div class="ml-4">
        <h1 class="text-2xl">解けたら天才！超高難易度謎解き5選</h1>
        <p class="text-gray-300">これが解けたらあなたも天才！？一筋縄では解けない超高難易度謎解きを集めました。</p>
      </div>
    </div>
    <div class="flex justify-center">
      <div class="w-3/4">
        <span class="text-blue-500">{{ response.creator.name }}</span>
        <h1 class="text-2xl font-bold">{{ response.name }}</h1>
        <div class="flex mt-2">
          <div class="w-1/3 h-48 bg-gray-200 flex items-center">
            <NuxtImg :src="response.image" fit="contain" :alt="response.name" />
          </div>
          <div class="ml-4 w-2/3">
            <div v-html="htmlContent" class="text-gray-100 text-md leading-relaxed"></div>
          </div>
        </div>
      </div>
    </div>
    <div>

    </div>
  </article>
</template>

<script setup>
  const runtimeConfig = useRuntimeConfig();
  const url = ref(runtimeConfig.public.apiUrl)
  const { data: response } = await useFetch(`${url.value}/api/v1/riddles/1/`)

  import MarkdownIt from 'markdown-it'
  const md = new MarkdownIt()
  const htmlContent = md.render(response.value.content)
</script>

<style>
  h2 {
    font-size:larger;
    font-weight: bold;
    color: royalblue;
    margin-bottom: 16px;
  }
  strong {
    background: linear-gradient(transparent 70%, #FFA503 70%);
  }
</style>