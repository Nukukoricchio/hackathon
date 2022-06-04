<template>
  <!-- Topbar Start -->
  <div class="navbar-custom">
    <div class="container-fluid">
      <ul class="list-unstyled topnav-menu float-right mb-0">
        <li class="d-none d-lg-block">
          <form class="app-search">
            <div class="app-search-box">
              <div class="input-group">
                <input
                  type="search"
                  class="form-control"
                  :placeholder="$t('navbar.search.text')"
                  id="top-search"
                />
                <div class="input-group-append">
                  <button class="btn" type="submit">
                    <i class="fe-search"></i>
                  </button>
                </div>
              </div>
            </div>
          </form>
        </li>

        <li class="dropdown d-inline-block d-lg-none">
          <a
            class="nav-link dropdown-toggle arrow-none waves-effect waves-light"
            data-toggle="dropdown"
            href="#"
            role="button"
            aria-haspopup="false"
            aria-expanded="false"
          >
            <i class="fe-search noti-icon"></i>
          </a>
          <div class="dropdown-menu dropdown-lg dropdown-menu-right p-0">
            <form class="p-3">
              <input
                type="text"
                class="form-control"
                :placeholder="$t('navbar.search.text')"
                aria-label="Recipient's username"
              />
            </form>
          </div>
        </li>

        <li class="dropdown d-none d-lg-inline-block">
          <a
            class="nav-link dropdown-toggle arrow-none waves-effect waves-light"
            @click="initFullScreen"
            data-toggle="fullscreen"
            href="#"
          >
            <i class="fe-maximize noti-icon"></i>
          </a>
        </li>

        <b-nav-item-dropdown
          variant="white"
          class="d-none d-lg-inline-block"
          right
          toggle-class="header-item"
        >
          <template v-slot:button-content>
            <img class :src="flag" alt="Header Language" height="16" />
            {{ text }}
          </template>
          <b-dropdown-item
            class="notify-item"
            v-for="(entry, i) in languages"
            :key="`Lang${i}`"
            :value="entry"
            @click="setLanguage(entry.language, entry.title, entry.flag)"
            :link-class="{ active: entry.language === current_language }"
          >
            <img
              :src="`${entry.flag}`"
              alt="user-image"
              class="mr-1"
              height="12"
            />
            <span class="align-middle">{{ entry.title }}</span>
          </b-dropdown-item>
        </b-nav-item-dropdown>
        <b-nav-item-dropdown
          right
          class="notification-list"
          menu-class="dropdown-lg"
        >
          <template slot="button-content" class="nav-link dropdown-toggle">
            <i class="fe-bell noti-icon"></i>
            <span class="badge badge-danger rounded-circle noti-icon-badge">{{
              $t("navbar.dropdown.notification.badge")
            }}</span>
          </template>

          <a href="#" class="dropdown-item noti-title">
            <h5 class="m-0">
              <span class="float-right">
                <a href class="text-dark">
                  <small>{{
                    $t("navbar.dropdown.notification.subtext")
                  }}</small>
                </a>
              </span>
              {{ $t("navbar.dropdown.notification.text") }}
            </h5>
          </a>

          <simplebar style="max-height: 230px;">
            <a
              href="javascript:void(0);"
              class="dropdown-item notify-item active"
            >
              <div class="notify-icon bg-soft-primary text-primary">
                <i class="mdi mdi-comment-account-outline"></i>
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.1.title") }}
                <small class="text-muted">{{
                  $t("navbar.dropdown.notification.1.text")
                }}</small>
              </p>
            </a>

            <!-- item-->
            <a href="javascript:void(0);" class="dropdown-item notify-item">
              <div class="notify-icon">
                <img
                  src="~/assets/images/users/avatar-2.jpg"
                  class="img-fluid rounded-circle"
                  alt
                />
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.2.title") }}
              </p>
              <p class="text-muted mb-0 user-msg">
                <small>{{ $t("navbar.dropdown.notification.2.text") }}</small>
              </p>
            </a>

            <!-- item-->
            <a href="javascript:void(0);" class="dropdown-item notify-item">
              <div class="notify-icon">
                <img
                  src="~/assets/images/users/avatar-4.jpg"
                  class="img-fluid rounded-circle"
                  alt
                />
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.3.title") }}
              </p>
              <p class="text-muted mb-0 user-msg">
                <small>{{ $t("navbar.dropdown.notification.3.text") }}</small>
              </p>
            </a>

            <!-- item-->
            <a href="javascript:void(0);" class="dropdown-item notify-item">
              <div class="notify-icon bg-soft-warning text-warning">
                <i class="mdi mdi-account-plus"></i>
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.4.title") }}
                <small class="text-muted">{{
                  $t("navbar.dropdown.notification.4.text")
                }}</small>
              </p>
            </a>

            <!-- item-->
            <a href="javascript:void(0);" class="dropdown-item notify-item">
              <div class="notify-icon bg-info">
                <i class="mdi mdi-comment-account-outline"></i>
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.5.title") }}
                <small class="text-muted">{{
                  $t("navbar.dropdown.notification.5.text")
                }}</small>
              </p>
            </a>

            <!-- item-->
            <a href="javascript:void(0);" class="dropdown-item notify-item">
              <div class="notify-icon bg-secondary">
                <i class="mdi mdi-heart"></i>
              </div>
              <p class="notify-details">
                {{ $t("navbar.dropdown.notification.6.title") }}
                <small class="text-muted">{{
                  $t("navbar.dropdown.notification.6.text")
                }}</small>
              </p>
            </a>
          </simplebar>

          <a
            href="javascript:void(0);"
            class="dropdown-item text-center text-primary notify-item notify-all"
          >
            {{ $t("navbar.dropdown.notification.button") }}
            <i class="fi-arrow-right"></i>
          </a>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown
          right
          class="notification-list topbar-dropdown"
          menu-class="profile-dropdown"
          toggle-class="p-0"
        >
          <template slot="button-content" class="nav-link dropdown-toggle">
            <div class="nav-user mr-0">
              <img
                class="rounded-circle header-profile-user"
                :src="'http://192.168.9.84:8000' + avatar"
                alt=""
              />
              <span class="pro-user-name ml-1">
                {{ name }}
                <i class="mdi mdi-chevron-down"></i>
              </span>
            </div>
          </template>
          <!-- item-->
          <!-- <nuxt-link class="dropdown-item" :to="'/profile/' + userId">
            <i
              class="fas fa-book-reader font-size-18 align-middle text-muted me-1"
            ></i>
            <span class="align-middle">Thông tin cá nhân</span>
          </nuxt-link> -->
          <b-dropdown-divider></b-dropdown-divider>
          <a
            class="dropdown-item"
            @click="logoutUser"
            href="javascript: void(0);"
          >
            <i class="fe-log-out mr-1"></i>
            <span>Đăng xuất</span>
          </a>
        </b-nav-item-dropdown>
      </ul>

      <!-- LOGO -->
      <div class="logo-box">
        <nuxt-link to="/" class="logo logo-dark text-center">
          <span class="logo-sm">
            <img src="~/assets/images/banner.jpg" alt height="24" />
            <!-- <span class="logo-lg-text-light">Minton</span> -->
          </span>
          <span class="logo-lg">
            <img src="~/assets/images/banner.jpg" alt height="20" />
            <!-- <span class="logo-lg-text-light">M</span> -->
          </span>
        </nuxt-link>

        <nuxt-link to="/" class="logo logo-light text-center">
          <span class="logo-sm">
            <img src="~/assets/images/banner.jpg" alt height="24" />
          </span>
          <span class="logo-lg">
            <img src="~/assets/images/banner.jpg" alt height="20" />
          </span>
        </nuxt-link>
      </div>

      <ul class="list-unstyled topnav-menu topnav-menu-left m-0">
        <li>
          <button
            class="button-menu-mobile waves-effect waves-light"
            @click="toggleMenu"
          >
            <i class="fe-menu"></i>
          </button>
        </li>
      </ul>
      <div class="clearfix"></div>
    </div>
  </div>
  <!-- end Topbar -->
