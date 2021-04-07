import store from "@/store";
import ru from "@/localization/ru.json";
import en from "@/localization/en.json";

const locales = {
  "ru-RU": ru,
  "en-US": en,
};

export default {
  install: (app) => {
    app.config.globalProperties.$localizeFilter = function (key) {
      const locale = store.getters.info.locale || "ru-RU";
      return locales[locale][key] || `[Localize error]: key ${key} not found`;
    };
  },
};
