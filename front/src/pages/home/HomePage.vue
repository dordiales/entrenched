<template>

    <h1>ENTRENCHED</h1>

    <p>Crea una partida o únete a una ya existente</p>
    <input type="text" v-model="gameName">

</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      info: {},
      gameName:""
    }
  },
  mounted() {
  },
  methods: {
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}
</style>
