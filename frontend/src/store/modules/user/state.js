export default {
    user: {
        login: 'pavel',
        name: 'Павел Б.',
        citi: 'Абакан'
    },
    choice: {
        category: {
            'hotel' : {id: 1, title: "Отели", icon: "mdi-bed", active: false,
                rating: 3, price: [0,10000]},
            'restaurant': {id: 2, title: "Рестораны", icon: "mdi-food-fork-drink", active: false,
                price: [0,10000], kitchenType: []},
            'museum': {id: 3, title: "Мероприятия", icon: "mdi-balloon", active: false},
            'travel': {id: 4, title: "Экскурсии", icon: "mdi-shoe-print", active: false},
            'avia': {id: 5, title: "Авиабилеты", icon: "mdi-airplane", active: false,
                airline: null, price: [0,30000]}
        },
        from: null,
        to: null,
        period: null,
        passengers: null
    }
};