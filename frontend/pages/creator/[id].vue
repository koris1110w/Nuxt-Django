<template>
  <div>
    <h1>Top Page</h1>
    <ul>
      <li v-for="riddle in response.results" :key="riddle.id">
        {{ riddle.id }}, {{ riddle.name }}
      </li>
    </ul>
    <NuxtLink to="/">Price</NuxtLink>
  </div>
</template>
<script setup>
  const { data: response, error } = await useFetch('http://localhost:80/api/v1/riddles/')
</script>