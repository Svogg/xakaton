import axios from "axios";

export default {
    login({commit}, user) {
        return new Promise((resolve, reject) => {
            commit('authRequest')
            const headers = {
                'Content-Type': 'multipart/form-data'
            }
            axios({url: process.env.VUE_APP_BASE + '/auth/token', data: user, method: 'POST', headers},)
                .then(resp => {
                    const token = resp.data.access_token
                    localStorage.setItem('token', token)
                    axios.defaults.headers.common['Authorization'] = token
                    commit('authSuccess', {token, user})
                    resolve(resp)
                })
                .catch(err => {
                    commit('authError')
                    localStorage.removeItem('token')
                    reject(err)
                })
        })
    },
    register({commit}, user) {
        return new Promise((resolve, reject) => {
            commit('authRequest')
            axios.post(process.env.VUE_APP_BASE + '/registration/register', null, {params: user})
                .then(resp => {
                    localStorage.setItem('token', '')
                    const token = null
                    const user = {}
                    axios.defaults.headers.common['Authorization'] = token
                    commit('authSuccess', {token, user})
                    resolve(resp)
                }).catch(err => {
                commit('authError', err)
                localStorage.removeItem('token')
                reject(err)
            })
        })
    },
    logout({commit}) {
        return new Promise((resolve) => {
            commit('logout')
            localStorage.removeItem('token')
            delete axios.defaults.headers.common['Authorization']
            resolve()
        })
    }
}