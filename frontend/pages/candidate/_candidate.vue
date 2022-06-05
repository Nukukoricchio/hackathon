<template>
  <div>
    <PageHeader :title="title" :items="items" />

    <div class="row mb-4">
      <div class="col-4" v-if="!zoom">
        <div class="card h-100">
          <div class="card-body">
            <div class="text-center">
              <div v-if="candidate.info_picture">
                <img
                  :src="candidate.info_picture"
                  alt
                  class="avatar-lg rounded-circle img-thumbnail"
                />
              </div>
              <div
                v-else
                class="avatar-lg d-inline-block me-2"
              >
                <div
                  class="avatar-title bg-soft-primary rounded-circle text-primary"
                >
                  <i class="mdi mdi-candidate-circle m-0"></i>
                </div>
              </div>
              <h5 class="mt-3 mb-1">{{ candidate.info_email }}</h5>
            </div>

            <hr class="my-4" />

            <div class="text-muted">
              <div class="table-responsive mt-1 mb-0">
                <div>
                  <span class="mb-1">Họ và tên :</span>
                  <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.info_name }}</h5>
                </div>
                <div>
                  <span class="mb-1">Số điện thoại :</span>
                  <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.info_phone }}</h5>
                </div>
                <div>
                  <span class="mb-1">Ngày sinh :</span>
                  <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.info_birthdate }}</h5>
                </div>
                <div>
                  <span class="mb-1">Giới tính :</span>
                  <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.info_gender }}</h5>
                </div>
                <div>
                  <span class="mb-1">Địa chỉ:</span>
                  <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.info_location_1 }}</h5>
                </div>
                <div class="text-center mt-3 pt-2">
                  <button type="button" class="btn btn-success" v-b-modal.modal-approve v-show="candidate.is_approved == false">Duyệt</button>
                  <button type="button" class="btn btn-danger" v-b-modal.modal-ban v-show="candidate.is_approved == true">Hủy duyệt</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div :class="[ zoom ? 'col-12' : 'col-8' ]">
        <div class="card mb-0">
          <b-tabs content-class="p-4" justified class="nav-tabs-custom">
            <a href="javascript: void(0);" v-if="!zoom">
              <i class="fas fa-expand-arrows-alt font-size-20 zoom-icon" @click="toggleZoom"></i>
            </a>
            <a href="javascript: void(0);" v-else>
              <i class="fas fa-compress-arrows-alt font-size-20 zoom-icon" @click="toggleZoom"></i>
            </a>
            <b-tab active>
              <template v-slot:title>
                <i class="fas fa-book-reader font-size-20"></i>
                <span class="d-none d-sm-block">Thông tin bổ sung</span>
              </template>
              <div>
                <div>
                  <div class="table-responsive mt-1 mb-0">
                    <div>
                      <span class="mb-1">Văn phòng ứng tuyển(ưu tiên số 1):</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.first_office }}</h5>
                    </div>
                    <div>
                      <span class="mb-1">Văn phòng ứng tuyển(ưu tiên số 2):</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.second_office }}</h5>
                    </div>
                    <div>
                      <span class="mb-1">Khoảng cách di chuyển đến văn phòng ứng tuyển ưu tiên số 1:</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.time_to_first_office ? candidate.time_to_first_office : '' }}</h5>
                    </div>
                    <div>
                      <span class="mb-1">Khoảng cách di chuyển đến văn phòng ứng tuyển ưu tiên số 2:</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.time_to_second_office ? candidate.time_to_second_office : '' }}</h5>
                    </div>
                    <div>
                      <span class="mb-1">Văn phòng ứng tuyển(ưu tiên số 2):</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.second_office }}</h5>
                    </div>
                    <div>
                      <span class="mb-1">Chiều cao:</span>
                      <h5 class="font-size-16 ml-2" style="display:inline" v-if="candidate.height">{{ candidate.height }} cm</h5>
                    </div>
                    <div>
                      <span class="mb-1">Cân nặng :</span>
                      <h5 class="font-size-16 ml-2" style="display:inline" v-if="candidate.weight">{{ candidate.weight }} kg</h5>
                    </div>
                    <div>
                      <span class="mb-1">Sẵn sàng làm việc xoay ca:</span>
                      <h5 class="font-size-16 ml-2" style="display:inline">{{ candidate.ready_ot ? 'Có': 'Không' }}</h5>
                    </div>
                  </div>
                </div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class="fas fa-calendar-alt font-size-20"></i>
                <span class="d-none d-sm-block">Kinh nghiệm</span>
              </template>
              <div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class="fas fa-graduation-cap font-size-20"></i>
                <span class="d-none d-sm-block">Trình độ học vấn</span>
              </template>
              <div>
                <div>
                  <div class="table-responsive">
                  </div>
                </div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class="fas fa-file-pdf font-size-20"></i>
                <span class="d-none d-sm-block">Tài liệu</span>
              </template>
              <div>
                <div class="table-responsive">
                  <table class="table table-nowrap table-hover mb-0">
                    <thead>
                      <tr>
                        <th scope="col">STT</th>
                        <th scope="col">File tài liệu</th>
                        <th scope="col">Tác vụ</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr v-for="(value, index) in files" :key="index">
                        <th scope="row">{{ index+1 }}</th>
                        <td v-if="value.file"><a :href="value.file">{{ value.file.split('/').pop() }}</a></td>
                        <td>
                          <span
                            class="px-1 text-primary"
                            v-b-tooltip.hover
                            title="Cập nhật"
                          >
                            <i
                              v-b-modal.modal-edit-member
                              class="fas fa-edit font-size-18"
                              @click="getCurrentMember(value)"
                            ></i>
                          </span>
                          <span
                            class="px-1 text-danger"
                            v-b-tooltip.hover
                            title="Xóa"
                          >
                            <i v-b-modal.modal-delete-member class="fas fa-trash-alt font-size-18"
                            @click="getCurrentMember(value)"></i>
                          </span>
                        </td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </b-tab>
          </b-tabs>
          <!-- Nav tabs -->
          <!-- Tab content -->
        </div>
      </div>
    </div>
    <!-- end row -->
    <b-modal id="modal-approve" title="Thông báo" title-class="font-18" @ok="handleApproveOK">
      <h5>Duyệt hồ sơ ứng viên?</h5>
    </b-modal>
    <b-modal id="modal-ban" title="Thông báo" title-class="font-18" @ok="handleBanOK">
      <h5>Hủy duyệt hồ sơ ứng viên?</h5>
    </b-modal>
  </div>
