<template>
  <div class="my-10 flex justify-center items-center">
    <el-image :src="creator.image" fit="cover" class="w-40 h-40 size-[200px] rounded-full"/>
    <div class="ml-10">
      <h3 class="text-xl font-semibold text-gray-800 group-hover:text-gray-600 dark:text-gray-300 dark:group-hover:text-white">
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
  <div class="grid grid-cols-2 lg:grid-cols-6 gap-4 mb-4 items-center">
    <!-- ワード検索 -->
    <div class="cols-span-1">
      <el-input
        v-model="selectWord"
        placeholder="検索"
        clearable
        class="h-10"
      ></el-input>
    </div>
    <!-- タイプ検索-->
    <div class="cols-span-1">
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
    <div class="cols-span-1">
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
    <div class="cols-span-1">
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
    <!-- 並び替え -->
    <div class="cols-span-1">
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
    <div class="cols-span-1">
      <el-button type="primary" @click="filter" class="w-full" size="large">フィルター</el-button>
    </div>
  </div>
  <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-y-4 gap-4">
    <c-card v-for="riddle in response.results" :key="riddle.id" :riddle="riddle"></c-card>
  </div>
  <div class="mt-4 flex justify-center items-center">
    <el-pagination background layout="prev, pager, next" v-model:current-page="page" :page-count="Math.ceil(response.count / 4)" @current-change="paging"></el-pagination>
  </div>
</template>
<script setup>
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
      title: "〜15分",
      value: "1",
    },
    {
      title: "15分〜45分",
      value: "2",
    },
    {
      title: "45分〜90分",
      value: "3",
    },
    {
      title: "90分〜180分",
      value: "4",
    },
    {
      title: "180分〜",
      value: "5",
    },
  ]
  const levelSet = [
    {
      title: "初級",
      value: "1",
    },
    {
      title: "初中級",
      value: "2",
    },
    {
      title: "中級",
      value: "3",
    },
    {
      title: "上級",
      value: "4",
    },
    {
      title: "超上級",
      value: "5",
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
  const selectOrder = ref("created_at")
  const query = ref({ 
    creator: creator.value.id,
    page: page.value,
    word: selectWord.value,
    type: selectType.value,
    time: selectTime.value,
    level: selectLevel.value,
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
      order: selectOrder.value,
    }
  }
  const { data: response } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`, { query })
  useSeoMeta({
    title: () => `${creator.value.name} | 謎解きデータベース`,
    ogTitle: () => `${creator.value.name} | 謎解きデータベース`,
  });
</script>