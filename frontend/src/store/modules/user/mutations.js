export default {
    setUserInfo: (state, data) => {
        state.user = data
    },
    setUserCiti: (state, citi) => {
        state.user.citi = citi
    },
    toggleChoiceCategoryActive(state, key){
        const category = state.choice.category[key]
        category.active = !category.active
    },
    setChoiceCategoryHotelRating(state, value){
        state.choice.category['hotel'].rating = value
    },
    setChoiceCategoryHotelPrice(state, value){
        state.choice.category['hotel'].price = value
    },
    setChoiceCategoryRestaurantPrice(state, value){
        state.choice.category['restaurant'].price = value
    },
    setChoiceCategoryRestaurantKitchenType(state, value){
        state.choice.category['restaurant'].kitchenType = value
    },
    setChoiceCategoryAviaPrice(state, value){
        state.choice.category['avia'].price = value
    },
    setChoiceCategoryAviaAirline(state, value){
        state.choice.category['avia'].airline = value
    }
}