export default {
  loading: "~/components/loading.vue",
  /*
  ** Nuxt rendering mode
  ** See https://nuxtjs.org/api/configuration-mode
  */
  ssr: false,
  /*
  ** Nuxt target
  ** See https://nuxtjs.org/api/configuration-target
  */
  target: 'server',
  publicRuntimeConfig: {
  },
  privateRuntimeConfig: {
    baseAPIURL: process.env.BASE_API_URL
  },
  /*
  ** Headers of the page
  ** See https://nuxtjs.org/api/configuration-head
  */
  head: {
    title: "Quản lí nhân sự - Yody",
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/yody.jpg' }
    ]
  },
  /*
  ** Global CSS
  */
  css: [
    "~/assets/scss/app.scss",
    'quill/dist/quill.core.css',
    'quill/dist/quill.snow.css',
    'quill/dist/quill.bubble.css'
  ],
  /*
  ** Plugins to load before mounting the App
  ** https://nuxtjs.org/guide/plugins
  */
  plugins: [
    "~/plugins/simplebar.js",
    "~/plugins/vue-click-outside.js",
    "~/plugins/vuelidate.js",
    "~/plugins/draggable.js",
    "~/plugins/vue-slidebar.js",
    "~/plugins/tour.js",
    "~/plugins/vue-lightbox.js",
    "~/plugins/mask.js",
    "~/plugins/quill-editor.js",
    "~/plugins/chartist.js",
    "~/plugins/vue-googlemap.js",
    "~/plugins/string-filter"
  ],
  /*
  ** Auto import components
  ** See https://nuxtjs.org/api/configuration-components
  */
  components: true,
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org
    'bootstrap-vue/nuxt',
    'nuxt-i18n',
    '@nuxtjs/axios',
    '@nuxtjs/auth-next',
    '@nuxtjs/toast',
    '@nuxtjs/pwa',
  ],
  i18n: {
    locales: ['vi', 'en'],
    defaultLocale: 'vi',
    vueI18n: {
      fallbackLocale: 'vi',
      messages: {
        vi: require('./locales/vi.json'),
        en: require('./locales/en.json'),
      }
    }
  },
  // Axios configuration
  axios: {
    baseURL: process.env.BASE_API_URL
  },
  toast: {
    position: 'bottom-right',
    duration: '6000',
    action: {
      icon: 'mdi-close-circle',
      onClick: (e, toastObject) => {
        toastObject.goAway(0)
      },
    },
    iconPack: 'mdi',
  },
  pwa: {
    meta: {
      title: 'DDIC-HR',
      author: 'DDIC',
    },
    manifest: {
      name: 'DDIC-HR',
      short_name: 'HR',
      lang: 'en',
      display: 'standalone'
    }
  },
  /*
  ** Build configuration
  ** See https://nuxtjs.org/api/configuration-build/
  */
  build: {
  },
  // Nuxt-auth configuration
  auth: {
    strategies: {
      local: {
        scheme: 'refresh',
        token: {
          property: "access",
          global: true,
          maxAge: 60 * 60 * 24
        },
        refreshToken: {
          property: 'refresh',
          data: 'refresh',
          maxAge: 60 * 60 * 24 * 7
        },
        user: {
          property: 'info',
        },
        endpoints: {
          login: { 
            url: '/api/token/',
            method: 'post',
            propertyName: "access"
          },
          refresh: { 
            url: '/api/token/refresh/', 
            method: 'post'
          },
          logout: false,
          user: { 
            url: '/api/accounts/information/', 
            method: 'get',
            propertyName: 'info'
          }
        }
      },
      //autoLogout: true
    },
    redirect: {
      login: '/auth/login',
      logout: '/auth/login',
      callback: '/auth/login',
      home: '/'
    }
  },
  // Middlewares
  router: {
    middleware: ['auth']
  },
  server: {
    host: "0.0.0.0"
  }
}
