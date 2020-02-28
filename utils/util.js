const formatTime = date => {
  const year = date.getFullYear()
  const month = date.getMonth() + 1
  const day = date.getDate()
  const hour = date.getHours()
  const minute = date.getMinutes()
  const second = date.getSeconds()

  return [year, month, day].map(formatNumber).join('/') + ' ' + [hour, minute, second].map(formatNumber).join(':')
}

const formatNumber = n => {
  n = n.toString()
  return n[1] ? n : '0' + n
}

//定义一个变量 方便下面函数的调用
const keys ='cookie'
//获取相应session
function getSessionIDFromResponse(res){
  var cookie = res.header['Set-Cookie']
  console.log('getSessionIDFromResponse:' + cookie)
  return cookie
}


//保存为键值对
function setCookieToStorage(cookie){
  try{
    wx.setStorageSync(keys, cookie)
  }catch(e){
    console.log(e)
  }
}

function getCookieFromStorage(){
  var value = wx.getStorageSync(keys)
  return value
}
module.exports = {
  formatTime: formatTime,
  getSessionIDFromResponse: getSessionIDFromResponse,
  setCookieToStorage: setCookieToStorage,
  getCookieFromStorage: getCookieFromStorage

}
