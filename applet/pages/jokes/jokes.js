// pages/jokes/jokes.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    jokes:[]

  },


  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var info = this
    //获取当前时间戳
    // var timestamp = Date.parse(new Date()) / 1000; 
    wx.request({
      url: 'http://127.0.0.1:8000/api/v1.0/juhe/TIS',
      method: "GET",
      header: {},
      success: function (res) {
        console.log('请求成功' + res.data.result.data)
        info.setData({ jokes: res.data.result.data })
      },
      faol: function (res) {
        console.log('请求失败:' + res.errMsg)
      },
    })

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})