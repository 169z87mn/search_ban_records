<template>
  <v-app class="main">
    <v-main>
        <MainPage />
    </v-main>
  </v-app>
</template>

<script>
import MainPage from './components/pages/main-page'

export default {
  name: 'App',
  components: {
    MainPage,
  },
  data: () => ({
    //
  }),
};
</script>

<style>
.main {
  min-width: 460px;
}
</style>