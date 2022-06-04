<template>
  <div class="row justify-content-center">
    <div class="col-md-8 col-lg-6 col-xl-5">
      <div class="card">
        <div class="card-body p-4">
          <div class="text-center w-75 m-auto">
            <div class="auth-logo">
              <nuxt-link to="/" class="logo logo-dark text-center">
                <span class="logo-lg">
                  <img src="~/assets/images/yody.png" alt height="70" />
                </span>
              </nuxt-link>

              <nuxt-link to="/" class="logo logo-light text-center">
                <span class="logo-lg">
                  <img src="~/assets/images/yody.png" alt height="70" />
                </span>
              </nuxt-link>
            </div>
            <p class="text-muted mb-4 mt-3">
              Đăng nhập vào hệ thống quản lý nhân sự của Yody.
            </p>
          </div>

          <form @submit.prevent="userLogin">
            <div class="form-group mb-3">
              <label for="email">Địa chỉ email</label>
              <input
                type="email"
                class="form-control"
                id="email"
                placeholder="Nhập email ..."
                v-model="login.email"
                required
              />
            </div>

            <div class="form-group mb-3">
              <label for="password">Mật khẩu</label>
              <div class="input-group input-group-merge">
                <input
                  type="password"
                  class="form-control"
                  id="password"
                  placeholder="Nhập mật khẩu ..."
                  v-model="login.password"
                  required
                />
                <div class="input-group-append" data-password="false">
                  <div class="input-group-text">
                    <span class="password-eye" id="togglePassword" @click="toggleVisibility"></span>
                  </div>
                </div>
              </div>
            </div>

            <div class="form-group mb-3">
              <div class="custom-control custom-checkbox">
                <input
                  type="checkbox"
                  class="custom-control-input"
                  id="checkbox-signin"
                  checked
                />
                <label class="custom-control-label" for="checkbox-signin"
                  >Ghi nhớ đăng nhập</label
                >
              </div>
            </div>

            <div class="form-group mb-0 text-center">
              <button class="btn btn-primary btn-block" type="submit">
                Đăng nhập
              </button>
            </div>
          </form>

        </div>
        <!-- end card-body -->
      </div>
      <!-- end card -->

      <div class="row mt-3">
        <div class="col-12 text-center">
          <p>
            <nuxt-link to="" class="text-muted ml-1"
              >Quên mật khẩu?</nuxt-link
            >
          </p>
        </div>
        <!-- end col -->
      </div>
      <!-- end row -->
    </div>
    <!-- end col -->
  </div>
  <!-- end row -->
</template>

<script>
export default {
  head() {
    return {
      title: `Quản lý nhân sự - DDIC | Đăng nhập`
    };
  },
  data() {
    return {
      login: {
        email: '',
        password: ''
      }
    };
  },
  layout: "auth",
  auth: 'guest',
  methods: {
    toggleVisibility() {
      let x = document.getElementById("password");
      if (x.type === "password") {
        x.type = "text";
      } else {
        x.type = "password";
      }
    },
    async userLogin() {
      try {
        await this.$auth.loginWith('local', { data: this.login })
        this.$toast.success('Đăng nhập thành công!', {
          icon: 'check'
        })
      } catch (error) {
        this.$toast.error('Đăng nhập lỗi! Vui lòng kiểm tra lại tài khoản', {
          icon: 'alert'
        })
      }
    }
  }
};
</script>
