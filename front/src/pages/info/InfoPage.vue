<template>

    <h1>COMO JUGAR A ENTRENCHED</h1>
    <section class="create-game-info">
      <h2>Cómo crear o unirse a una partida</h2>
      <img src="https://i.imgur.com/JspZZSc.png" alt="imagen soldado inglés">
      <p>
        En la página home tendrás acceso a una casilla de entrada en la que puedes escribir 
        el nombre de una partida. El botón junto a esta casilla ("Ir a la partida") te permite 
        crear una partida con el nombre que hayas introducido, o si ya existe una partida con ese 
        nombre te llevará a la página de la partida.
      </p>
    </section>

    <section class="join-game-info">
      <h2>Los equipos</h2>
      <p>En cada partida existen 2 equipos</p>
      <ul class="team-soldiers">
        <li>
          <figure>
            <img src="https://i.imgur.com/wf7jOk5.png" alt="imagen soldado inglés">
            <figcaption>Ingleses</figcaption>
          </figure>
        </li>
        <li>
          <figure>
            <img src="https://i.imgur.com/KtNJ5T1.png" alt="imagen de soldado alemán">
            <figcaption>Alemanes</figcaption>
          </figure>
        </li>
      </ul>
      <p>Al entrar en una partida llegarás a la pantalla de visualizacion del juego</p>
      <figure>
        <img src="https://i.imgur.com/C8qnP8Y.png" alt="ejemplo pantalla de visualización del juego">
        <figcaption>
          En la pantalla de visualizacion de una partida puedes usar los dos 
          botones al pie del tablero de la partida para unirte a uno de los dos equipos
        </figcaption>
      </figure>
      <figure>
        <img src="https://i.imgur.com/benb32C.png" alt="ejemplo de botones de unirse a un equipo desactibados">
        <figcaption>
          Si alguien se ha conectado previamente como uno de los dos 
          jugadores en la partida aparecera el botón de unirse desactivado
        </figcaption>
      </figure>
      
    </section>

    <hr>

    <section class="rules-info">
      <h2>Las reglas del juego</h2>
      <h3>Pantalla</h3>
      <section class="interface-info">
        <img class="ui-img" src="https://i.imgur.com/reFOgLm.png" alt="ejemplo pantalla juego para los jugadores activos">
        <p class= ui-up>
          En la pantalla de la parte superior muestra el tablero de juego, 
          puedes clicar en uno de tus soldados para moverlo a una casilla adyacente, 
          pero solo si es tu turno y la casilla esta vacía o tiene a un enemigo.
          El cuartel general no se puede mover en ningun caso. 
          En caso de mover a la casilla de un enemigo se iniciará un asalto (ver reglas del combate)
        </p>
        <p class="ui-down">
          En la parte inferior dispones de la información del equipo al que te has unido,
          a qué equipo le toca realizar un movimiento y el botón para abandonar la partida y 
          un botón que hace aparecer la información de las reglas de combate
        </p>
      </section>

      <h3>Soldados</h3>
      <p>En el juego existen 3 tipos de soldados</p>

      <ul class="soldier-types">
        <li>
          <p>Tropas</p>
          <ul>
            <li>
              <figure>
                <img src="https://i.imgur.com/8WtYp5E.png" alt="imagen de tropa inglesa">
                <figcaption>Tropa Inglesa</figcaption>
              </figure>
            </li>
            <li>
              <figure>
                <img src="https://i.imgur.com/sgBDzUb.png" alt="imagen de tropa alemana">
                <figcaption>Tropa Alemana</figcaption>
              </figure>
            </li>
          </ul>
        </li>

        <li>
          <p>Granaderos</p>
          <ul>
            <li>
              <figure>
                <img src="https://i.imgur.com/64Vdf7N.png" alt="imagen de granadero inglés">
                <figcaption>Granadero Inglés</figcaption>
              </figure>
            </li>
            <li>
              <figure>
                <img src="https://i.imgur.com/guKaS99.png" alt="imagen de granadero alemán">
                <figcaption>Granadero Alemán</figcaption>
              </figure>
            </li>
          </ul>
        </li>
        
        <li>
          <p>Ametralladoras</p>
          <ul>
            <li>
              <figure>
                <img src="https://i.imgur.com/SROxcoG.png" alt="imagen de ametralladora inglesa">
                <figcaption>Ametralladora Inglesa</figcaption>
              </figure>
            </li>
            <li>
              <figure>
                <img src="https://i.imgur.com/ECbNeFH.png" alt="imagen de ametralladora alemana">
                <figcaption>Ametralladora Alemana</figcaption>
              </figure>
            </li>
          </ul>
        </li>
      </ul>

      <h3>Reglas del combate</h3>
      <p>Los diferentes soldados poseen una relación de quien puede derrotar a quien en combate.</p>
      <p>Las tropas vencen a los granaderos y pierden contra las ametralladoras.</p>
      <p>Los granaderos vencen a las ametralladoras pero son derrotados por las tropas.</p>
      <p>Las ametralladoras derrotan a las tropas pero pierden contra los granaderos.</p>
      <p>En caso de empate, ambos soldados son derrotados.</p>

      <h3>Cuarteles generales y como terminar la partida.</h3>
      <p>Cada jugador tiene un cuartel general (HQ), si atacas el cuartel del enemigo ganas la partida</p>

      <ul class="hq">
        <li>
          <figure>
            <img src="https://i.imgur.com/gKYRMFk.png" alt="imagen del cuartel general inglés">
            <figcaption>Cuartel General Inglés</figcaption>
          </figure>
        </li>
        <li>
          <figure>
            <img src="https://i.imgur.com/nzf6NaJ.png" alt="imagen del cuartel general inglés">
            <figcaption>Cuartel General Alemán</figcaption>
          </figure>
        </li>
      </ul>



    </section>

    <footer>
      <p>Art made by cheese.sketch</p>
      <p>Instagram</p>
      <a href="https://www.instagram.com/cheese.sketch/">@cheese.sketch</a>
    </footer>
</template>

<script>
export default {
  name: 'Info',
  data() {
    return {
    }
  },
}
</script>

<style scoped>
h1 {
  font-style: italic;
}
footer {
  margin-top: 2em;
}
footer p{
  margin: 0.2em;
  justify-content: center;
}
ul {
  list-style: none;
  margin: 0;
  padding: 0;
}

h3 {
  margin-top: 2em;
}
p {
  max-width: 60vw;
  margin: 0 auto;
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
.team-soldiers img {
  max-width: 15em;
}

.team-soldiers li{
  display: inline-block;
}

.interface-info {
  display: grid;
  grid-template-areas: 
    "ui up" 
    "ui down";
}

.ui-img{
  grid-area: ui;
  max-width: 50vw;
}

.ui-up{
  grid-area: up;
  margin: auto 5em auto 0;
  width: 40vw;
}

.ui-down{
  grid-area: down;
  margin: auto 5em auto 0;
  width: 40vw;
}

.soldier-types img {
  max-width: 10em;
}

.soldier-types li ul li{
  display: inline-block;
}
.hq li{
  display: inline-block;
}
.hq img {
  max-width: 15em;
}
</style>
