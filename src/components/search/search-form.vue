<template>
  <div>
    <v-text-field
        label="user_name"
        v-model="user_name"
        prefix="@"
        @keyup.enter="search"
      >
      <template v-slot:append-outer>
        <v-btn color="primary" v-bind:disabled="isProcessing" v-on:click="search">Search</v-btn>
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
    user_name: "",
    resultModel: false,
    result: null,
    isProcessing: false,
  }),
  methods: {
    search () {
      console.log("search")
      this.isProcessing = true
      this.resultModel = false

      let data = {
        "withCredentials": true,
        "user_name": this.user_name,
      }
      axios.get("https://yxm7lbxscl.execute-api.ap-northeast-1.amazonaws.com/stg/" + this.user_name, data).then((result) => {
        this.result = result.data
        this.resultModel = true
        this.isProcessing = false
      }).catch((err) => {
        console.log(err)
      });
    }
  }
}
</script>

<style>
</style>