</template>

<script>
/**
 * Topbar component
 */
export default {
  data() {
    return {
      languages: [
        {
          flag: require("~/assets/images/flags/vi.png"),
          language: "vi",
          title: "Tiếng việt"
        },
        {
          flag: require("~/assets/images/flags/us.jpg"),
          language: "en",
          title: "English"
        }
      ],
      current_language: this.$i18n.locale,
      text: null,
      flag: null,
      value: null,
      avatar: this.$auth.user.avatar,
      name: this.$auth.user.full_name,
      userId: this.$auth.user.id
    };
  },
  mounted() {
    this.value = this.languages.find(x => x.language === this.$i18n.locale);
    this.text = this.value.title;
    this.flag = this.value.flag;
  },
  methods: {
    /**
     * Toggle menu
     */
    toggleMenu() {
      this.$parent.toggleMenu();
    },
    /**
     * Full screen
     */
    initFullScreen() {
      document.body.classList.toggle("fullscreen-enable");
      if (
        !document.fullscreenElement &&
        /* alternative standard method */
        !document.mozFullScreenElement &&
        !document.webkitFullscreenElement
      ) {
        // current working methods
        if (document.documentElement.requestFullscreen) {
          document.documentElement.requestFullscreen();
        } else if (document.documentElement.mozRequestFullScreen) {
          document.documentElement.mozRequestFullScreen();
        } else if (document.documentElement.webkitRequestFullscreen) {
          document.documentElement.webkitRequestFullscreen(
            Element.ALLOW_KEYBOARD_INPUT
          );
        }
      } else {
        if (document.cancelFullScreen) {
          document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
          document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
          document.webkitCancelFullScreen();
        }
      }
    },
    /**
     * Toggle rightbar
     */
    toggleRightSidebar() {
      this.$parent.toggleRightSidebar();
    },
    /**
     * Set languages
     */
    setLanguage(locale, country, flag) {
      this.$i18n.locale = locale;
      this.current_language = locale;
      this.text = country;
      this.flag = flag;
    },
    /**
     * Horizontal-toggle menu
     */
    horizonalmenu() {
      let element = document.getElementById("topnav-menu-content");
      element.classList.toggle("show");
    },
    async logoutUser() {
      await this.$auth.logout();
    },
  }
};
</script>
