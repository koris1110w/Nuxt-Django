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
  const { data: testf } = await useFetch("https://nginx:8080/api/v1/riddles/")
  console.log("testf")
  console.log(testf)
  const { data: testg } = await useFetch("https://https-portal:443/api/v1/riddles/")
  console.log("testg")
  console.log(testg)
  const { data: testh } = await useFetch("http://https-portal:443/api/v1/riddles/")
  console.log("testh")
  console.log(testh)
  const { data: testi } = await useFetch("https://https-portal/api/v1/riddles/")
  console.log("testi")
  console.log(testi)
  const { data: testj } = await useFetch("http://https-portal/api/v1/riddles/")
  console.log("testj")
  console.log(testj)
  const { data: testk } = await useFetch("http://157.7.207.38/api/v1/riddles/")
  console.log("testk")
  console.log(testk)
  const { data: testl } = await useFetch("https://157.7.207.38/api/v1/riddles/")
  console.log("testl")
  console.log(testl)
  const test = async () => {
    console.log("test")
    const runtimeConfig = useRuntimeConfig();
    console.log(runtimeConfig.public.apiUrl)
    const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
    console.log("riddles")
    console.log(riddles)
  }
</script>