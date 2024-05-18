<template>
  <el-header class="mb-6 border-b border-gray-600">
    <div class="flex justify-between items-center h-full mx-auto container">
      <div class="flex items-center">
        <a href="/" class="text-xl font-600 mr-3 flex  items-center"> 
          <img src="~/assets/img/favicon.png" class="w-9 h-9"/>
          <p class="ml-1">謎解きデータベース</p>
        </a>
        <el-link href="/list/" :underline="false">謎解き一覧</el-link>
      </div>
      <!-- <div class="flex items-center">
        <el-link href="/list/" :underline="false">log in</el-link>
      </div> -->
    </div>
  </el-header>
</template>