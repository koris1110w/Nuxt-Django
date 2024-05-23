<template>
  <canvas ref="canvasRef" width="300" height="300"></canvas>
</template>

<script lang="ts" setup>
import { fabric } from "fabric";

// template内のキャンバスを参照
const canvasRef = ref<HTMLCanvasElement>();

onMounted(() => {
  // fabricを初期化
  const canvas = new fabric.Canvas(canvasRef.value!);
  canvas.isDrawingMode = true; // お絵描きモードを有効
});
</script>

<style>
canvas {
  border: 1px solid #eee;
}
</style>