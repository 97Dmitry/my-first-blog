const dateMixin = {
    methods: {
      parseDate(date) {
          if (String(new Date(date).getDay()).length < 2) {
              return '0' + new Date(date).getDay() + '.' +
                  String(new Date(date).getMonth()) + 1 + '.' +
                  String(new Date(date).getFullYear())
          } else return new Date(date).getDay() + '.' +
              String(new Date(date).getMonth()) + 1 + '.' +
              String(new Date(date).getFullYear())
      }
    }
}

const app = Vue.createApp({
  mixins: [dateMixin]
})
app.mixin(dateMixin)