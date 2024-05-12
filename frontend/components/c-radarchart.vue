<template>
  <!-- 定義したdataとoptionsを渡してあげます。 -->
  <Radar :data="data" :options="options"/>
</template>
<script setup lang="ts">
interface Props {
  riddle: object
}
const props = defineProps<Props>()
// @types/chart.jsの型付けを使用するためにimportしてます。
import type { ChartData, ChartOptions } from 'chart.js';

// それぞれの部品をインポートしていきます。
// まだ種類があると思いますが、とりあえず手当たり次第importしておきます。
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
  PointElement,
  RadialLinearScale,
  Filler,
  LineElement
} from 'chart.js'

// 今回はRadar-chartを作成するので、import。
// 他にも{ Bar }など、種類があります。
import { Radar } from 'vue-chartjs'

// ここでChartJSでこれらを使います〜と登録してあげます。
ChartJS.register(CategoryScale, LinearScale, BarElement,PointElement ,RadialLinearScale, LineElement, Filler, Title, Tooltip, Legend)

// ここではchartに使うdataを登録していきます。
// ChartData<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const data:ChartData<'radar'> = {
  labels: [
    'ストーリー性',
    'ギミック',
    'スッキリ感',
    '難易度',
  ],
  datasets: [
    {
      label: '評価',
      backgroundColor: 'rgba(247, 186, 41, 0.2)',
      borderColor: '#F7BA29',
      pointBackgroundColor: '#F7BA29',
      pointBorderColor: '#F7BA29',
      pointHoverBackgroundColor: '#ffa503',
      pointHoverBorderColor: '#ffa503',
      data: [props.riddle.rating_story, props.riddle.rating_gimmick, props.riddle.rating_sukkiri, props.riddle.rating_level]
    }
  ]
};

// ここではchartに使うoptionsを登録していきます。
// ChartOptions<'radar'>でRadar-Chartの型付けを使ってます。
// 他にも<"bar">などがあります。
const options:ChartOptions<'radar'> = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    r: {
      backgroundColor: "",
      pointLabels: {
        font: {
          size: 14
        },
        color: "rgb(209, 213, 219)"
      },
      angleLines: {
        color: "rgb(209, 213, 219)"
      },
      grid: {
        color: "rgb(209, 213, 219)"
      },
      ticks: {
        color: "rgb(209, 213, 219)",
        backdropColor: "#111827"
      },
      max: 5,
      min: 0,
    },
  },
  plugins: {
    legend: {
      display: false
    }
  }
};
</script>