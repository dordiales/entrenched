<template>
    <section class="game-board" v-if="player === 'player_2'">
        <article  v-for="square in squares" class="square" :class="square.player" :style="isAdyacent(square)" :key="square.square" @click="onSquareClicked(square)">
          <img :src="getSoldierIcon(square)" :alt="square.player + '-' + square.soldier" v-if="square.soldier !=undefined">
        </article>
    </section>
    <section class="game-board" v-else>
        <article  v-for="square in squares.slice().reverse()" class="square" :class="square.player" :style="isAdyacent(square)" :key="square.square" @click="onSquareClicked(square)">
          <img :src="getSoldierIcon(square)" :alt="square.player + '-' + square.soldier" v-if="square.soldier !=undefined">
        </article>
    </section>

    <section class="control-panel">
      <ul >
        <li :class="player">Comandando a los soldados {{selectedTeam}}</li>
        <li>Es el turno del comandante {{commanderTrun}}</li>
        <li><button class="button-green" @click="openRulesModal">Reglas</button></li>
        <li><button class="button-red" @click="exitGame">Abandonar partida</button></li>
      </ul>
    </section>

    <WinnerModal v-show="modalOpened" :winner="winner" @finish="finishGame"/>
    <RulesModal v-show="rulesOpened" @closeRules="closeRulesModal"/>

</template>

<script>
import {getGameState, putGameMovement, getGameSquares, exitGame} from '@/services/api.js';
import WinnerModal from '@/components/WinnerModal.vue';
import RulesModal from './RulesModal.vue'

export default {
    components: {WinnerModal, RulesModal},
    data() {
    return {
      activePlayer: "player_1",
      user: this.$route.params.playerId,
      player: this.$route.params.playerId,
      squares: [],
      movement: {from:"", to:""},
      winner: "",
      modalOpened: false,
      rulesOpened: false,
      gameId: this.$route.params.gameId,
      adjacentSquaresDict : {
            "A1": ["B1", "A2"],
            "A2": ["A1", "B2", "A3"],
            "A3": ["A2", "B3", "A4"],
            "A4": ["A3", "B4", "A5"],
            "A5": ["A4", "B5", "A6"],
            "A6": ["A5", "B6", "A7"],
            "A7": ["A6", "B7", "A8"],
            "A8": ["A7", "B8", "A9"],
            "A9": ["A8", "B9"],
            "B1": ["C1", "B2", "A1"],
            "B2": ["B1", "C2", "B3", "A2"],
            "B3": ["B2", "C3", "B4", "A3"],
            "B4": ["B3", "C4", "B5", "A4"],
            "B5": ["B4", "C5", "B6", "A5"],
            "B6": ["B5", "C6", "B7", "A6"],
            "B7": ["B6", "C7", "B8", "A7"],
            "B8": ["B7", "C8", "B9", "A8"],
            "B9": ["B8", "C9", "A9"],
            "C1": ["D1", "C2", "B1"],
            "C2": ["C1", "D2", "C3", "B2"],
            "C3": ["C2", "D3", "C4", "B3"],
            "C4": ["C3", "D4", "C5", "B4"],
            "C5": ["C4", "D5", "C6", "B5"],
            "C6": ["C5", "D6", "C7", "B6"],
            "C7": ["C6", "D7", "C8", "B7"],
            "C8": ["C7", "D8", "C9", "B8"],
            "C9": ["C8", "D9", "B9"],
            "D1": ["E1", "D2", "C1"],
            "D2": ["D1", "E2", "D3", "C2"],
            "D3": ["D2", "E3", "D4", "C3"],
            "D4": ["D3", "E4", "D5", "C4"],
            "D5": ["D4", "E5", "D6", "C5"],
            "D6": ["D5", "E6", "D7", "C6"],
            "D7": ["D6", "E7", "D8", "C7"],
            "D8": ["D7", "E8", "D9", "C8"],
            "D9": ["D8", "E9", "C9"],
            "E1": ["E2", "D1"],
            "E2": ["E1", "E3", "D2"],
            "E3": ["E2", "E4", "D3"],
            "E4": ["E3", "E5", "D4"],
            "E5": ["E4", "E6", "D5"],
            "E6": ["E5", "E7", "D6"],
            "E7": ["E6", "E8", "D7"],
            "E8": ["E7", "E9", "D8"],
            "E9": ["E8", "D9"],
        },
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
      const dataRefresh = window.setInterval(() => {
        const onCreationRoute = this.gameId
        if (this.$route.params.gameId != onCreationRoute){
          window.clearInterval(dataRefresh)
        } else {
          this.loadData()
        }
      }, 500);
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
      if (square.soldier == 'hq'){
        return ''
      }
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
    },
    closeWinnerModal() {
      this.modalOpened = false;
    },
    openRulesModal(){
      this.rulesOpened = true;
    },
    closeRulesModal(){
      this.rulesOpened = false;
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
      
    },
    isAdyacent(square){
      if (this.movement.from == ""){
        return {}
      }
      if (square.player == this.player){
        return {}
      }
      let adyacentSquares = this.adjacentSquaresDict[this.movement.from]
      if (adyacentSquares.includes(square.square)){
        if (square.player != this.player && square.player != null){
          return {backgroundColor: 'darkorange'}
        } else {
          return {backgroundColor: 'darkcyan'}
        }
        
      } else {
        return {}
      }
      
    },
    async exitGame(){
      const response = await exitGame(this.player, this.gameId).then(async() => {
          this.$router.push({name: "Game" ,params:{gameId: this.gameId}})
        })
        return response
    },
    async finishGame(){
      const response = await exitGame(this.player, this.gameId).then(async() => {
          this.$router.push({name: "Home"})
        })
        return response
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
    background: white;
    width: fit-content;
    margin: auto;
    padding: 0em 1em;
    border: 4px inset #3e4e22;
  }
  .control-panel ul .player_1 {
    color: #b37c34;
    background: white;
    width: fit-content;
    margin: auto;
    padding: 0em 1em;
    border: 4px inset #3e4e22;
  }
  .control-panel ul li{
    margin: 1em 0;
    color: whitesmoke;
  }
</style>