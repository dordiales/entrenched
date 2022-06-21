<template>

    <div class="portrait-align">
    <h1>ENTRENCHED</h1>
    <section class="game-input">
      <h3>Crea una partida o únete a una ya existente</h3>
      <input type="text" v-model="gameName" @keyup.enter="onClickMoveToGame">
      <button class="button-green" @click="onClickMoveToGame">Ir a la Partida</button>
    </section>

    <router-link class="info" to="/info">+Info</router-link>

    <footer>
      <p>Art made by cheese.sketch</p>
      <p>Instagram</p>
      <a href="https://www.instagram.com/cheese.sketch/">@cheese.sketch</a>
    </footer>
    </div>
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
  font-size: 6em;
}
footer {
  margin-top: 2em;
}
footer p{
  margin: 0.2em;
  justify-content: center;
}

.info {
  display: block;
  margin: auto;
  margin-top: 1em;
  width: fit-content;
}

.game-input{
  color: whitesmoke;
  margin: 0 auto;
  padding: 2em;
  border: 4px inset #3e4e22;
  width: fit-content;
  display: grid;
  grid-template-columns: 1fr;
  box-shadow: 0px 6px 0px #58732a;
  background-color: #58732a;
}
.game-input button {
  max-width: fit-content;
  align-self: center;
  margin: auto;
  margin-top: 1em;
}
.game-input input {
  box-shadow: 1px 1px 5px #585858 ;
}

@media only screen and (orientation:landscape) and (max-width:961px){
  h1 {
    font-size: 4em;
    margin: 0 auto 0.5%;
  }

  footer {
  margin-top: 1em;
  display: flex;
  justify-content: center;
}
.game-input{
  color: whitesmoke;
  margin: 0 auto;
  padding: 2em;
  border: 4px inset #3e4e22;
  width: fit-content;
  display: grid;
  grid-template-columns: 1fr;
  box-shadow: 0px 6px 0px #58732a;
  background-color: #58732a;
}
}

@media only screen and (orientation:portrait) and (max-width:450px){

  h1 {
    font-size: 4em;
    margin: 0 auto 0.5%;
  }

  footer {
  margin-top: 1em;
  display: flex;
  justify-content: center;
}

.portrait-align{
  position: fixed;
  left: 45%;

}
.game-input {
  width: 50vh;
}
}


</style>
