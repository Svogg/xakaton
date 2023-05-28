<template>
  <v-menu
      ref="menu"
      v-model="menu"
      :close-on-content-click="false"
      transition="scale-transition"
      offset-y
      min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <div
          class="passengers-counter"
          v-bind="attrs"
          v-on="on"
      >
        <v-icon v-text="icon"/>
        {{ count }}
      </div>
    </template>
    <v-list
        two-line
        subheader
        class="passengers-counter-menu"
    >
      <v-subheader>Количество гостей</v-subheader>

      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>Взрослые</v-list-item-title>
          <v-list-item-subtitle>cтарше 12 лет</v-list-item-subtitle>
        </v-list-item-content>
        <CountField
          v-model="adult"
          :min="1"
          :max="10"
        />
      </v-list-item>

      <v-list-item>
        <v-list-item-content>
          <v-list-item-title>Дети</v-list-item-title>
          <v-list-item-subtitle>от 2 до 12 лет</v-list-item-subtitle>
        </v-list-item-content>
        <CountField
          v-model="children"
          :min="0"
          :max="10"
        />
      </v-list-item>
    </v-list>
  </v-menu>
</template>

<script>
import CountField from "@/components/ui/CountField.vue";

export default {
  name: "PassengersCounter",
  components:{
    CountField
  },
  data() {
    return {
      menu: false,
      icons: {
        'add': 'mdi-account-plus',
        'one': 'mdi-account',
        'multi': 'mdi-account-multiple'
      },
      adult: 1,
      children: 0
    }
  },
  computed: {
    count() {
      return this.adult + this.children
    },
    icon() {
      if (!this.count) {
        return this.icons["add"]
      }
      if (this.count === 1) {
        return this.icons["one"]
      }
      return this.icons["multi"]
    }
  }
}
</script>

<style scoped lang="scss">
.passengers-counter {

  &:hover {
    font-weight: 500;
  }
}
</style>