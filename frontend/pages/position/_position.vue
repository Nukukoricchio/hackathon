<template>
  <div>
    <PageHeader :title="title" :items="items" />
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
                  <b-button variant="outline-primary" v-b-modal.modal-add
                    ><i class="fas fa-plus-circle font-size-18 mr-1"></i>Thêm tiêu chí
                    </b-button
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
                :items="criteriaList"
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
                <template v-slot:cell(action)="data">
                  <ul class="list-inline mb-0">
                    <li class="list-inline-item">
                      <span
                        class="px-2 text-primary"
                        v-b-tooltip.hover
                        title="Cập nhật"
                      >
                        <i
                          v-b-modal.modal-edit
                          class="fas fa-edit font-size-18"
                          @click="getCurrentCriteria(data.item)"
                        ></i>
                      </span>
                    </li>
                    <li class="list-inline-item">
                      <span
                        class="px-2 text-danger"
                        v-b-tooltip.hover
                        title="Xóa"
                      >
                        <i v-b-modal.modal-delete class="fas fa-trash-alt font-size-18"
                        @click="getCurrentCriteria(data.item)"></i>
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
    <b-modal
      id="modal-add"
      title="Thêm tiêu chí"
      title-class="font-18"
      @show="resetAddModal"
      @ok="handleAddOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleAddSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="formmessage">Tiêu chí:</label>
                      <textarea
                        id="formmessage"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập mô tả về tiêu chí ..."
                        v-model="newAddCriteria.rule"
                      ></textarea>
                    </div>
                  </div>
                </div>
              </form>
            </div>
            <!-- end card-body -->
          </div>
          <!-- end card -->
        </div>
        <!-- end col -->
      </div>
    </b-modal>

    <b-modal
      id="modal-edit"
      title="Cập nhật tiêu chí"
      title-class="font-18"
      @show="resetEditModal"
      @ok="handleEditOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleEditSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="formmessage">Tiêu chí:</label>
                      <textarea
                        id="formmessage"
                        class="form-control"
                        rows="3"
                        v-model="newEditCriteria.rule"
                        placeholder="Cập nhật tiêu chí ..."
                      ></textarea>
                    </div>
                  </div>
                </div>
              </form>
            </div>
            <!-- end card-body -->
          </div>
          <!-- end card -->
        </div>
        <!-- end col -->
      </div>
    </b-modal>
    <b-modal id="modal-delete" title="Cảnh báo" title-class="font-18" @ok="handleDeleteOK">
      <h5>Bạn có chắc muốn xóa không?</h5>
      <p>
        Khi đã xóa sẽ không khôi phục dữ liệu được nữa!
      </p>
    </b-modal>
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: `${this.title} | DDIC-HR`,
    };
  },
  async asyncData({params}) {
    const positionId = params.position
    return { positionId }
  },
  data() {
    return {
      title: '',
      items: [
        {
          text: "Vị trí",
          href: "/",
        },
        {
          text: "Tiêu chí",
          active: true,
        },
      ],
      criteriaList: [],
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
          label: "STT",
        },
        {
          key: "rule",
          label: 'Tiêu chí'
        },
        {
          key: "created",
          label: 'Ngày tạo'
        },
        {
          key: "updated",
          label: 'Lần cuối cập nhật'
        },
        {
          key: "action",
          label: "Tác vụ"
        }
      ],
      currentCriteria: null,
      newAddCriteria: {
        rule: "",
      },
      newEditCriteria: {
        rule: ""
      },
    };
  },
  async created() {
    await this.getPosition()
  },
  computed: {
    /**
     * Total no. of records
     */
    rows() {
      return this.criteriaList.length;
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
    getCurrentCriteria(item) {
      this.currentCriteria = item;
    },
    resetAddModal() {
      this.newAddCriteria.rule = "";
    },
    resetEditModal() {
      this.newEditCriteria.rule = this.currentCriteria.rule;
    },
    async handleAddOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddSubmit();
    },
    async handleEditOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleEditSubmit();
    },
    async handleDeleteOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteSubmit();
    },
    async handleAddSubmit() {
      try {
        let data = {
          rule: this.newAddCriteria.rule,
          position: this.positionId
        }
        await this.$axios.post(
          "/api/services/criteria/",
          data
        );

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add");
        });
        await this.getPosition();
        this.$toast.success("Thêm tiêu chí thành công!", {
          icon: 'check'
        });
      } catch (error) {
        this.$toast.error('Chức vụ đã tồn tại hoặc không hợp lệ!', {
          icon: 'alert'
        })
      }
    },
    async handleEditSubmit() {
      try {
        let url = "/api/services/criteria/" + this.currentCriteria.id + "/";
        await this.$axios.patch(url, this.newEditCriteria);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-edit");
        });
        await this.getPosition();
        this.$toast.success("Cập nhật tiêu chí thành công!", {
          icon: 'check'
        });
      } catch (error) {
        this.$toast.error('Chức vụ đã tồn tại hoặc không hợp lệ!', {
         icon: 'alert'
        })
      }
    },
    async handleDeleteSubmit() {
      try {
        let url = "/api/services/criteria/" + this.currentCriteria.id + "/";
        await this.$axios.delete(url);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete");
        });
        await this.getPosition();
        this.$toast.success("Đã xóa thành công!", {
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
    async getPosition() {
      try {
        let url = "/api/services/position/" + this.positionId + "/";
        let response = await this.$axios.get(url);
        this.criteriaList = response.data.criterias;
        this.title = response.data.name
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
  },
};
</script>

<style scoped>
.text-body:hover {
  color: #FDAF17 !important;
}
</style>
