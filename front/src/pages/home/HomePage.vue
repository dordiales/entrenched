<template>

    <h1>ENTRENCHED</h1>
    <section class="game-input">
    <p>Crea una partida o únete a una ya existente</p>
    <input type="text" v-model="gameName">
    <button @click="onClickMoveToGame">Ir a la Partida</button>
    </section>
    <footer>
      <p>Art made by cheese.sketch</p>
      <p>Instagram</p>
      <a href="https://www.instagram.com/cheese.sketch/">@cheese.sketch</a>
    </footer>
</template>

<script>
import {startNewGame} from '@/services/api.js';

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
    async onClickMoveToGame(){
      console.log(this.gameName)
      const response = await startNewGame(this.gameName).then(async() => {
          this.$router.push(`/game/${this.gameName}`)
        })
        
      return response
    }
  }


}
</script>

<style scoped>
h1 {
  font-style: italic;
}

footer p{
  margin: 0.2em;
  justify-content: center;
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
