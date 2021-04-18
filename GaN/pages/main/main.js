// pages/main.js
const util = require('../../utils/util.js')
Page({

  /**
   * 页面的初始数据
   */
  data: {
    userName: null,
    userId: null,
    dept: null,
    score: null,
    rsvData: null
  },

  scanQR() {
    wx.scanCode({
      onlyFromCamera: false,
      scanType: ['qrCode'],
      success(res) {
        console.log(res.result)
        wx.request({
          url: `http://libic.njfu.edu.cn/ClientWeb/pro/ajax/device.aspx?date=${util.YYYYMMDD(new Date)}&dev_id=${res.result.match(/(?<=Seat_)\d+/)}&act=get_rsv_sta`,
          success(res) {
            console.log(res.data.data[0].title)
          },
          fail(res) {
            console.log(res)
          }
        })
      },
      fail: (res) => {
        console.log(res)
      }
    })
    wx.request({
      url: res.result,
      header: {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Cookie': wx.getStorageSync("sessionid")
      },
      success(res) {
        console.log(res)
      }
    })
  },

  fetchRsv() {
    let that = this;
    wx.request({
      url: 'http://libic.njfu.edu.cn/ClientWeb/pro/ajax/reserve.aspx?stat_flag=9&act=get_my_resv',
      header: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': wx.getStorageSync("sessionid")
      },
      success(res) {
        // console.log(res)
        that.setData({
          rsvData: res.data.data
        })
      }
    })
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    let that = this;
    wx.request({
      url: 'http://libic.njfu.edu.cn/ClientWeb/pro/ajax/login.aspx',
      method: "POST",
      data: {
        'id': '',
        'pwd': '',
        'act': 'login'
      },
      header: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
      },
      success(res) {
        // console.log(res)
        wx.removeStorageSync('sessionid')
        wx.setStorageSync("sessionid", res.header["Set-Cookie"])
        that.setData({
          userName: res.data.data.name,
          userId: res.data.data.id,
          dept: res.data.data.dept,
          score: res.data.data.score
        })
        that.fetchRsv()
      }
    })
    wx.stopPullDownRefresh()
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
    var that = this
    that.setData({
      userName: null,
      userId: null,
      dept: null,
      score: null,
      rsvData: null
    })
    this.onLoad()
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