export default {
    user: {
        login: 'pavel',
        name: 'Павел Б.',
        citi: 'Абакан'
    },
    choice: {
        category: {
            'hotel' : {id: 1, title: "Отели", icon: "mdi-bed", active: false,
                oid: '642fe4c73145a2c4ce7357da',
                rating: 3, price: [0,10000]},
            'restaurant': {id: 2, title: "Рестораны", icon: "mdi-food-fork-drink", active: false,
                oid: '641c1974496364042d0ab33e',
                price: [0,10000], kitchenType: []},
            'event': {id: 3, title: "Мероприятия", icon: "mdi-balloon", active: false,
                oid: '642fe4c73145a2c4ce7357da',
            },
            'travel': {id: 4, title: "Экскурсии", icon: "mdi-shoe-print", active: false,
                oid: '60ca1a5a1a4b0700192fcb02',
            },
            'avia': {id: 5, title: "Авиабилеты", icon: "mdi-airplane", active: false,
                oid: '',
                airline: null, price: [0,30000]}
        }
    }
};