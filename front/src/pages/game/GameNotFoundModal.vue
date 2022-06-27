<template>
  <div class="modal-wrapper" >

      <article>
          <h1>Partida no encontrada</h1>
          <p>La partida que esta buscando no existe o ya se ha acabado</p>
          <button class="button-red" @click="closeModal">Volver a Home</button>
      </article>

  </div>
  
</template>

<script>


export default {
    
    name: "GameNotFoundModal",
    props: {
    },
    emits: ['close'],
    methods: {
    closeModal(){
      this.$emit("close")

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

button{
    padding: 0.5em;
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
    margin-bottom: 2em;
    font-weight: bold;
}
article h1{

    margin-top: 2em;
    font-weight: bold;
}


</style>