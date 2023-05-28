export default {
    authRequest(state) {
        state.status = 'loading'
    },
    authSuccess(state, data) {
        state.status = 'success'
        state.token = data.token || null
        state.user = {...data.user, citi: null}
    },
    authError(state) {
        state.status = 'error'
    },
    logout(state) {
        state.status = ''
        state.token = ''
        state.user = {}
    },
    setUserCiti: (state, citi) => {
        state.user.citi = citi
    },
}