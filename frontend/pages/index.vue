<template>
  test
  <el-button
    round
    type="primary"
    tag="a"
    size="large"
    class="text-sm font-semibold mt-4 w-40"
    rel="noopener noreferrer"
    @click="test()"
  >button</el-button>
</template>
<script>
  const test = async () => {
    const runtimeConfig = useRuntimeConfig();
    const { data: riddles } = await useFetch(`${runtimeConfig.public.apiUrl}/api/v1/riddles/`)
  }
</script>