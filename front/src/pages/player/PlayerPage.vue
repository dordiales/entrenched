<template>
    <section class="game-board">
        <article  v-for="square in squares" class="square" v-bind:class="square.player" :key="square.square" @click="onSquareClicked(square)">
          {{square.soldier}}
        </article>
    </section>

    <button @click="loadData">Refrescar estado</button>

    <h3>Debug</h3>
    <p>Jugador: {{activePlayer}} Movimiento:{{movement}} Ganador: {{winner}}</p>
    
    <WinnerModal v-show="modalOpened" :winner="winner"/>

</template>

<script>
import {getGameState, putGameMovement, getPlayerTurn} from '@/services/api.js';
import WinnerModal from '@/components/WinnerModal.vue';

export default {
    components: {WinnerModal},
    data() {
    return {
      activePlayer: "player_1",
      user: this.$route.params.playerId,
      player: "",
      squares: [],
      movement: {from:"", to:""},
      winner: "",
      modalOpened: false,
      gameId: this.$route.params.gameId
    };
  },
  mounted() {
    this.loadData();
  },
  computed:{
      
  },
  methods: {
    async loadData() {
      this.squares = await getGameState(this.gameId)
      this.activePlayer = await getPlayerTurn(this.gameId)


      const hqList = this.squares.filter(e=>e.soldier == "hq")
         
        if (hqList.length !== 2) {
          let winner_player = hqList.pop().player
          this.winner = winner_player
          this.openWinnerModal()
        }
    },
    async sendMovement() {
      
      await putGameMovement(this.movement, this.gameId)

    }, 
    isValidMovement(){
          if (this.movement.from !=="" && this.movement.to !==""){
              return true
          } else {
              return false
          }
      },
    async onSquareClicked(square){
      if (square.soldier !==null && square.player === this.activePlayer){
        this.movement.from = square.square}
      if (this.movement.from !=="" && this.movement.from !== square.square){
        this.movement.to = square.square
      }
      if (this.isValidMovement()){
        this.sendMovement().then(async(result) => {
          this.movement = {from:"", to:""}
          this.loadData()
        
          return result
        })
      }
    },
    openWinnerModal() {
      this.modalOpened = true;
      console.log("click modal" + this.modalOpened);
    },
    closeWinnerModal() {
      this.modalOpened = false;
    },
  },
}
</script>

<style>
    .game-board {
        display: grid;
        grid-template-rows: 5em 5em 5em 5em 5em;
        grid-template-columns: 5em 5em 5em 5em 5em 5em 5em 5em 5em;
        margin: 5em
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