<template>
  <div class="main">
    <h1 class="text-center">Search BAN checker</h1>
    <v-card class="main-card">
      <SearchForm />
    </v-card>
  </div>
</template>

<script>
import SearchForm from '../search/search-form'

export default {
  name: 'MainPage',
  components: {
    SearchForm,
  },
  data: () => ({
    text: 'SearchBAN checker'
  }),
}
</script>

<style>
.main-card {
  margin: 3rem;
  padding: 3rem;
}
</style>