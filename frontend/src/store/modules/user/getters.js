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
    }
}