<template>
  <div id="app">
    <h1>News site</h1>
    <ul class="categories-list">
      <li v-for="category in categories"
          class="categories-list__category"
          :category_id="category.id"
          @click="getAllNews($event)"
      >
          {{ category.name }}
      </li>
    </ul>

    <div class="content">
      <section class="news-list">
        <div v-for="news in newsList.results" class="news-list__news">
          <router-link :to="{ name: 'news', params: { id: news.id } }">
            <img :src="news.image" alt="" width="300">
            <h3>{{ news.title }}</h3>
          </router-link>
        </div>
      </section>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import News from './Components/News.vue'

  export default {
    name: 'app',
    data () {
      return {
        rootDomain: 'http://localhost:8000/',
        categories: [],
        newsList: [],
      }
    },
    created(){
      this.getAllCategories();
      this.getAllNews();
    },
    methods:{
      getAllCategories(){
        let categories_url = this.rootDomain+'categories-list/';

        axios.get(categories_url).then(response => {
          this.categories = response.data.results;
        }).catch(error => {
          console.log('--getAllCategories error--');
          console.log(error);
        })
      },
      getAllNews(event){
        let category = '';

        if (event !== undefined){
          category = '?category_id=' + event.currentTarget.getAttribute('category_id')
        }

        let news_url = this.rootDomain + 'news/' + category;

        axios.get(news_url).then(response => {
          this.newsList = response.data;
        }).catch(error => {
          console.log('--getAllNews error--');
          console.log(error);
        })
      },
    },
    components: {
        'news': News,
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
