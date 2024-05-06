<template>
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
        v-model="selectType"
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
        v-model="selectTime"
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
        v-model="selectLevel"
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
      <el-button type="primary" @click="getRiddleList" class="w-full" size="large">フィルター</el-button>
    </div>
  </div>
</template>
<script setup>
  const typeSet = [
    {
      title: "WEB",
      value: "web",
    },
    {
      title: "LINE",
      value: "line",
    },
  ]
  const timeSet = [
    {
      title: "〜15分",
      value: "10",
    },
    {
      title: "15分〜45分",
      value: "30",
    },
    {
      title: "45分〜90分",
      value: "60",
    },
    {
      title: "90分〜180分",
      value: "120",
    },
    {
      title: "180分〜",
      value: "300",
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
</script>