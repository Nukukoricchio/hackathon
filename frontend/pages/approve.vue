<template>
  <div>
    <PageHeader :title="title" :items="items" />
    <div class="row">
      <div class="col">
        <div class="mb-3">
          <label for="formdepartment">Phòng ban:</label>
          <multiselect
            id="formdepartment"
            v-model="department"
            :options="departmentOptions"
            class="helo"
          ></multiselect>
        </div>
      </div>
      <div class="col">
        <div class="mb-3">
          <label for="formposition">Chân dung ứng viên:</label>
          <multiselect
            id="formposition"
            v-model="position"
            :options="positionOptions"
            class="helo"
          ></multiselect>
        </div>
      </div>
      <div class="col">
        <div class="mb-3">
          <label for="formposition">Tiêu chí khác:</label>
          <multiselect
            id="formposition"
            :options="[]"
            class="helo"
          ></multiselect>
        </div>
      </div>
      <div class="col">
        <div class="mb-3">
          <label for="cccd_date">Thời gian:</label>
          <b-form-datepicker
            id="cccd_date"
            :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
            locale="vi"
            v-model="date"
          ></b-form-datepicker>
        </div>
      </div>
    </div>
    <div class="text-center mb-3 mt-2">
      <b-button variant="outline-primary" size="sm" @click="getData"
        >Tìm kiếm</b-button
      >
    </div>
    <div class="text-center" v-if="showLoading">
      <b-spinner large type="grow" variant="warning"></b-spinner>
    </div>
    <div class="row" v-if="showDashboard">
      <div class="col-12">
        <div class="card">
          <div class="card-body">
            <div class="row mb-md-2">
              <div class="col-sm-12 col-md-6">
                  <div id="tickets-table_length" class="dataTables_length">
                    <label class="d-inline-flex align-items-center">
                      Hiện&nbsp;
                      <b-form-select v-model="perPage" size="sm" :options="pageOptions">
                      </b-form-select>&nbsp;bản ghi
                    </label>
                  </div>
              </div>
              <!-- Search -->
              <div class="col-sm-12 col-md-6">
                <div
                  id="tickets-table_filter"
                  class="dataTables_filter text-md-right"
                > 
                  <label class="d-inline-flex align-items-center">
                    Tìm:
                    <b-form-input
                      v-model="filter"
                      type="search"
                      placeholder="Tìm kiếm..."
                      class="form-control form-control-sm ml-2"
                    ></b-form-input>
                  </label>
                </div>
              </div>
              <!-- End search -->
            </div>
            <!-- Table -->
            <div class="table-responsive mb-0">
              <b-table
                class="table table-centered table-nowrap"
                :items="candidateList"
                :fields="fields"
                responsive="sm"
                :per-page="perPage"
                :current-page="currentPage"
                :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc"
                :filter="filter"
                :filter-included-fields="filterOn"
                @filtered="onFiltered"
              >
                <template v-slot:cell(id)="data">
                  <span class="text-body">{{ data.index + 1 }}</span>
                </template>
                <template v-slot:cell(info_email)="data">
                  <img
                    v-if="data.item.info_picture"
                    :src="data.item.info_picture"
                    alt='duaofaf'
                    class="avatar-xs rounded-circle me-2"
                  />
                  <div
                    v-if="!data.item.info_picture"
                    class="avatar-xs d-inline-block me-2"
                  >
                    <div
                      class="avatar-title bg-soft-primary rounded-circle text-primary"
                    >
                      <i class="mdi mdi-account-circle m-0"></i>
                    </div>
                  </div>
                  <nuxt-link :to="'/candidate/' + data.item.id" class="text-body">{{ data.item.info_email }}</nuxt-link>
                </template>
              </b-table>
            </div>
            <div class="row">
              <div class="col">
                <div
                  class="dataTables_paginate paging_simple_numbers float-right"
                >
                  <ul class="pagination pagination-rounded mb-0">
                    <!-- pagination -->
                    <b-pagination
                      v-model="currentPage"
                      :total-rows="rows"
                      :per-page="perPage"
                    ></b-pagination>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";
