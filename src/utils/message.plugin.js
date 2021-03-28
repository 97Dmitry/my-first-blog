export default {
    install: (app) => {
        app.config.globalProperties.$message = function (text) {
            M.toast({html: text, classes: 'rounded'})
        }

        app.config.globalProperties.$error = function (text) {
            M.toast({html: `[Ошибка]: ${text}`})
        }
    }
}