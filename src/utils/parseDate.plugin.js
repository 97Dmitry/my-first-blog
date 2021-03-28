function Minutes(time) {
  if (time < 10) {
    return time + '0'
  } else {
    return time
  }
}

function Hours(time) {
  if (time < 10) {
    return '0' + time
  } else {
    return time
  }
}

export default {
  install: (app) => {
    app.config.globalProperties.$parseDate = function (date) {
      let newDate = Date.parse(date)
      newDate = new Date(newDate).getDate() + ',' +
        new Date(newDate).getMonth() + 1 + ',' +
        new Date(newDate).getFullYear() + ' ' +
        Hours(new Date(newDate).getHours()) + ':' +
        Minutes(new Date(newDate).getMinutes())
      return newDate
    }
  }
}
