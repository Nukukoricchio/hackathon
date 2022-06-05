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
          <label>Trạng thái:</label>
          <multiselect
            id="formposition"
            v-model="state"
            :options="['Đã duyệt', 'Chưa duyệt']"
            class="helo"
          ></multiselect>
        </div>
      </div>
    </div>
    <div class="row">
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
                  <button type="button" class="btn btn-success" v-b-tooltip.hover title="Tải CV lên hệ thống" @click="uploadFile">
                    <i class="fas fa-file-upload"></i>
                  </button>
                  <input ref="file" type="file" style="display:none" multiple @change="uploadFileSubmit" />
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
                <template v-slot:cell(role)="data">
                  <ul>
                    <li v-for="(r, index) in data.item.role" :key="index">{{ r.role_name }}</li>
                  </ul>
                </template>
                <template v-slot:cell(action)="data">
                  <ul class="list-inline mb-0">
                    <li class="list-inline-item">
                      <span
                        class="px-2 text-danger"
                        v-b-tooltip.hover
                        title="Xóa hồ sơ ứng viên"
                      >
                        <i v-b-modal.modal-delete class="fas fa-trash-alt font-size-18"
                        @click="getCurrentCandidate(data.item)"></i>
                      </span>
                    </li>
                  </ul>
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
    <b-modal id="modal-delete" title="Cảnh báo" title-class="font-18" @ok="handleDeleteOK">
      <h5>Bạn có chắc muốn xóa hồ sơ ứng viên này không?</h5>
      <p>
        Khi đã xóa thì sẽ không khôi phục dữ liệu được nữa!
      </p>
    </b-modal>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";

export default {
  head() {
    return {
      title: `${this.title} | Yody`,
    };
  },
  components: {
    Multiselect,
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
      state: null,
      candidateList: [],
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
        {
          key: 'action',
          label: 'Tác vụ'
        }
      ],
      currentCandidate: '',
      firstOfficeOptions: [],
      secondOfficeOptions: [],
      readyOtOptions: [
        'Có',
        'Không'
      ],
      readyOtChoices: {
        'Có': true,
        'Không': false
      },
      newSubmitCandidate: {
        first_office: '',
        second_office: '',
        time_to_first_office: '',
        time_to_second_office: '',
        height: '',
        weight: '',
        ready_ot: '',
        file: null
      },
    };
  },
  async created() {
    await this.getCandidate();
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
    async resetAddModal() {
      await this.getOfficeOptions()

      this.newSubmitCandidate.first_office = this.firstOfficeOptions[0]
      this.newSubmitCandidate.second_office = this.secondOfficeOptions[1]
      this.newSubmitCandidate.time_to_first_office = ''
      this.newSubmitCandidate.time_to_second_office = ''
      this.newSubmitCandidate.height = ''
      this.newSubmitCandidate.weight = ''
      this.newSubmitCandidate.ready_ot = this.readyOtOptions[0]
      this.newSubmitCandidate.file = null
    },
    async handleAddOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddSubmit();
    },
    async handleDeleteOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteSubmit();
    },
    async handleAddSubmit() {
      try {
        let formData = new FormData();
        formData.append('first_office', this.newSubmitCandidate.first_office)
        formData.append('second_office', this.newSubmitCandidate.second_office)
        formData.append('time_to_first_office', this.newSubmitCandidate.time_to_first_office)
        formData.append('time_to_second_office', this.newSubmitCandidate.time_to_second_office)
        formData.append('height', this.newSubmitCandidate.height)
        formData.append('weight', this.newSubmitCandidate.weight)
        formData.append("ready_ot", this.readyOtChoices[this.newSubmitCandidate.ready_ot]);
        if (this.newSubmitCandidate.file) formData.append("file", this.newSubmitCandidate.file);

        await this.$axios.post("/api/candidate/submit/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add");
        });
        await this.getCandidate();
        this.$toast.success("Thực hiện thao tác ứng tuyển thành công!", {
          icon: "check",
        });
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
    async handleDeleteSubmit() {
      try {
        await this.$axios.delete("/api/candidate/" + this.currentCandidate.id);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete");
        });
        await this.getCandidate()
        this.$toast.success("Đã xóa hồ sơ thành công!", {
          icon: 'check'
        });
      } catch (error) {
        if (error.response.status == 400) {
          let errors = error.response.data;
          // Toast errors
          for (let err in errors) {
            this.$toast.error(err + " : " + errors[err], {
              icon: 'alert'
            });
          }
        } else {
          this.$toast.error('Đã có lỗi xảy ra', {
            icon: 'alert'
          })
        }
      }
    },
    async getOfficeOptions() {
      try {
        this.firstOfficeOptions = []
        this.secondOfficeOptions = []
        let response = await this.$axios.get('/api/services/office/')
        for (let office of response.data) {
          this.firstOfficeOptions.push(office.name)
          this.secondOfficeOptions.push(office.name)
        }
      } catch (error) {
        if (error.response.status == 400) {
          let errors = error.response.data;
          // Toast errors
          for (let err in errors) {
            this.$toast.error(err + " : " + errors[err], {
              icon: 'alert'
            });
          }
        } else {
          this.$toast.error('Đã có lỗi xảy ra', {
            icon: 'alert'
          })
        }
      }
    },
    uploadFile() {
      this.$refs.file.click()
    },
    async uploadFileSubmit() {
      try {
        let formData = new FormData()
        let file = this.$refs.file
        file.files.forEach(f => {
          formData.append("files", f);
        });
        await this.$axios.post("/api/candidate/upload/", formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        await this.getCandidate()
        this.$toast.success('Tải CV lên hệ thống thành công!', {
          icon: 'check'
        })
      } catch (error) {
        if (error.response.status == 400) {
          let errors = error.response.data;
          // Toast errors
          for (let err in errors) {
            this.$toast.error(err + " : " + errors[err], {
              icon: 'alert'
            });
          }
        } else {
          this.$toast.error('Đã có lỗi xảy ra', {
            icon: 'alert'
          })
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

