<template>
  <div v-if="news">
    <h3>{{ news.title }}</h3>
    <div><img :src="news.image" alt=""></div>
    <div v-html="news.text"></div>
    <p>{{ news.pub_date }}</p>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'app',
    props: ['id'],
    data () {
      return {
        news: null
      }
    },
    created(){
      this.getNews(this.id);
    },
    methods:{
      getNews(id){
        let news_url = this.$parent.rootDomain+'news/' + id +'/';

        axios.get(news_url).then(response => {
          this.news = response.data;
          console.log('-- getNews --');
          console.log(this.news)
        }).catch(error => {
          console.log('--getNews error--');
          console.log(error);
        })
      },
    },
    watch: {
        '$route'() {
          this.getNews(this.id);
        }
      }
  }
</script>

<style lang="scss">

</style>
