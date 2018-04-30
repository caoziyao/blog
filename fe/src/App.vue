<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    /*text-align: center;*/
    color: #2c3e50;
    height: 900px;
    /*margin-top: 60px;*/
  }

  a:link {
   color: #000000;
   text-decoration: none;
  }
  a:visited {
   color: #000000;
   text-decoration: none;
  }
  a:hover {
   color: #999999;
   text-decoration: underline;
  }
</style>
