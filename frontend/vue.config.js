const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave:false,
  devServer: {
    port: 8080,
    liveReload: true,    
    host: "0.0.0.0",
    allowedHosts: "all",
    open: true,
    webSocketServer: false,
    // client: {
    //   overlay: true,
    //   webSocketURL: {
    //     hostname: "0.0.0.0",
    //     pathname: "/ws",
    //     port: 443,
    //     protocol: "ws",
    //   }
    // },
    compress: true,
  },
})