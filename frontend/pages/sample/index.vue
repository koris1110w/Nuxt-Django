<template>
  test
  <el-button
    round
    type="primary"
    size="large"
    class="text-sm font-semibold mt-4 w-40"
    @click="aaa()"
  >button</el-button>
  <ClientOnly>
    <c-canvas></c-canvas>
  </ClientOnly>
</template>
<script setup>
  const runtimeConfig = useRuntimeConfig();
  console.log(runtimeConfig.public.test)
  console.log(runtimeConfig.public.apiUrl)
  const { data: samples, error } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
  console.log("samples")
  console.log(samples)
  const aaa = async () => {
    console.log("test")
    const runtimeConfig = useRuntimeConfig();
    console.log(runtimeConfig.public.test)
    console.log(runtimeConfig.public.apiUrl)
    const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    console.log("riddles")
    console.log(riddles)
  }
</script>