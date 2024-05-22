<template>
  <h1 class="text-xl font-bold text-white my-4">プライバシーポリシー</h1>
  <el-card class="m-4" shadow="never">
    <template #header>
      <div class="card-header">
        <span class="text-xl">個人情報保護方針</span>
      </div>
    </template>
    <p class="text item">謎解きデータベースの管理人(以下「管理人」といいます。)は，謎解きデータベース上で提供するサービス(以下「本サービス」といいます。)における利用者の個人情報の取り扱いについて，以下の通りにプライバシーポリシー(以下「本ポリシー」といいます。)を定め，個人情報の保護に努めます。
      本ポリシーは利用規約に含まれるものとして位置づけられており，利用者が本サービスを利用するときに適用されます。</p>
  </el-card>
  <el-card class="m-4">
    <template #header>
      <div class="card-header" shadow="never">
        <span class="text-xl">個人情報の利用目的</span>
      </div>
    </template>
    <p class="text item">管理人が個人情報を収集・利用する目的は，以下の通りです。</p>
    <ul>
      <li>（１）本サービスの提供・運営のため</li>
      <li>（２）本人確認を行うため</li>
      <li>（３）利用者にご自身の登録情報の閲覧や変更，削除を行っていただくため</li>
      <li>（４）利用者からのお問い合わせに回答するため</li>
      <li>（５）上記の利用目的に付随する目的</li>
    </ul>
  </el-card>
  <el-card class="m-4">
    <template #header>
      <div class="card-header" shadow="never">
        <span class="text-xl">アクセス解析</span>
      </div>
    </template>
    <p class="text item">管理人は，本サービスにおいてGoogleアナリティクスを利用しています。
      トラフィックデータは匿名で収集されており，個人を特定するものではありません。
      Googleアナリティクスはトラフィックデータの収集のためにCookieを使用しています。
      詳細は<a href="https://policies.google.com/technologies/partner-sites?hl=ja" class="text-blue-400 hover:text-blue-500">「Googleのサービスを使用するサイトやアプリから収集した情報のGoogleによる使用」のページ</a>で確認できます。</p>
  </el-card>
  <el-card class="m-4">
    <template #header>
      <div class="card-header" shadow="never">
        <span class="text-xl">個人情報の安全管理</span>
      </div>
    </template>
    <p class="text item">管理人は，個人情報への不正アクセス・漏洩・紛失・破損・改ざんなどを防止するため，セキュリティシステムの維持・管理を徹底します。</p>
  </el-card>
  <el-card class="m-4">
    <template #header>
      <div class="card-header" shadow="never">
        <span class="text-xl">個人情報の第三者への開示</span>
      </div>
    </template>
    <p class="text item">管理人は，以下のいずれかに該当する場合を除き，第三者に対して個人情報を開示・提供することはしません。</p>
    <ul>
      <li>（１）本人の承諾がある場合</li>
      <li>（２）個人を識別することができない状態で統計的なデータとして開示・提供する場合</li>
      <li>（３）官公庁などの公的機関から法令に基づいて開示を求められた場合</li>
      <li>（４）人の生命，身体または財産の保護のために必要な場合</li>
    </ul>
  </el-card>
  <el-card class="m-4">
    <template #header>
      <div class="card-header" shadow="never">
        <span class="text-xl">プライバシーポリシーの変更</span>
      </div>
    </template>
    <p class="text item">管理人は，日本の法令や規範を遵守するとともに，必要に応じて本ポリシーの内容を見直して変更できるものとします。
      本ポリシーの変更については，本サービス内で告知する方法で利用者に通知します。
      変更後の本ポリシーは，本ウェブサイトに掲載したときから効力を生じるものとします。</p>
  </el-card>
</template>
<script setup>
  useSeoMeta({
    title: 'プライバシーポリシー | 謎解きデータベース',
    ogTitle: 'プライバシーポリシー | 謎解きデータベース',
  });
</script>