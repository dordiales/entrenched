<template>
  <div class="modal-wrapper" >

      <article>
          <h1>Reglas de combate</h1>
          <ul>
              <li>
                    <ul>
                        <li><img src="https://i.imgur.com/8WtYp5E.png" alt="imagen de tropa inglesa"></li>
                        <li><img src="https://i.imgur.com/sgBDzUb.png" alt="imagen de tropa alemana"></li>
                        <li><p>vencen a</p></li>
                        <li><img src="https://i.imgur.com/64Vdf7N.png" alt="imagen de granadero inglés"></li>
                        <li><img src="https://i.imgur.com/guKaS99.png" alt="imagen de granadero alemán"></li>
                    </ul>
              </li>

              <li>
                    <ul>
                        <li><img src="https://i.imgur.com/64Vdf7N.png" alt="imagen de granadero inglés"></li>
                        <li><img src="https://i.imgur.com/guKaS99.png" alt="imagen de granadero alemán"></li>
                        <li><p>vencen a</p></li>
                        <li><img src="https://i.imgur.com/SROxcoG.png" alt="imagen de ametralladora inglesa"></li>
                        <li><img src="https://i.imgur.com/ECbNeFH.png" alt="imagen de ametralladora alemana"></li>
                    </ul>   
              </li>

              <li>
                    <ul>
                        <li><img src="https://i.imgur.com/SROxcoG.png" alt="imagen de ametralladora inglesa"></li>
                        <li><img src="https://i.imgur.com/ECbNeFH.png" alt="imagen de ametralladora alemana"></li>
                        <li><p>vencen a</p></li>
                        <li><img src="https://i.imgur.com/8WtYp5E.png" alt="imagen de tropa inglesa"></li>
                        <li><img src="https://i.imgur.com/sgBDzUb.png" alt="imagen de tropa alemana"></li>
                    </ul>  
              </li>
          </ul>
          <p>Captura el cuartel general enemigo para ganar</p>
          <ul class="hq-rules">
                <li>
                    <img src="https://i.imgur.com/gKYRMFk.png" alt="imagen del cuartel general inglés">
                    <p>Cuartel Inglés</p>
                </li>
                <li>
                    <img src="https://i.imgur.com/nzf6NaJ.png" alt="imagen del cuartel general alemán">
                    <p>Cuartel Alemán</p>
                </li>
          </ul>
          <button class="button-red" @click="modalClose">Cerrar</button>
      </article>

  </div>
  
</template>

<script>


export default {
    
    name: "RulesModal",
    props: {
    },
    methods: {
    modalClose(){
      this.$emit("closeRules")

    },
  },
  
}
</script>

<style scoped>

*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

.modal-wrapper{
    width: 100vw;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: rgba(250, 246, 246, 0.589);
    position: fixed;
    top: 0;
    left:0;
    z-index: 999;

}
article{
    width:70%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    border: 4px inset #3e4e22;
    box-shadow: 0px 6px 0px #58732a;
    background-color: #58732a;
    padding: 1em 1em 3em;
    color:#fae8b9;
}

article p{
    font-size: 1.2em;
    margin-top:1em;
    margin-bottom: 1em;
    font-weight: bold;
}
article h1{

    margin-top: 2em;
    font-weight: bold;
}
button {
    padding: 0.5em;
}

ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
ul li ul li {
    display:inline-block;
    vertical-align: middle;
}
ul li ul li p{
    margin: 0 1em;
}

img {
  max-width: 5em;
}
.hq-rules li{
    display:inline-block;
    vertical-align: middle;
    margin: 1em;
    margin-top: 0;
}

@media only screen and (orientation:landscape) and (max-width:961px){
    article {
        padding: 1em;
    }
    img {
        max-width: 3em;
    }

    article h1{
        font-size: 80%;
        margin:0;
    }
    
    article p {
        font-size: 80%;
        margin: 0;
    }

    ul li ul li p{
        font-size: 80%;
    }

    article button {
        font-size: 80%;
        margin-top: 1em;
    }

    .hq-rules li {
        margin:0;
    }
 }

@media only screen and (orientation:portrait) and (max-width:450px){
    article {
        padding: 1em;
    }
    img {
        max-width: 3em;
    }

    article h1{
        font-size: 80%;
        margin:0;
    }
    
    article p {
        font-size: 80%;
        margin: 0;
    }

    ul li ul li p{
        font-size: 80%;
    }

    article button {
        font-size: 80%;
        margin-top: 1em;
    }

    .hq-rules li {
        margin:0;
    }
}

</style>