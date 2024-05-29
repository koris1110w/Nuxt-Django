<template>
  <html class="dark bg-gray-900">
    <NuxtLayout>
      <NuxtPage />
    </NuxtLayout>
  </html>
</template>
<script lang="ts" setup>
  import 'element-plus/theme-chalk/dark/css-vars.css'
  import './assets/styles/main.css'
  useHead({
    title: "謎解きデータベース",
    link: [
      {rel: "stylesheet", href: "https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap"}
    ]
  })
  // ➊ divコンテナーの参照
  const containerRef = ref<HTMLDivElement>();

  // ➋ コンポーネントがマウントされたときの処理
  onMounted(() => {
    // スクリプトを定義 (AdSense本体をロード)
    const adsScript = document.createElement(`script`);
    adsScript.async = true;
    adsScript.crossOrigin = `anonymous`;
    adsScript.src = `https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-7081501069094845`;

    // スクリプトを定義 (AdSense実行)
    const inlineScript = document.createElement(`script`);
    inlineScript.type = `text/javascript`;
    inlineScript.text = `(adsbygoogle = window.adsbygoogle || []).push({});`;

    // DOMに追加
    containerRef.value.appendChild(adsScript);
    containerRef.value.appendChild(inlineScript);
  });
</script>