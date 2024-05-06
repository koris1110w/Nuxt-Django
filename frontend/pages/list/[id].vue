<template>
  <div>
    <h1>{{ $route.params.id }}</h1>
  </div>
</template>
<script setup>
  const { data, error } = await useFetch('http://localhost:80/api/v1/riddles/', {
    transform: data => data.filter(content => content.id === $route.params.id)
  })
  console.log(data)
  console.log(data)
</script>