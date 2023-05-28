import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import ru from "vuetify/es5/locale/ru";

Vue.use(Vuetify);
export default new Vuetify({
  lang:{
    locales: {ru},
    current: 'ru'
  },
    icons: {
      iconfont: 'mdiSvg', // 'mdi' || 'mdiSvg' || 'md' || 'fa' || 'fa4' || 'faSvg'
    },
    theme: {
      options: { customProperties: true },
      themes: {
        light: {
          primary: '#FFCF08',
          secondary: '#007470',
          error: '#DF2A00',
          warning: '#E76D00',
          success: '#007470',
          background: '#FAEFDB',
          backgroundDefault: '#FFFBF3'
        },
        dark: {
          primary: '#FFC90A',
          secondary: '#009E54',
          error: '#DF2A00',
          warning: '#E76D00',
          success: '#007470',
          background: '#191919',
        },
      },
  },
});
