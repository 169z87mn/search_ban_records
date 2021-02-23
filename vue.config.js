module.exports = {
  transpileDependencies: [
    'vuetify'
  ],
  devServer: {
    proxy: {
      "/stg/": {
        target: process.env.VUE_APP_API_GATEWAY_URL
      }
    }
  }
}
