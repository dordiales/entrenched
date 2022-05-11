<template>

    <h1>ENTRENCHED</h1>
    <section class="game-input">
    <p>Crea una partida o únete a una ya existente</p>
    <input type="text" v-model="gameName">
    <button @click="onClickMoveToGame">Ir a la Partida</button>
    </section>
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
    onClickMoveToGame(){
      this.$router.push(`/game/${this.gameName}`)
    }
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}

.game-input{
  margin: 0 auto;
  padding: 2em;
  border: 2px solid black;
  width: fit-content;
  display: grid;
  grid-template-columns: 1fr;
}
.game-input button {
  max-width: fit-content;
  align-self: center;
  margin: auto;
  margin-top: 1em;
}
</style>
