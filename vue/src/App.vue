<template>
  <div id="app">
    <h1>News site</h1>
    <ul class="categories-list">
      <li v-for="category in categories"
          class="categories-list__category"
          @click="getCategoryNews(category.id)"
      >
          {{ category.name }}
      </li>
    </ul>
    <main class="main">
      <aside>
        <section class="news-list">
          <div v-for="news in newsList.results" class="news-list__news">
            <router-link :to="{ name: 'news', params: { id: news.id } }">
              <img :src="news.image" alt="" width="300">
              <h3>{{ news.title }}</h3>
            </router-link>
          </div>
        </section>
        <section class="pagination">
            <button @click="getCategoryNews(currentCategory, newsList.previous)" v-if="newsList.previous">
              previous
            </button>

            <button @click="getCategoryNews(currentCategory, newsList.next)" v-if="newsList.next">
              next
            </button>
        </section>
      </aside>

      <section class="news">
        <router-view></router-view>
      </section>
    </main>
  </div>
</template>

<script>
  import axios from 'axios'
  import News from './Components/News.vue'

  export default {
    name: 'app',
    props: ['page'],
    data () {
      return {
        rootDomain: 'http://localhost:8000/',
        categories: [],
        newsList: [],
        currentCategory: null,
      }
    },
    created(){
      this.getAllCategories();
      this.getCategoryNews();
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
      getCategoryNews(category_id, page_url){
        this.currentCategory = category_id;

        let category = category_id ? `?category_id=${category_id}`: '';
        let news_url = page_url || this.rootDomain + `news/${category}`;

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
    -moz-osx-font-smoothing:w grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
  }
  .categories-list{
    border: 1px solid black;
    padding: 10px;
    list-style: none;
    display: flex;
    flex-wrap: wrap;

    &__category{
      text-decoration: underline;
      cursor: pointer;
      margin-left: 20px;
    }
  }
  .main{
    display: flex;
    justify-content: space-between;
  }
  .news-list{
    min-width: 300px;
    border: 1px solid black;
  }
  .news{
    border: 1px solid black;
  }
  aside{
    border: 1px solid black;
  }
</style>