import PulseLoader from 'vue-spinner/src/PulseLoader.vue'

export default {
  head() {
    return {
      title: `${this.title} | Yody`,
    };
  },
  components: {
    Multiselect,
    PulseLoader
  },
  data() {
    return {
      title: "Danh sách ứng viên",
      items: [
        {
          text: "Ứng viên",
        },
        {
          text: "Danh sách",
          active: true,
        },
      ],
      department: null,
      departmentOptions: [],
      departmentToId: {},
      position: null,
      positionOptions: [],
      date: null,
      candidateList: [],
      showDashboard: false,
      showLoading: false,
      totalRows: 1,
      currentPage: 1,
      perPage: 10,
      pageOptions: [10, 25, 50, 100],
      filter: null,
      filterOn: [],
      sortBy: "age",
      sortDesc: false,
      fields: [
        {
          key: "id",
          label: 'STT'
        },
        {
          key: "info_email",
          label: 'Email'
        },
        {
          key: "info_name",
          label: 'Họ và tên'
        },
        {
          key: "info_phone",
          label: 'Số điện thoại'
        },
        {
          key: "gender_name",
          label: 'Giới tính'
        },
        {
          key: 'info_birthdate',
          label: 'Ngày sinh'
        },
      ],
    };
  },
  async created() {
    await this.getOptions();
  },
  computed: {
    /**
     * Total no. of records
     */
    rows() {
      return this.candidateList.length;
    },
  },
  mounted() {
    // Set the initial number of items
    this.totalRows = this.items.length;
  },
  watch: {
    async department() {
      if (this.department) {
        try {
          this.position = null;
          this.positionOptions = [];
          let response = await this.$axios.get(
            "/api/services/department/" + this.departmentToId[this.department] + "/"
          );
          for (let item of response.data.positions) {
            this.positionOptions.push(item.name);
          }
          if (this.positionOptions.length > 0) this.position = this.positionOptions[0]
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
      } else {
        this.position = null;
        this.positionOptions = [];
      }
    },
  },
  methods: {
    /**
     * Search the table data with search input
     */
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    getCurrentCandidate(item) {
      this.currentCandidate = item;
    },
    async getData() {
      this.showDashboard = false;
      if (!this.position) {
        this.$toast.error("Chưa chọn chân dung ứng viên!", {
          icon: "alert",
        });
      } else {
        try {
          let data = {
            position: this.position
          };
          this.showLoading = true
          console.log('dataa ', this.showLoading)
          let response = await this.$axios.post(
            "/api/candidate/rank/",
            data
          );
          this.candidateList = response.data
          this.showDashboard = true
          this.showLoading = false
        } catch (error) {
          if (error.response.status == 400) {
            let errors = error.response.data;
            // Toast errors
            for (let err in errors) {
              this.$toast.error(err + " : " + errors[err], {
                icon: "alert",
              });
            }
          } else if (error.response.status == 404) {
            this.$toast.error("Chưa có hợp đồng!", {
              icon: "alert",
            });
          } else {
            this.$toast.error("Đã có lỗi xảy ra", {
              icon: "alert",
            });
          }
        }
      }
    },
    async getOptions() {
      try {
        this.departmentOptions = []
        this.departmentToId = {}
        let response = await this.$axios.get('/api/services/department/')
        for (let item of response.data) {
          this.departmentOptions.push(item.name)
          this.departmentToId[item.name] = item.id
        }
        this.department = this.departmentOptions[0]
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
    },
    async getCandidate() {
      try {
        let response = await this.$axios.get('/api/candidate/list/')
        this.candidateList = response.data
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
  },
};
</script>

<style scoped>
.text-body:hover {
  color: #FDAF17 !important;
}
</style>

