<template>
  <v-menu
      ref="menu"
      v-model="menu"
      :close-on-content-click="false"
      :return-value.sync="dates"
      transition="scale-transition"
      offset-y
      min-width="auto"
  >
    <template v-slot:activator="{ on, attrs }">
      <v-text-field
          v-model="dateRangeText"
          label="ПЕРИОД"
          prepend-inner-icon="mdi-calendar"
          v-bind="attrs"
          v-on="on"
          dense
          readonly
          hide-details
          clearable
      ></v-text-field>
    </template>
    <v-date-picker
        v-model="dates"
        range
        no-title
        scrollable
    >
      <v-spacer></v-spacer>
      <v-btn
          text
          color="primary"
          @click="menu = false"
      >
        Отмена
      </v-btn>
      <v-btn
          text
          color="primary"
          @click="$refs.menu.save(dates)"
      >
        ОК
      </v-btn>
    </v-date-picker>
  </v-menu>
</template>

<script>
export default {
  name: "DatePicker",
  data: () => ({
    dates: [],
    menu: false,
  }),
  computed: {
    dateRangeText() {
      if(!this.dates?.length) return null
      const dt1 = this.dates[0].substr(5)
      const dt2 = this.dates[1] ? ` ~ ${this.dates[1].substr(5)}` : ''
      return dt1  + dt2
    },
  },
}
</script>

<style scoped>

</style>