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
  const aaa = async () => {
    console.log("test")
    const runtimeConfig = useRuntimeConfig();
    console.log(runtimeConfig.public.test)
    console.log(runtimeConfig.public.apiUrl)
    const { data: riddles, error } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    console.log("riddles")
    console.log(riddles)
    console.log("error")
    console.log(error)
    const { data: samples } = await useAsyncData(
      'samples',
      () => $fetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    )
    console.log("samples")
    console.log(samples)
  }
</script>