<template>
  <v-simple-table>
    <thead>
      <tr>
        <th class="text-center">
          Item
        </th>
        <th class="text-center">
          Result
        </th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Twitter ID</td>
        <td class="text-center">{{ result.user_name }}</td>
      </tr>
      <tr>
        <td>Exist</td>
        <td class="text-center">{{ result.exist }}</td>
      </tr>
      <tr>
        <td>Search BAN</td>
        <td class="text-center">{{ result.search_ban }}</td>
      </tr>
      <tr>
        <td>24h Tweet</td>
        <td class="text-center">{{ result.tweet_count }}</td>
      </tr>
      <tr>
        <td>in Retweet</td>
        <td class="text-center">{{ result.retweet_count }}</td>
      </tr>
    </tbody>
  </v-simple-table>
</template>

<script>
export default {
  name: "Result",
  props: ['result'],
  data: () => ({
  })
}
</script>

<style>

</style>