</template>

<script>
import Multiselect from "vue-multiselect";
import "vue-multiselect/dist/vue-multiselect.min.css";

export default {
  head() {
    return {
      title: `${this.title} | DDIC-HR`,
    };
  },
  components: {
    Multiselect
  },
  async asyncData({params}) {
    const candidateId = params.candidate
    return { candidateId }
  },
  async created() {
    await this.getCandidate()
  },
  data() {
    return {
      title: "Chi tiết hồ sơ ứng viên",
      items: [
        {
          text: "Ứng viên",
        },
        {
          text: "Hồ sơ",
          active: true,
        },
      ],
      candidate: [],
      files: [],
      zoom: false
    };
  },
  methods: {
    toggleZoom() {
      this.zoom = !this.zoom
    },
    async handleApproveOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleApproveSubmit();
    },
    async handleApproveSubmit() {
      try {
        let url = '/api/candidate/' + this.candidateId + '/'
        let data = {
          is_approved: true
        }
        await this.$axios.patch(url, data);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-approve");
        });
        await this.getCandidate();
        this.$toast.success("Duyệt hồ sơ ứng viên thành công!", {
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
    async handleBanOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleBanSubmit();
    },
    async handleBanSubmit() {
      try {
        let url = '/api/candidate/' + this.candidateId + '/'
        let data = {
          is_approved: false
        }
        await this.$axios.patch(url, data);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-ban");
        });
        await this.getCandidate();
        this.$toast.success("Hủy duyệt hồ sơ ứng viên thành công!", {
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
    async getCandidate() {
      try {
        let response = await this.$axios.get('/api/candidate/' + this.candidateId + '/')
        this.candidate = response.data
        this.files = this.candidate.files
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

<style>
.nav-tabs .nav-link.active, .nav-tabs .nav-item.show .nav-link {
  color: #FDAF17 !important;
  border-color: #FDAF17 !important;
  border-left: none !important;
  border-right: none !important;
  border-top: none !important;
}
.zoom-icon {
  position: relative;
  top: -95px;
  left: -30px;
}
</style>
