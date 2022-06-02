<template>
  <div class="modal-wrapper" >

      <article>
          <h1>{{winner}}</h1>
          <p>gana la partida</p>
      </article>

  </div>
  
</template>

<script>


export default {
    
    name: "WinnerModal",
    props: {
        winner: {
            type: String,
            required: true
        }
    },
    methods: {
    modalClose(){
      this.$emit("closeModal")

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
    background-color: rgb(77, 91, 106);
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