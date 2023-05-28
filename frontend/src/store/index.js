import Vue from "vue";
import Vuex from "vuex";
import state from './state.js'
import actions from './actions.js'
import mutations from './mutations.js'
import getters from './getters.js'
import user from './modules/user/index.js'
import reference from './modules/reference/index.js'
import auth from './modules/auth/index.js'

Vue.use(Vuex);

const store = new Vuex.Store({
    state,
    mutations,
    actions,
    getters,
    modules: {
        user,
        reference,
        auth
    },
});

export default store