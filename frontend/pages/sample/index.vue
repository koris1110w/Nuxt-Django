<template>
  test
  <el-button
    round
    type="primary"
    size="large"
    class="text-sm font-semibold mt-4 w-40"
    @click="test()"
  >button</el-button>
</template>
<script setup>
  const runtimeConfig = useRuntimeConfig();
  console.log(runtimeConfig.public.apiUrlOnServer)
  const { data: samples, error } = await useFetch(`${runtimeConfig.public.apiUrlOnServer}/api/v1/riddles/`)
  console.log("samples")
  console.log(samples)
  const { data: testb } = await useFetch("/api/v1/riddles/")
  console.log("testb")
  console.log(testb)
  const { data: testc } = await useFetch("nazotokidb.com/api/v1/riddles/")
  console.log("testc")
  console.log(testc)
  const { data: testd } = await useFetch("http://nazotokidb.com/api/v1/riddles/")
  console.log("testd")
  console.log(testd)
  const { data: teste } = await useFetch("https://nazotokidb.com/api/v1/riddles/")
  console.log("teste")
  console.log(teste)
  const test = async () => {
    console.log("test")
    const runtimeConfig = useRuntimeConfig();
    console.log(runtimeConfig.public.apiUrl)
    const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    console.log("riddles")
    console.log(riddles)
  }
</script>