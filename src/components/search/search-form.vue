<template>
  <div>
    <v-text-field
        label="user_name"
        v-model="user_name"
        prefix="@"
      >
      <template v-slot:append-outer>
        <v-btn color="primary" v-on:click="search">Search</v-btn>
      </template>
    </v-text-field>
    <Result v-model="resultModel" :result="result" />
  </div>
</template>

<script>
import axios from "axios";
import Result from '../result/result'

export default {
  name: "SearchForm",
  components: {
    Result,
  },
  data: () => ({
    "user_name": "",
    "resultModel": false,
    "result": null,
  }),
  methods: {
    search () {
      console.log("search")
      let data = {
        "withCredentials": true,
        "user_name": this.user_name,
      }
      axios.get("https://yxm7lbxscl.execute-api.ap-northeast-1.amazonaws.com/stg/" + this.user_name, data).then((result) => {
        this.result = result.data
        this.resultModel = true
      }).catch((err) => {
        console.log(err)
      });
    }
  }
}
</script>

<style>

</style>