<template>
  <div>
    <PageHeader :title="title" :items="items" />
    <div class="card">
      <div class="card-body">
        <h5 class="card-title mb-3">{{ post.title }}</h5>
        <div class="card-text" v-html="post.content"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: `${this.title} | Yody`,
    };
  },
  data() {
    return {
      title: "Trang chủ",
      items: [
        {
          text: "Yody",
        },
        {
          text: "Trang chủ",
          active: true,
        },
      ],
      post: {
        title: '',
        content: ''
      }
    };
  },
  async created() {
    // await this.getLastestPost()
  },
  methods: {
    async getLastestPost() {
      try {
        let response = await this.$axios.get('/api/post/lastest/')
        this.post = response.data
      } catch (error) {
        if (error.response.status == 400) {
          let errors = error.response.data;
          // Toast errors
          for (let err in errors) {
            this.$toast.error(err + " : " + errors[err], {
              icon: "alert",
            });
          }
        } else {
          this.$toast.error("Đã có lỗi xảy ra", {
            icon: "alert",
          });
        }
      }
    }
  }
};
</script>
