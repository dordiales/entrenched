<template>

    <h3>Es el turno del comandante {{commanderTrun}}</h3>

    <div class="page-organizer">

    <div class="board-wrapper">
    <section class="game-board">
      <article  v-for="square in squares" class="square" v-bind:class="square.player" :key="square.square">
        <img :src="getSoldierIcon(square)" :alt="square.player + '-' + square.soldier" v-if="square.soldier !=undefined">
      </article>
    </section>
    </div>


    <section class="join-buttons">
      <button class="button-player1" v-if="player1 === null" @click="joinAsPlayer('player_1')">Unirse como Jugador 1: Ingleses</button>
      <button class="button-player1-disabled" v-else disabled>Unirse como Jugador 1: Ingleses</button>

      <button class="button-player2" v-if="player2 === null" @click="joinAsPlayer('player_2')">Unirse como Jugador 2: Alemanes</button>
      <button class="button-player2-disabled" v-else disabled>Unirse como Jugador 2: Alemanes</button>
    </section>
    <router-link to="/"><button class="button-green">Volver a seleccion de partida</button></router-link>
    </div>
    

    <WinnerModal v-show="modalOpened" :winner="winner" @finish="finishGame"/>

    

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
  computed: {
    commanderTrun (){
      if (this.activePlayer === "player_1"){
        return "inglés"
      } else {
        return "alemán"
      } 
    },

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
      const dataRefresh = window.setInterval(() => {
        const onCreationRoute = this.gameId
        if (this.$route.params.gameId != onCreationRoute){
          window.clearInterval(dataRefresh)
        } else {
          this.loadData()
        }
      }, 5000);
    },
    
    openWinnerModal() {
      this.modalOpened = true;
    },
    closeWinnerModal() {
      this.modalOpened = false;
    },
    async joinAsPlayer(playerName){
      const response = await joinGame(playerName, this.gameId)
      if (response.ok){
      this.$router.push({name: "Player" ,params:{gameId: this.gameId, playerId: playerName}})
      }
      return response
      
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
    finishGame(){
      this.$router.push({name: "Home"})
    }
  },
}
</script>

<style scoped>

  button {
    margin: 1em
  }
  h3{
    margin-top: 5em;
  }
  .game-board {
      display: grid;
      grid-template-rows: 5em 5em 5em 5em 5em;
      grid-template-columns: 5em 5em 5em 5em 5em 5em 5em 5em 5em;
      margin: 2em auto;
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
  .player_1 {
    color: #5a6db1;
  }
  .player_2 {
    color: #b37c34;
  }

  @media only screen and (orientation:landscape) and (max-width:961px){

    h3 {
      height: 5vh;
      margin-top: 0.5em;
      margin-bottom: 1em;
    }

    .page-organizer {
      display: grid;
      grid-template-areas: "join-buttons board"
                            "return-button board";
      grid-template-columns: 3fr 8fr;
      grid-template-rows: 2fr 1fr;
    }

    .board-wrapper {
      grid-area: board;
      width: 70vw;
      height: 80vh;
      margin: 0 auto;
    }
    .game-board {
      
      width: 100%;
      height: 100%;
      margin: 0em;
      grid-template-columns: auto auto auto auto auto auto auto auto auto;;
      grid-template-rows: auto auto auto auto auto;

    }
    .square {
      border: 1px dashed rgb(153, 58, 35);
      background-color: beige;
      min-width: 0;
      min-height: 0;
      object-fit: contain;


    }
    .square img {
      min-width: 0;
      min-height: 0;
      object-fit: contain;
    }
    
  }

  .join-buttons {
    grid-area: join-buttons;
  }
  .green-button {
    grid-area: return-button;
  }

  @media only screen and (orientation:portrait) and (max-width:450px){

    h3 {
      height: 5vh;
      margin-top: 0.5em;
      margin-bottom: 1em;
      align-content: center;
    }

    .page-organizer {
      display: grid;
      grid-template-areas: "join-buttons board"
                            "return-button board";
      grid-template-columns: 3fr 8fr;
      grid-template-rows: 2fr 1fr;
    }

    .board-wrapper {
      grid-area: board;
      width: 70vh;
      height: 80vw;
      margin: 0 auto;
    }
    .game-board {
      
      width: 100%;
      height: 100%;
      margin: 0em;
      grid-template-columns: auto auto auto auto auto auto auto auto auto;;
      grid-template-rows: auto auto auto auto auto;

    }
    .square {
      border: 1px dashed rgb(153, 58, 35);
      background-color: beige;
      min-width: 0;
      min-height: 0;
      object-fit: contain;


    }
    .square img {
      min-width: 0;
      min-height: 0;
      object-fit: contain;
    }
    
  }

  .join-buttons {
    grid-area: join-buttons;
  }
  .green-button {
    grid-area: return-button;
  }
</style>