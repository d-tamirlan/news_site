<template>
  <div id="app">
    <h1>News site</h1>
    <ul class="categories-list">
      <li v-for="category in categories.results" class="categories-list__category">
        {{ category.name }}
      </li>
    </ul>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'app',
    data () {
      return {
        rootDomain: 'http://localhost:8000/',
        categories: [],
      }
    },
    created(){
      this.getAllCategories();
    },
    methods:{
      getAllCategories(){
        let categories_url = this.rootDomain+'categories-list/';

        axios.get(categories_url).then(response => {
          this.categories = response.data;
          console.log(this.categories)
        }).catch(error => {
          console.log('--error--');
          console.log(error);
        })
      }
    }
  }
</script>

<style lang="scss">
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .categories-list{
    list-style: none;
    display: flex;
    flex-wrap: wrap;
  }
  .categories-list__category{
    margin-left: 20px;
  }
</style>
