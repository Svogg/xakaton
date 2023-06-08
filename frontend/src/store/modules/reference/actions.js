import axios from "axios";

export default {
    async loadCities({commit}) {
        const result = await axios.get(process.env.VUE_APP_BASE + '/entity/city')
        commit("setCities", result.data)
    },
    async loadAirlines({commit}) {
        const result = await axios.get(process.env.VUE_APP_BASE + '/entity/airlines')
        commit("setAirlines", result.data)
    }
}