<template>
    <section class="game-board">
      <article  v-for="square in squares" class="square" v-bind:class="square.player" :key="square.square">
        {{square.soldier}}
      </article>
    </section>


    <button v-if="player1 === null" @click="joinAsPlayer('player_1')">Unirse como Jugador 1</button>
    <button v-else disabled>Unirse como Jugador 1</button>

    <button v-if="player2 === null" @click="joinAsPlayer('player_2')">Unirse como Jugador 2</button>
    <button v-else disabled>Unirse como Jugador 2</button>

    <button @click="loadData">Refrescar estado</button>

    <p>Player1: {{player1}} Player2: {{player2}}</p>

    <WinnerModal v-show="modalOpened" :winner="winner"/>

    

</template>

<script>
import {getGameSquares, getGameState, joinGame} from '@/services/api.js';
import WinnerModal from '@/components/WinnerModal.vue';

export default {
    components: {WinnerModal},
    data() {
    return {
      activePlayer: "player_1",
      squares: [],
      movement: {from:"", to:""},
      winner: "",
      modalOpened: false,
      gameId: this.$route.params.gameId,
      player1 :null,
      player2 :null,
    };
  },
  mounted() {
    this.loadData();
    this.refreshData();
  },
  methods: {

    async loadData() {
      this.squares = await getGameSquares(this.gameId)
      let gameState = await getGameState(this.gameId)
      this.activePlayer = gameState.active_player
      this.player1 = gameState.player_1
      this.player2 = gameState.player_2
      

      const hqList = this.squares.filter(e=>e.soldier == "hq")
         
        if (hqList.length !== 2) {
          let winner_player = hqList.pop().player
          this.winner = winner_player
          this.openWinnerModal()
        }
    },

    async refreshData() {
      window.setInterval(() => {
       this.loadData()
    }, 5000);
    },
    
    openWinnerModal() {
      this.modalOpened = true;
      console.log("click modal" + this.modalOpened);
    },
    closeWinnerModal() {
      this.modalOpened = false;
    },
    async joinAsPlayer(playerName){
      const response = await joinGame(playerName, this.gameId).then(async() => {
          this.$router.push({name: "Player" ,params:{gameId: this.gameId, playerId: playerName}})
        })
        return response
      
    },
  },
}
</script>

<style>

    button {
      margin: 1em
    }
    .game-board {
        display: grid;
        grid-template-rows: 5em 5em 5em 5em 5em;
        grid-template-columns: 5em 5em 5em 5em 5em 5em 5em 5em 5em;
        margin: 5em;
        justify-content: center;
    }
    .square {
      border: 1px solid black;
      background-color: beige;

    }
    .player_1 {
      color: #5a6db1;
    }
    .player_2 {
      color: #b37c34;
    }
</style>