<template>
  <div>
    <v-card>
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
    //
  }),
}
</script>

<style>

</style>