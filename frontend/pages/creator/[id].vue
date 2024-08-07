<template>
  <div class="mx-4">
    <div class="my-10 flex justify-center items-center">
      <div class="w-40 h-40 bg-white size-[200px] rounded-full flex items-center overflow-hidden">
        <NuxtImg format="webp" :src="creator.image" width="160" sizes="160px" fit="contain" :alt="creator.name"/>
      </div>
      <!-- <el-image :src="creator.image" fit="contain" class="w-40 h-40 bg-white size-[200px] rounded-full"/> -->
      <div class="ml-10">
        <h3 class="text-xl font-semibold text-gray-800 dark:text-gray-300">
          {{ creator.name }}
        </h3>
        <el-button
          round
          type="primary"
          tag="a"
          class="text-sm font-semibold h-10 mt-4"
          :href="creator.url"
          target="_blank"
          rel="noopener noreferrer"
        >クリエイターサイトへ</el-button>
      </div>
    </div>
    <h1 class="text-xl font-bold text-white my-4">{{ creator.name }}の謎解き一覧</h1>
    <div class="grid grid-cols-2 lg:grid-cols-7 gap-4 mb-4 items-center">
        <!-- キーワード検索 -->
        <div class="col-span-1">
          <el-input
            v-model="selectWord"
            placeholder="キーワード検索"
            clearable
            class="h-10"
            :prefix-icon="Search"
          ></el-input>
        </div>
        <!-- タイプ検索-->
        <div class="col-span-1">
          <el-select
            multiple
            v-model="selectType.value"
            placeholder="タイプ"
            size="large"
          >
            <el-option
              v-for="item in typeSet"
              :key="item.value"
              :label="item.title"
              :value="item.value"
            ></el-option>
          </el-select>
        </div>
        <!-- 時間検索 -->
        <div class="col-span-1">
          <el-select
            multiple
            v-model="selectTime.value"
            placeholder="時間"
            size="large"
          >
            <el-option
              v-for="item in timeSet"
              :key="item.value"
              :label="item.title"
              :value="item.value"
            ></el-option>
          </el-select>
        </div>
        <!-- 難易度検索 -->
        <div class="col-span-1">
          <el-select
            multiple
            v-model="selectLevel.value"
            placeholder="難易度"
            size="large"
          >
            <el-option
              v-for="item in levelSet"
              :key="item.value"
              :label="item.title"
              :value="item.value"
            ></el-option>
          </el-select>
        </div>
        <!-- タグ検索 -->
        <div class="col-span-1">
          <el-select
            multiple
            v-model="selectTag.value"
            placeholder="タグ"
            size="large"
          >
            <el-option
              v-for="item in tagSet"
              :key="item.value"
              :label="item.title"
              :value="item.value"
            ></el-option>
          </el-select>
        </div>
        <!-- 並び替え -->
        <div class="col-span-1">
          <el-select
            v-model="selectOrder"
            placeholder="並べ替え"
            size="large"
          >
            <el-option
              v-for="item in orderSet"
              :key="item.value"
              :label="item.title"
              :value="item.value"
            ></el-option>
          </el-select>
        </div>
        <!-- フィルター -->
        <div class="col-span-2 lg:col-span-1">
          <el-button type="primary" @click="filter" class="w-full" size="large" :icon="Filter">フィルター</el-button>
        </div>
      </div>
    <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-y-4 gap-4">
      <c-card v-for="riddle in response.results" :key="riddle.id" :riddle="riddle"></c-card>
    </div>
    <div class="mt-4 flex justify-center items-center">
      <el-pagination background layout="prev, pager, next" v-model:current-page="page" :page-count="Math.ceil(response.count / 6)" @current-change="paging" :pager-count="4"></el-pagination>
    </div>
  </div>
</template>
<script setup>
  import {
    Filter,
    Search,
  } from '@element-plus/icons-vue'
  const typeSet = [
    {
      title: "WEB",
      value: "web",
    },
    {
      title: "LINE@",
      value: "line",
    },
  ]
  const timeSet = [
    {
      title: "〜30分",
      value: "1",
    },
    {
      title: "30分〜90分",
      value: "2",
    },
    {
      title: "90分〜180分",
      value: "3",
    },
    {
      title: "180分〜",
      value: "4",
    },
  ]
  const levelSet = [
    {
      title: "初級",
      value: "1",
    },
    {
      title: "中級",
      value: "2",
    },
    {
      title: "上級",
      value: "3",
    },
    {
      title: "超上級",
      value: "4",
    },
  ]
  const tagSet = [
    {
      title: "ストーリー◎",
      value: "story",
    },
    {
      title: "ギミック◎",
      value: "gimmick",
    },
    {
      title: "スッキリ◎",
      value: "sukkiri",
    },
  ]
  const orderSet = [
    {
      title: "新着順",
      value: "created_at"
    },
    {
      title: "難易度順",
      value: "level"
    },
    {
      title: "プレイ数順",
      value: "playings"
    },
    {
      title: "評価順",
      value: "rating"
    }
  ]
  const id = useRoute().params.id
  const runtimeConfig = useRuntimeConfig();
  const { data: creator } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/creator/${id}`)
  const page = ref(1)
  const selectWord = ref("")
  const selectType = reactive([])
  const selectTime = reactive([])
  const selectLevel = reactive([])
  const selectTag = reactive([])
  const selectOrder = ref("created_at")
  const query = ref({ 
    creator: creator.value.id,
    page: page.value,
    word: selectWord.value,
    type: selectType.value,
    time: selectTime.value,
    level: selectLevel.value,
    tag: selectTag.value,
    order: selectOrder.value,
  })
  const filter = () => {
    page.value = 1
    query.value = {
      creator: creator.value.id,
      page: page.value,
      word: selectWord.value,
      type: selectType.value,
      time: selectTime.value,
      level: selectLevel.value,
      tag: selectTag.value,
      order: selectOrder.value,
    }
  }
  const paging = () => {
    query.value = {
      creator: creator.value.id,
      page: page.value,
      word: selectWord.value,
      type: selectType.value,
      time: selectTime.value,
      level: selectLevel.value,
      tag: selectTag.value,
      order: selectOrder.value,
    }
  }
  const { data: response } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`, { query })
  useSeoMeta({
    title: () => `${creator.value.name} | 謎解きデータベース`,
    ogTitle: () => `${creator.value.name} | 謎解きデータベース`,
  });
</script>