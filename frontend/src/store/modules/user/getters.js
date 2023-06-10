export default {
    getChoiceCategories: state => {
        return state.choice.category
    },
    getChoice: state => {
        return state.choice
    },
    getChoiceCategory: (state) => {
        return (code) =>{
            return state.choice.category[code]
        }
    },
    getActiveChoice:(state) => {
        return Object.keys(state.choice.category)
          .filter(key => state.choice.category[key].active)
          .reduce((obj, key) => {
            obj.push(key)
            return obj
          }, [])
    }
}