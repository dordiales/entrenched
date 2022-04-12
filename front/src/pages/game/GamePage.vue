<template>
    <section class="game-board">
        <article  v-for="square in squares" class="square" v-bind:class="square.player" :key="square.square" @click="onSquareClicked(square)">
          {{square.soldier}}
        </article>
    </section>
    <p>Movimiento:{{movement}} Ganador: {{winner}}</p>
    

</template>

<script>
import {getGameState, putGameMovement} from '@/services/api.js';

export default {
    data() {
    return {
      player: "player_1",
      squares: [],
      movement: {from:"", to:""},
      winner: ""
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.squares = await getGameState()
      const hqList = this.squares.filter(e=>e.soldier == "hq")
         
        if (hqList.length !== 2) {
          let winner_player = hqList.pop().player
          this.winner = winner_player
        }
    },
    async sendMovement() {
      await putGameMovement(this.movement)

    }, 
    async onSquareClicked(square){
      if (square.soldier !==null && square.player === this.player){
        this.movement.from = square.square}
      if (this.movement.from !=="" && this.movement.from !== square.square){
        this.movement.to = square.square
      }
      if (this.movement.from !=="" && this.movement.to !==""){
        this.sendMovement().then(async(result) => {
          this.movement = {from:"", to:""}
          this.loadData()
        
          return result
        })

      }
    }
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