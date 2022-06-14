<template>
    <section class="game-board">
        <article  v-for="square in squares" class="square" v-bind:class="square.player" :key="square.square" @click="onSquareClicked(square)">
          <img :src="getSoldierIcon(square)" :alt="square.player + '-' + square.soldier" v-if="square.soldier !=undefined">
        </article>
    </section>

    <section class="control-panel">
      <ul >
        <li :class="player">Comandando a los soldados {{selectedTeam}}</li>
        <li>Es el turno del comandante {{commanderTrun}}</li>
        <li><button class="button-green">Abandonar partida</button></li>
      </ul>
    </section>

    <WinnerModal v-show="modalOpened" :winner="winner"/>

</template>

<script>
import {getGameState, putGameMovement, getGameSquares} from '@/services/api.js';
import WinnerModal from '@/components/WinnerModal.vue';

export default {
    components: {WinnerModal},
    data() {
    return {
      activePlayer: "player_1",
      user: this.$route.params.playerId,
      player: this.$route.params.playerId,
      squares: [],
      movement: {from:"", to:""},
      winner: "",
      modalOpened: false,
      gameId: this.$route.params.gameId
    };
  },
  mounted() {
    this.loadData();
    this.refreshData();
  },
  computed:{
    selectedTeam (){
      if (this.player === "player_1"){
        return "ingleses"
      } else {
        return "alemanes"
      }
    },
    commanderTrun (){
      if (this.activePlayer === "player_1"){
        return "inglés"
      } else {
        return "alemán"
      } 
    },
      
  },
  methods: {
    async loadData() {
      this.squares = await getGameSquares(this.gameId)
  
      let gameState = await getGameState(this.gameId)

      this.activePlayer = gameState.active_player


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
      if (square.soldier !==null && square.player === this.activePlayer && square.player === this.player){
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
    getSoldierIcon(square){
      const iconsRoute = 'https://i.imgur.com/'
      const iconRouter = {'player_1':{trooper:'8WtYp5E.png',
                             grenadier:'64Vdf7N.png', 
                             machinegun: 'SROxcoG.png', 
                             hq: 'gKYRMFk.png'
                            },
                   'player_2':{trooper:'sgBDzUb.png',
                             grenadier:'guKaS99.png', 
                             machinegun: 'ECbNeFH.png', 
                             hq: 'nzf6NaJ.png'
                            }
                  }
      const iconPlayer = square.player
      const iconSoldier = square.soldier
      const soldierIconRoute = iconsRoute + iconRouter[iconPlayer][iconSoldier]
      return soldierIconRoute
      
    }
  },
}
</script>

<style scoped>
  .game-board {
      display: grid;
      grid-template-rows: 5em 5em 5em 5em 5em;
      grid-template-columns: 5em 5em 5em 5em 5em 5em 5em 5em 5em;
      margin: 5em auto;
      justify-content: center;
      border: 3px solid rgb(153, 58, 35);
      width: fit-content;
  }
  .square {
    border: 1px dashed rgb(153, 58, 35);
    background-color: beige;

  }
  .square img {
    height: 100%;
    width: 100%;
    object-fit: contain;
  }
  .control-panel{
    font-size: 1.5rem;
    font-weight: bolder;
    border: 4px inset #3e4e22;
    display: grid;
    grid-template-columns: 1fr;
    box-shadow: 0px 6px 0px #58732a;
    background-color: #58732a;
    margin: 0 auto;
    width: 60vw;
  }
  .control-panel ul {
    list-style: none;
    margin: 1em 0;
    padding: 0;

  }
  .control-panel ul .player_2 {
    color: #5a6db1;
  }
  .control-panel ul .player_1 {
    color: #b37c34;
  }
  .control-panel ul li{
    margin: 1em 0;
    color: whitesmoke;
  }
</style>