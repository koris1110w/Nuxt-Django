<template>
  test
  <el-button
    round
    type="primary"
    size="large"
    class="text-sm font-semibold mt-4 w-40"
    @click="aaa()"
  >button</el-button>
</template>
<script setup>
  const aaa = async () => {
    console.log("test")
    const runtimeConfig = useRuntimeConfig();
    const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    console.log(riddles.value.results[0].name)
  }
</script>