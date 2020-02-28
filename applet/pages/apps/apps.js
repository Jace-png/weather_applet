const app=getApp()
Page({
    data: {
        grids: [0,1]
    },
  onLoad: function (options) {
    this.updateMenuData()
  },

  updateMenuData: function () {
    //定义变量接收值
    var appinfo = this
    wx.request({
      url: app.globalData.appurl+app.globalData.apptype+app.globalData.appname,
      success: function (res) {
        console.log('请求成功')
        console.log(res.data)
        console.log(res)
        appinfo.setData({ grids: res.data.publish})
      },
      fail:function(res){
        console.log('请求失败'+res.errMsg)
      }
    })
  },
  pageskip:function(e){
     console.log(e)
     var index = e.currentTarget.dataset.index
    //  wx.showToast({
    //    title: index+'',
    //  })
     var item = this.data.grids[index]
     console.log(item)
     if (item.app.name == "支付宝"){
       wx.navigateTo({
         url: '/pages/zfb/zfb',
       })
     }else if (item.app.name == '微信'){
       wx.navigateTo({
         url: '/pages/wx/wx',
       })
     }else if (item.app.name == 'QQ'){
       wx.switchTab({
         url: '/pages/index/index',
       })
     }else if (item.app.name =="每日一笑"){
       wx.navigateTo({
         url: '/pages/jokes/jokes',
       })
     }
  },
});
