<template>
  <h1 class="text-xl font-bold text-white my-4">お問い合わせ</h1>
  <el-card class="m-4" shadow="never">
    <p class="text item">
      <el-link href="https://x.com/nazotokidb" type="primary" target="_blank">X(Twitter)のアカウント(@nazotokidb)</el-link>宛にDMにてご連絡ください。
    </p>
  </el-card>
<!-- <el-button @click="test">test</el-button> -->
</template>
<script setup>
  useSeoMeta({
    title: 'お問い合わせ | 謎解きデータベース',
    ogTitle: 'お問い合わせ | 謎解きデータベース',
  });
  // const test = async () => {
  //   const runtimeConfig = useRuntimeConfig();
  //   const { data: riddle, error } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/1`)
  //   console.log(riddle.name)
  // }
</script>