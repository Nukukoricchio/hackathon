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
              <!-- <div v-if="role.length > 0">
                <h5 class="font-size-16">Chức vụ :</h5>
                <ul>
                  <li v-for="(r, index) in candidate.role" :key="index">{{ r.role_name }}</li>
                </ul>
              </div> -->
              <div class="table-responsive mt-1 mb-0">
                <div>
                  <p class="mb-1">Họ và tên :</p>
                  <h5 class="font-size-16">{{ candidate.info_name }}</h5>
                </div>
                <div>
                  <p class="mb-1">Số điện thoại :</p>
                  <h5 class="font-size-16">{{ candidate.info_phone }}</h5>
                </div>
                <div>
                  <p class="mb-1">Ngày sinh :</p>
                  <h5 class="font-size-16">{{ candidate.info_birthdate }}</h5>
                </div>
                <div>
                  <p class="mb-1">Giới tính :</p>
                  <h5 class="font-size-16">{{ candidate.info_gender }}</h5>
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
                <span class="d-none d-sm-block">Thông tin chung</span>
              </template>
              <div>
                <span
                  class="text-danger float-right"
                  v-b-tooltip.hover
                  title="Xóa"
                  v-show="profile"
                >
                  <i v-b-modal.modal-delete-profile class="fas fa-trash-alt" style="font-size: 20px;"></i>
                </span>
                <span
                  class="text-success float-right mr-2"
                  v-b-tooltip.hover
                  title="Cập nhật thông tin chung"
                  v-show="profile"
                >
                  <i v-b-modal.modal-edit-profile class="far fa-edit" style="font-size: 20px;"></i>
                </span>
                <div v-if="profile">
                  <ul class="activity-feed mb-0 pl-2">
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Mã nhân viên: </span>
                        <span class="font-size-26 font-weight-bold">{{ profile.staff_code }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Cấp bậc:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.get_kind_display }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Giới tính:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.get_gender_display }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Số CCCD/CMT:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.cccd_code }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Ngày cấp CCCD/CMT:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.cccd_date }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Nơi cấp CCCD/CMT:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.cccd_place }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Địa chỉ thường trú:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.cccd_address }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Quê quán:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.cccd_home }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Ngân hàng:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.bank_name }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Số tài khoản ngân hàng:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.bank_number }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Email cá nhân:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.personal_email }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Số sổ BHXH:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.bhxd_code }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Mã số thuế cá nhân:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.taxt_code }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">Quốc tịch:</span>
                        <span class="font-size-26 font-weight-bold">{{ profile.nation }}</span>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">File scan CCCD/CMT:</span>
                        <a :href="'http://192.168.9.84:8000' + profile.cccd_file" 
                        class="font-size-26 font-weight-bold" v-if="profile.cccd_file">Tải xuống</a>
                      </div>
                    </li>
                    <li class="feed-item">
                      <div class="feed-item-list">
                        <span class="font-size-26 mr-2">File scan BHXH:</span>
                        <a :href="'http://192.168.9.84:8000' + profile.bhxh_file"
                        class="font-size-26 font-weight-bold" v-if="profile.bhxh_file"
                        >Tải xuống</a>
                      </div>
                    </li>
                  </ul>
                </div>
                <div v-else>
                  <span
                    class="text-success float-right"
                    v-b-tooltip.hover
                    title="Thêm thông tin chung"
                  >
                    <i v-b-modal.modal-add-profile class="fas fa-plus-square" style="font-size: 20px;"></i>
                  </span>
                </div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class="fas fa-calendar-alt font-size-20"></i>
                <span class="d-none d-sm-block">GĐ làm việc</span>
              </template>
              <div v-if="profile">
                <div>
                  <div>
                    <span
                      class="text-success float-right"
                      v-b-tooltip.hover
                      title="Thêm giai đoạn làm việc"
                    >
                      <i v-b-modal.modal-add-work class="fas fa-plus-square" style="font-size: 20px;"></i>
                    </span>
                  </div>
                </div>

                <div>
                  <div class="table-responsive">
                    <table class="table table-nowrap table-hover mb-0">
                      <thead>
                        <tr>
                          <th scope="col">STT</th>
                          <th scope="col">Ngày bđ thử việc</th>
                          <th scope="col">Ngày bđ LVCT</th>
                          <th scope="col">Ngày bđ nghỉ việc</th>
                          <th scope="col">Loại HĐLĐ</th>
                          <th scope="col">File CV</th>
                          <th scope="col">File BC</th>
                          <th scope="col">File SYLL</th>
                          <th scope="col">Giấy KSK</th>
                          <th scope="col">Hộ khẩu</th>
                          <th scope="col">Tác vụ</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(value, index) in workStages" :key="index">
                          <th scope="row">{{ index+1 }}</th>
                          <td>{{ value.pre_date ? value.pre_date : '' }}</td>
                          <td>{{ value.in_date ? value.in_date : '' }}</td>
                          <td>{{ value.out_date ? value.out_date : '' }}</td>
                          <td>
                            <span class="badge bg-soft-primary font-size-12"
                              >{{ value.get_kind_display }}</span
                            >
                          </td>
                          <td v-if="value.cv_file"><a :href="'http://192.168.9.84:8000' + value.cv_file">Xem</a></td>
                          <td v-else></td>
                          <td v-if="value.level_file"><a :href="'http://192.168.9.84:8000' + value.level_file">Xem</a></td>
                          <td v-else></td>
                          <td v-if="value.syll_file"><a :href="'http://192.168.9.84:8000' + value.syll_file">Xem</a></td>
                          <td v-else></td>
                          <td v-if="value.ksk_file"><a :href="'http://192.168.9.84:8000' + value.ksk_file">Xem</a></td>
                          <td v-else></td>
                          <td v-if="value.hk_file"><a :href="'http://192.168.9.84:8000' + value.hk_file">Xem</a></td>
                          <td v-else></td>
                          <td>
                            <span
                              class="px-1 text-primary"
                              v-b-tooltip.hover
                              title="Cập nhật"
                            >
                              <i
                                v-b-modal.modal-edit-work
                                class="fas fa-edit font-size-18"
                                @click="getCurrentWorkStage(value)"
                              ></i>
                            </span>
                            <span
                              class="px-1 text-danger"
                              v-b-tooltip.hover
                              title="Xóa"
                            >
                              <i v-b-modal.modal-delete-work class="fas fa-trash-alt font-size-18"
                              @click="getCurrentWorkStage(value)"></i>
                            </span>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class=" fas fa-file-alt font-size-20"></i>
                <span class="d-none d-sm-block">Bằng cấp</span>
              </template>
              <div v-if="profile">
                <div>
                  <div>
                    <span
                      class="text-success float-right"
                      v-b-tooltip.hover
                      title="Thêm bằng cấp"
                    >
                      <i v-b-modal.modal-add-education class="fas fa-plus-square" style="font-size: 20px;"></i>
                    </span>
                  </div>
                </div>

                <div>
                  <div class="table-responsive">
                    <table class="table table-nowrap table-hover mb-0">
                      <thead>
                        <tr>
                          <th scope="col">STT</th>
                          <th scope="col">Tốt nghiệp trường</th>
                          <th scope="col">Chuyên ngành</th>
                          <th scope="col">Năm tốt nghiệp</th>
                          <th scope="col">Trình độ</th>
                          <th scope="col">Bằng cấp</th>
                          <th scope="col">File bằng cấp</th>
                          <th scope="col">Tác vụ</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(value, index) in educations" :key="index">
                          <th scope="row">{{ index+1 }}</th>
                          <td>{{ value.school }}</td>
                          <td>{{ value.major }}</td>
                          <td>{{ value.graduated_year }}</td>
                          <td>
                            <span class="badge bg-soft-primary font-size-12"
                              >{{ value.get_degree_display }}</span
                            >
                          </td>
                          <td>
                            <span class="badge bg-soft-success font-size-12"
                              >{{ value.get_level_display }}</span
                            >
                          </td>
                          <td v-if="value.level_file"><a :href="'http://192.168.9.84:8000' + value.level_file">Xem</a></td>
                          <td v-else></td>
                          <td>
                            <span
                              class="px-1 text-primary"
                              v-b-tooltip.hover
                              title="Cập nhật"
                            >
                              <i
                                v-b-modal.modal-edit-education
                                class="fas fa-edit font-size-18"
                                @click="getCurrentEducation(value)"
                              ></i>
                            </span>
                            <span
                              class="px-1 text-danger"
                              v-b-tooltip.hover
                              title="Xóa"
                            >
                              <i v-b-modal.modal-delete-education class="fas fa-trash-alt font-size-18"
                              @click="getCurrentEducation(value)"></i>
                            </span>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </b-tab>
            <b-tab>
              <template v-slot:title>
                <i class=" fas fa-child font-size-20"></i>
                <span class="d-none d-sm-block">Gia đình</span>
              </template>
              <div v-if="profile">
                <div>
                  <div>
                    <span
                      class="text-success float-right"
                      v-b-tooltip.hover
                      title="Thêm thành viên gia đình"
                    >
                      <i v-b-modal.modal-add-member class="fas fa-plus-square" style="font-size: 20px;"></i>
                    </span>
                  </div>
                </div>

                <div>
                  <div class="table-responsive">
                    <table class="table table-nowrap table-hover mb-0">
                      <thead>
                        <tr>
                          <th scope="col">STT</th>
                          <th scope="col">Họ và tên</th>
                          <th scope="col">Giới tính</th>
                          <th scope="col">Ngày sinh</th>
                          <th scope="col">Giấy khai sinh</th>
                          <th scope="col">Tác vụ</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr v-for="(value, index) in members" :key="index">
                          <th scope="row">{{ index+1 }}</th>
                          <td>{{ value.name }}</td>
                          <td>
                            <span class="badge bg-soft-primary font-size-12"
                              >{{ value.get_gender_display }}</span
                            >
                          </td>
                          <td>{{ value.birth_day ? value.birth_day : '' }}</td>
                          <td v-if="value.birth_file"><a :href="'http://192.168.9.84:8000' + value.birth_file">Xem</a></td>
                          <td v-else></td>
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
              </div>
            </b-tab>
          </b-tabs>
          <!-- Nav tabs -->
          <!-- Tab content -->
        </div>
      </div>
    </div>
    <!-- end row -->
    <b-modal
      id="modal-add-profile"
      title="Tạo mới thông tin chung"
      title-class="font-18"
      @show="resetAddProfileModal"
      @ok="handleAddProfileOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleAddProfileSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="staff_code">Mã nhân viên:</label>
                      <input
                        id="staff_code"
                        type="text"
                        class="form-control"
                        placeholder="Nhập mã nhân viên ..."
                        v-model="newAddProfile.staff_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Cấp bậc:</label>
                      <multiselect v-model="newAddProfile.kind" :options="profileKindOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label>Giới tính:</label>
                      <multiselect v-model="newAddProfile.gender" :options="genderOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_code">Số CCCD/CMT:</label>
                      <input
                        id="cccd_code"
                        type="text"
                        class="form-control"
                        placeholder="Nhập số CCCD/CMT ..."
                        v-model="newAddProfile.cccd_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày cấp CCCD/CMT:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newAddProfile.cccd_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_place">Nơi cấp CCCD/CMT:</label>
                      <textarea
                        id="cccd_place"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập nơi cấp CCCD/CMT ..."
                        v-model="newAddProfile.cccd_place"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_address">Địa chỉ thường trú:</label>
                      <textarea
                        id="cccd_address"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập địa chỉ thường trú ..."
                        v-model="newAddProfile.cccd_address"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_home">Quê quán:</label>
                      <textarea
                        id="cccd_home"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập quê quán ..."
                        v-model="newAddProfile.cccd_home"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="bank_name">Tên ngân hàng:</label>
                      <input
                        id="bank_name"
                        type="text"
                        class="form-control"
                        placeholder="Nhập tên ngân hàng ..."
                        v-model="newAddProfile.bank_name"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="bank_number">Số tài khoản ngân hàng:</label>
                      <input
                        id="bank_number"
                        type="text"
                        class="form-control"
                        placeholder="Nhập số tài khoản ngân hàng ..."
                        v-model="newAddProfile.bank_number"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="personal_email">Email cá nhân:</label>
                      <input
                        id="personal_email"
                        type="email"
                        class="form-control"
                        placeholder="Nhập email cá nhân ..."
                        v-model="newAddProfile.personal_email"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="bhxd_code">Số sổ BHXH:</label>
                      <input
                        id="bhxd_code"
                        type="text"
                        class="form-control"
                        placeholder="Nhập số sổ BHXH ..."
                        v-model="newAddProfile.bhxd_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="taxt_code">Mã số thuế cá nhân:</label>
                      <input
                        id="taxt_code"
                        type="text"
                        class="form-control"
                        placeholder="Nhập mã số thuế cá nhân ..."
                        v-model="newAddProfile.taxt_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="nation">Quốc tịch:</label>
                      <input
                        id="nation"
                        type="text"
                        class="form-control"
                        placeholder="Nhập quốc tịch ..."
                        v-model="newAddProfile.nation"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="cccd_file">File scan CCCD/CMT:</label>
                      <b-form-file
                        id="cccd_file"
                        v-model="newAddProfile.cccd_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="bhxh_file">File scan BHXH:</label>
                      <b-form-file
                        id="bhxh_file"
                        v-model="newAddProfile.bhxh_file"
                        plain
                      ></b-form-file>
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
      id="modal-edit-profile"
      title="Cập nhật thông tin chung"
      title-class="font-18"
      @show="resetEditProfileModal"
      @ok="handleEditProfileOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleEditProfileSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="staff_code">Mã nhân viên:</label>
                      <input
                        id="staff_code"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật mã nhân viên ..."
                        v-model="newEditProfile.staff_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Cấp bậc:</label>
                      <multiselect v-model="newEditProfile.kind" :options="profileKindOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label>Giới tính:</label>
                      <multiselect v-model="newEditProfile.gender" :options="genderOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_code">Số CCCD/CMT:</label>
                      <input
                        id="cccd_code"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật số CCCD/CMT ..."
                        v-model="newEditProfile.cccd_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày cấp CCCD/CMT:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newEditProfile.cccd_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_place">Nơi cấp CCCD/CMT:</label>
                      <textarea
                        id="cccd_place"
                        class="form-control"
                        rows="3"
                        placeholder="Cập nhật nơi cấp CCCD/CMT ..."
                        v-model="newEditProfile.cccd_place"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_address">Địa chỉ thường trú:</label>
                      <textarea
                        id="cccd_address"
                        class="form-control"
                        rows="3"
                        placeholder="Cập nhật địa chỉ thường trú ..."
                        v-model="newEditProfile.cccd_address"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_home">Quê quán:</label>
                      <textarea
                        id="cccd_home"
                        class="form-control"
                        rows="3"
                        placeholder="Cập nhật quê quán ..."
                        v-model="newEditProfile.cccd_home"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="bank_name">Tên ngân hàng:</label>
                      <input
                        id="bank_name"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật tên ngân hàng ..."
                        v-model="newEditProfile.bank_name"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="bank_number">Số tài khoản ngân hàng:</label>
                      <input
                        id="bank_number"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật số tài khoản ngân hàng ..."
                        v-model="newEditProfile.bank_number"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="personal_email">Email cá nhân:</label>
                      <input
                        id="personal_email"
                        type="email"
                        class="form-control"
                        placeholder="Cập nhật email cá nhân ..."
                        v-model="newEditProfile.personal_email"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="bhxd_code">Số sổ BHXH:</label>
                      <input
                        id="bhxd_code"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật số sổ BHXH ..."
                        v-model="newEditProfile.bhxd_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="taxt_code">Mã số thuế cá nhân:</label>
                      <input
                        id="taxt_code"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật mã số thuế cá nhân ..."
                        v-model="newEditProfile.taxt_code"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="nation">Quốc tịch:</label>
                      <input
                        id="nation"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật quốc tịch ..."
                        v-model="newEditProfile.nation"
                      />
                    </div>
                    <div class="mb-3">
                      <label for="cccd_file">File scan CCCD/CMT:</label>
                      <b-form-file
                        id="cccd_file"
                        v-model="newEditProfile.cccd_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="bhxh_file">File scan BHXH:</label>
                      <b-form-file
                        id="bhxh_file"
                        v-model="newEditProfile.bhxh_file"
                        plain
                      ></b-form-file>
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
    <b-modal id="modal-delete-profile" title="Cảnh báo" title-class="font-18" @ok="handleDeleteProfileOK">
      <h5>Bạn có chắc muốn xóa không?</h5>
      <p>
        Khi đã xóa sẽ không khôi phục dữ liệu được nữa!
      </p>
    </b-modal>
    <b-modal
      id="modal-add-work"
      title="Tạo mới giai đoạn làm việc"
      title-class="font-18"
      @show="resetAddWorkStageModal"
      @ok="handleAddWorkStageOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleAddWorkStageSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu thử việc:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newAddWorkStage.pre_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu làm việc chính thức:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newAddWorkStage.in_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu nghỉ việc:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newAddWorkStage.out_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label>Loại hợp đồng lao động:</label>
                      <multiselect v-model="newAddWorkStage.kind" :options="workStageKindOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="cv_file">File CV:</label>
                      <b-form-file
                        id="cv_file"
                        v-model="newAddWorkStage.cv_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="level_file">File bằng cấp:</label>
                      <b-form-file
                        id="level_file"
                        v-model="newAddWorkStage.level_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="syll_file">Sơ yếu lý lịch xác nhận địa phương:</label>
                      <b-form-file
                        id="syll_file"
                        v-model="newAddWorkStage.syll_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="ksk_file">Giấy ksk:</label>
                      <b-form-file
                        id="ksk_file"
                        v-model="newAddWorkStage.ksk_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="hk_file">Hộ khẩu:</label>
                      <b-form-file
                        id="hk_file"
                        v-model="newAddWorkStage.hk_file"
                        plain
                      ></b-form-file>
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
      id="modal-edit-work"
      title="Cập nhật giai đoạn làm việc"
      title-class="font-18"
      @show="resetEditWorkStageModal"
      @ok="handleEditWorkStageOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleEditWorkStageSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu thử việc:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newEditWorkStage.pre_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu làm việc chính thức:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newEditWorkStage.in_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="cccd_date">Ngày bắt đầu nghỉ việc:</label>
                      <b-form-datepicker
                        id="cccd_date"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newEditWorkStage.out_date"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label>Loại hợp đồng lao động:</label>
                      <multiselect v-model="newEditWorkStage.kind" :options="workStageKindOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="cv_file">File CV:</label>
                      <b-form-file
                        id="cv_file"
                        v-model="newEditWorkStage.cv_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="level_file">File bằng cấp:</label>
                      <b-form-file
                        id="level_file"
                        v-model="newEditWorkStage.level_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="syll_file">Sơ yếu lý lịch xác nhận địa phương:</label>
                      <b-form-file
                        id="syll_file"
                        v-model="newEditWorkStage.syll_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="ksk_file">Giấy ksk:</label>
                      <b-form-file
                        id="ksk_file"
                        v-model="newEditWorkStage.ksk_file"
                        plain
                      ></b-form-file>
                    </div>
                    <div class="mb-3">
                      <label for="hk_file">Hộ khẩu:</label>
                      <b-form-file
                        id="hk_file"
                        v-model="newEditWorkStage.hk_file"
                        plain
                      ></b-form-file>
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
    <b-modal id="modal-delete-work" title="Cảnh báo" title-class="font-18" @ok="handleDeleteWorkStageOK">
      <h5>Bạn có chắc muốn xóa không?</h5>
      <p>
        Khi đã xóa sẽ không khôi phục dữ liệu được nữa!
      </p>
    </b-modal>
    <b-modal
      id="modal-add-education"
      title="Tạo mới bằng cấp"
      title-class="font-18"
      @show="resetAddEducationModal"
      @ok="handleAddEducationOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleAddEducationSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="school">Tốt nghiệp trường:</label>
                      <textarea
                        id="school"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập tên trường..."
                        v-model="newAddEducation.school"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="major">Chuyên ngành:</label>
                      <textarea
                        id="major"
                        class="form-control"
                        rows="3"
                        placeholder="Nhập tên chuyên ngành..."
                        v-model="newAddEducation.major"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="graduated_year">Năm tốt nghiệp:</label>
                      <input
                        id="graduated_year"
                        type="text"
                        class="form-control"
                        placeholder="Nhập năm tốt nghiệp ..."
                        v-model="newAddEducation.graduated_year"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Trình độ:</label>
                      <multiselect v-model="newAddEducation.degree" :options="degreeOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label>Bằng cấp:</label>
                      <multiselect v-model="newAddEducation.level" :options="levelOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="level_file">File bằng cấp:</label>
                      <b-form-file
                        id="level_file"
                        v-model="newAddEducation.level_file"
                        plain
                      ></b-form-file>
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
      id="modal-edit-education"
      title="Cập nhật bằng cấp"
      title-class="font-18"
      @show="resetEditEducationModal"
      @ok="handleEditEducationOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleEditEducationSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="school">Tốt nghiệp trường:</label>
                      <textarea
                        id="school"
                        class="form-control"
                        rows="3"
                        placeholder="Cập nhật tên trường..."
                        v-model="newEditEducation.school"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="major">Chuyên ngành:</label>
                      <textarea
                        id="major"
                        class="form-control"
                        rows="3"
                        placeholder="Cập nhật tên chuyên ngành..."
                        v-model="newEditEducation.major"
                      ></textarea>
                    </div>
                    <div class="mb-3">
                      <label for="graduated_year">Năm tốt nghiệp:</label>
                      <input
                        id="graduated_year"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật năm tốt nghiệp ..."
                        v-model="newEditEducation.graduated_year"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Trình độ:</label>
                      <multiselect v-model="newEditEducation.degree" :options="degreeOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label>Bằng cấp:</label>
                      <multiselect v-model="newEditEducation.level" :options="levelOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="level_file">File bằng cấp:</label>
                      <b-form-file
                        id="level_file"
                        v-model="newEditEducation.level_file"
                        plain
                      ></b-form-file>
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
    <b-modal id="modal-delete-education" title="Cảnh báo" title-class="font-18" @ok="handleDeleteEducationOK">
      <h5>Bạn có chắc muốn xóa không?</h5>
      <p>
        Khi đã xóa sẽ không khôi phục dữ liệu được nữa!
      </p>
    </b-modal>
    <b-modal
      id="modal-add-member"
      title="Thêm thành viên trong gia đình"
      title-class="font-18"
      @show="resetAddMemberModal"
      @ok="handleAddMemberOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleAddMemberSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="name">Họ và tên thành viên gia đình:</label>
                      <input
                        id="name"
                        type="text"
                        class="form-control"
                        placeholder="Nhập họ và tên thành viên gia đình ..."
                        v-model="newAddMember.name"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Giới tính:</label>
                      <multiselect v-model="newAddMember.gender" :options="genderOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="birth_day">Ngày sinh:</label>
                      <b-form-datepicker
                        id="birth_day"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newAddMember.birth_day"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="birth_file">Giấy khai sinh:</label>
                      <b-form-file
                        id="birth_file"
                        v-model="newAddMember.birth_file"
                        plain
                      ></b-form-file>
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
      id="modal-edit-member"
      title="Cập nhật thành viên trong gia đình"
      title-class="font-18"
      @show="resetEditMemberModal"
      @ok="handleEditMemberOK"
    >
      <div class="row">
        <div class="col-lg-12">
          <div class="card">
            <div class="card-body">
              <form
                class="outer-repeater"
                @submit.stop.prevent="handleEditMemberSubmit"
              >
                <div class="outer">
                  <div class="outer">
                    <div class="mb-3">
                      <label for="name">Họ và tên thành viên gia đình:</label>
                      <input
                        id="name"
                        type="text"
                        class="form-control"
                        placeholder="Cập nhật họ và tên thành viên gia đình ..."
                        v-model="newEditMember.name"
                      />
                    </div>
                    <div class="mb-3">
                      <label>Giới tính:</label>
                      <multiselect v-model="newEditMember.gender" :options="genderOptions" 
                        :multiple="false" :allow-empty="false"></multiselect>
                    </div>
                    <div class="mb-3">
                      <label for="birth_day">Ngày sinh:</label>
                      <b-form-datepicker
                        id="birth_day"
                        :date-format-options="{ year: 'numeric', month: 'numeric', day: 'numeric' }"
                        locale="vi"
                        v-model="newEditMember.birth_day"
                      ></b-form-datepicker>
                    </div>
                    <div class="mb-3">
                      <label for="birth_file">Giấy khai sinh:</label>
                      <b-form-file
                        id="birth_file"
                        v-model="newEditMember.birth_file"
                        plain
                      ></b-form-file>
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
    <b-modal id="modal-delete-member" title="Cảnh báo" title-class="font-18" @ok="handleDeleteMemberOK">
      <h5>Bạn có chắc muốn xóa không?</h5>
      <p>
        Khi đã xóa sẽ không khôi phục dữ liệu được nữa!
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
      role: [],
      profile: null,
      workStages: [],
      educations: [],
      members: [],
      genderOptions: [
        'Nam',
        'Nữ',
        'Khác'
      ],
      genderChoices: {
        'Nam': 'M',
        'Nữ': 'F',
        'Khác': 'O'
      },
      profileKindOptions: [
        'Nhân viên & Chuyên viên',
        'Phó phòng',
        'Trưởng phòng',
        'Phó tổng giám đốc',
        'Tổng giám đốc'
      ],
      profileKindChoices: {
        'Nhân viên & Chuyên viên': '1',
        'Phó phòng': '2',
        'Trưởng phòng': '3',
        'Phó tổng giám đốc': '4',
        'Tổng giám đốc': '5'
      },
      newAddProfile: {
        staff_code: '',
        kind: '',
        gender: '',
        cccd_code: '',
        cccd_date: '',
        cccd_place: '',
        cccd_address: '',
        cccd_home: '',
        bank_name: '',
        bank_number: '',
        personal_email: '',
        bhxd_code: '',
        taxt_code: '',
        nation: '',
        cccd_file: null,
        bhxh_file: null,
      },
      newEditProfile: {
        staff_code: '',
        kind: '',
        gender: '',
        cccd_code: '',
        cccd_date: '',
        cccd_place: '',
        cccd_address: '',
        cccd_home: '',
        bank_name: '',
        bank_number: '',
        personal_email: '',
        bhxd_code: '',
        taxt_code: '',
        nation: '',
        cccd_file: null,
        bhxh_file: null,
      },
      workStageKindOptions: [
        'Hợp đồng thử việc',
        'Hợp đồng xác định thời hạn',
        'Hợp đồng không xác định thời hạn',
        'Hợp đồng dịch vụ',
        'Chưa phân loại'
      ],
      workStageKindChoices: {
        'Hợp đồng thử việc': 'HĐTV',
        'Hợp đồng xác định thời hạn': 'HĐXĐTH',
        'Hợp đồng không xác định thời hạn': 'HĐKXĐTH',
        'Hợp đồng dịch vụ': 'HĐDV',
        'Chưa phân loại': 'CPL'
      },
      newAddWorkStage: {
        pre_date: '',
        in_date: '',
        out_date: '',
        kind: '',
        cv_file: null,
        level_file: null,
        syll_file: null,
        ksk_file: null,
        hk_file: null
      },
      newEditWorkStage: {
        pre_date: '',
        in_date: '',
        out_date: '',
        kind: '',
        cv_file: null,
        level_file: null,
        syll_file: null,
        ksk_file: null,
        hk_file: null
      },
      currentWorkStage: null,
      degreeOptions: [
        'Trung học phổ thông',
        'Trung cấp',
        'Cao đẳng',
        'Đại học',
        'Trên đại học'
      ],
      degreeChoices: {
        'Trung học phổ thông': 'THPT',
        'Trung cấp': 'TC',
        'Cao đẳng': 'CĐ',
        'Đại học': 'ĐH',
        'Trên đại học': 'TĐH'
      },
      levelOptions: [
        'Trung bình',
		    'Trung bình khá',
		    'Khá',
		    'Giỏi'
      ],
      levelChoices: {
        'Trung bình': 'TB',
		    'Trung bình khá': 'TBK',
		    'Khá': 'K',
		    'Giỏi': 'G'
      },
      currentEducation: null,
      newAddEducation: {
        school: '',
        major: '',
        graduated_year: '',
        degree: '',
        level: '',
        level_file: null
      },
      newEditEducation: {
        school: '',
        major: '',
        graduated_year: '',
        degree: '',
        level: '',
        level_file: null
      },
      currentMember: null,
      newAddMember: {
        name: '',
        gender: '',
        birth_day: '',
        birth_file: null
      },
      newEditMember: {
        name: '',
        gender: '',
        birth_day: '',
        birth_file: null
      },
      zoom: false
    };
  },
  methods: {
    toggleZoom() {
      this.zoom = !this.zoom
    },
    getCurrentWorkStage(value) {
      this.currentWorkStage = value
    },
    getCurrentEducation(value) {
      this.currentEducation = value
    },
    getCurrentMember(value) {
      this.currentMember = value
    },
    resetAddProfileModal() {
      this.newAddProfile.staff_code = ''
      this.newAddProfile.kind = 'Nhân viên & Chuyên viên'
      this.newAddProfile.gender = 'Nam'
      this.newAddProfile.cccd_code = ''
      this.newAddProfile.cccd_date = ''
      this.newAddProfile.cccd_place = ''
      this.newAddProfile.cccd_address = ''
      this.newAddProfile.cccd_home = ''
      this.newAddProfile.bank_name = ''
      this.newAddProfile.bank_number = ''
      this.newAddProfile.personal_email = ''
      this.newAddProfile.bhxd_code = ''
      this.newAddProfile.taxt_code = ''
      this.newAddProfile.nation = ''
      this.newAddProfile.cccd_file = null
      this.newAddProfile.bhxh_file = null
    },
    resetEditProfileModal() {
      this.newEditProfile.staff_code = this.profile.staff_code
      this.newEditProfile.kind = this.profile.get_kind_display
      this.newEditProfile.gender = this.profile.get_gender_display
      this.newEditProfile.cccd_code = this.profile.cccd_code
      if(this.profile.cccd_date) this.newEditProfile.cccd_date = this.profile.cccd_date.split("/").reverse().join("-");
      else this.newEditProfile.cccd_date = ''
      this.newEditProfile.cccd_place = this.profile.cccd_place
      this.newEditProfile.cccd_address = this.profile.cccd_address
      this.newEditProfile.cccd_home = this.profile.cccd_home
      this.newEditProfile.bank_name = this.profile.bank_name
      this.newEditProfile.bank_number = this.profile.bank_number
      this.newEditProfile.personal_email = this.profile.personal_email
      this.newEditProfile.bhxd_code = this.profile.bhxd_code
      this.newEditProfile.taxt_code = this.profile.taxt_code
      this.newEditProfile.nation = this.profile.nation
      this.newEditProfile.cccd_file = null
      this.newEditProfile.bhxh_file = null
    },
    resetAddWorkStageModal() {
      this.newAddWorkStage.pre_date = ''
      this.newAddWorkStage.in_date = ''
      this.newAddWorkStage.out_date = ''
      this.newAddWorkStage.kind = this.workStageKindOptions[2]
      this.newAddWorkStage.cv_file = null
      this.newAddWorkStage.level_file = null
      this.newAddWorkStage.syll_file = null
      this.newAddWorkStage.ksk_file = null
      this.newAddWorkStage.hk_file = null
    },
    resetEditWorkStageModal() {
      if(this.currentWorkStage.pre_date) this.newEditWorkStage.pre_date = this.currentWorkStage.pre_date.split("/").reverse().join("-");
      else this.newEditWorkStage.pre_date = ''
      if(this.currentWorkStage.in_date) this.newEditWorkStage.in_date = this.currentWorkStage.in_date.split("/").reverse().join("-");
      else this.newEditWorkStage.in_date = ''
      if(this.currentWorkStage.out_date) this.newEditWorkStage.out_date = this.currentWorkStage.out_date.split("/").reverse().join("-");
      else this.newEditWorkStage.out_date = ''
      this.newEditWorkStage.kind = this.currentWorkStage.get_kind_display
      this.newAddWorkStage.cv_file = null
      this.newAddWorkStage.level_file = null
      this.newAddWorkStage.syll_file = null
      this.newAddWorkStage.ksk_file = null
      this.newAddWorkStage.hk_file = null
    },
    resetAddEducationModal() {
      this.newAddEducation.school = ''
      this.newAddEducation.major = ''
      this.newAddEducation.graduated_year = ''
      this.newAddEducation.degree = this.degreeOptions[3]
      this.newAddEducation.level = this.levelOptions[2]
      this.newAddEducation.level_file = null
    },
    resetEditEducationModal() {
      this.newEditEducation.school = this.currentEducation.school
      this.newEditEducation.major = this.currentEducation.major
      this.newEditEducation.graduated_year = this.currentEducation.graduated_year
      this.newEditEducation.degree = this.currentEducation.get_degree_display
      this.newEditEducation.level = this.currentEducation.get_level_display
      this.newEditEducation.level_file = null
    },
    resetAddMemberModal() {
      this.newAddMember.name = ''
      this.newAddMember.gender = this.genderOptions[0]
      this.newAddMember.birth_day = ''
      this.newAddMember.birth_file = null
    },
    resetEditMemberModal() {
      this.newEditMember.name = this.currentMember.name
      this.newEditMember.gender = this.currentMember.get_gender_display
      if(this.currentMember.birth_day) this.newEditMember.birth_day = this.currentMember.birth_day.split("/").reverse().join("-");
      else this.newEditMember.birth_day = ''
      this.newEditMember.birth_file = null
    },
    async handleAddProfileOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddProfileSubmit();
    },
    async handleEditProfileOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleEditProfileSubmit();
    },
    async handleDeleteProfileOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteProfileSubmit();
    },
    async handleAddWorkStageOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddWorkStageSubmit();
    },
     async handleEditWorkStageOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleEditWorkStageSubmit();
    },
    async handleDeleteWorkStageOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteWorkStageSubmit();
    },
    async handleAddEducationOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddEducationSubmit();
    },
    async handleEditEducationOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleEditEducationSubmit();
    },
    async handleDeleteEducationOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteEducationSubmit();
    },
    async handleAddMemberOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleAddMemberSubmit();
    },
    async handleEditMemberOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleEditMemberSubmit();
    },
    async handleDeleteMemberOK(bvModalEvt) {
      // Prevent modal from closing
      bvModalEvt.preventDefault();
      // Trigger submit handler
      await this.handleDeleteMemberSubmit();
    },
    async handleAddProfileSubmit() {
      try {
        let formData = new FormData();
        formData.append("staff_code", this.newAddProfile.staff_code);
        formData.append("kind", this.profileKindChoices[this.newAddProfile.kind]);
        formData.append("gender", this.genderChoices[this.newAddProfile.gender]);
        formData.append("cccd_code", this.newAddProfile.cccd_code);
        if (this.newAddProfile.cccd_date) formData.append("cccd_date", this.newAddProfile.cccd_date.split("-").reverse().join("/"));
        formData.append("cccd_place", this.newAddProfile.cccd_place);
        formData.append("cccd_address", this.newAddProfile.cccd_address);
        formData.append("cccd_home", this.newAddProfile.cccd_home);
        formData.append("bank_name", this.newAddProfile.bank_name);
        formData.append("bank_number", this.newAddProfile.bank_number);
        formData.append("personal_email", this.newAddProfile.personal_email);
        formData.append("bhxd_code", this.newAddProfile.bhxd_code);
        formData.append("taxt_code", this.newAddProfile.taxt_code);
        formData.append("nation", this.newAddProfile.nation);
        if (this.newAddProfile.cccd_file) formData.append("cccd_file", this.newAddProfile.cccd_file);
        if (this.newAddProfile.bhxh_file) formData.append("bhxh_file", this.newAddProfile.bhxh_file);
        formData.append("user", this.candidate.id);

        await this.$axios.post("/api/hr/profile/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add-profile");
        });
        await this.getInfo();
        this.$toast.success("Tạo thông tin chung thành công!", {
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
    async handleEditProfileSubmit() {
      try {
        let formData = new FormData();
        formData.append("staff_code", this.newEditProfile.staff_code);
        formData.append("kind", this.profileKindChoices[this.newEditProfile.kind]);
        formData.append("gender", this.genderChoices[this.newEditProfile.gender]);
        formData.append("cccd_code", this.newEditProfile.cccd_code);
        if (this.newEditProfile.cccd_date) formData.append("cccd_date", this.newEditProfile.cccd_date.split("-").reverse().join("/"));
        formData.append("cccd_place", this.newEditProfile.cccd_place);
        formData.append("cccd_address", this.newEditProfile.cccd_address);
        formData.append("cccd_home", this.newEditProfile.cccd_home);
        formData.append("bank_name", this.newEditProfile.bank_name);
        formData.append("bank_number", this.newEditProfile.bank_number);
        formData.append("personal_email", this.newEditProfile.personal_email);
        formData.append("bhxd_code", this.newEditProfile.bhxd_code);
        formData.append("taxt_code", this.newEditProfile.taxt_code);
        formData.append("nation", this.newEditProfile.nation);
        if (this.newEditProfile.cccd_file) formData.append("cccd_file", this.newEditProfile.cccd_file);
        if (this.newEditProfile.bhxh_file) formData.append("bhxh_file", this.newEditProfile.bhxh_file);

        await this.$axios.patch("/api/hr/profile/" + this.profile.id + '/', formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-edit-profile");
        });
        await this.getInfo();
        this.$toast.success("Cập nhật thông tin chung thành công!", {
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
    async handleDeleteProfileSubmit() {
      try {
        let url = "/api/hr/profile/" + this.profile.id + '/'
        await this.$axios.delete(url);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete-profile");
        });
        await this.getInfo();
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
    async handleAddWorkStageSubmit() {
      try {
        let formData = new FormData();
        if (this.newAddWorkStage.pre_date) formData.append("pre_date", this.newAddWorkStage.pre_date.split("-").reverse().join("/"));
        if (this.newAddWorkStage.in_date) formData.append("in_date", this.newAddWorkStage.in_date.split("-").reverse().join("/"));
        if (this.newAddWorkStage.out_date) formData.append("out_date", this.newAddWorkStage.out_date.split("-").reverse().join("/"));
        formData.append("kind", this.workStageKindChoices[this.newAddWorkStage.kind]);
        if (this.newAddWorkStage.cv_file) formData.append("cv_file", this.newAddWorkStage.cv_file);
        if (this.newAddWorkStage.level_file) formData.append("level_file", this.newAddWorkStage.level_file);
        if (this.newAddWorkStage.syll_file) formData.append("syll_file", this.newAddWorkStage.syll_file);
        if (this.newAddWorkStage.ksk_file) formData.append("ksk_file", this.newAddWorkStage.ksk_file);
        if (this.newAddWorkStage.hk_file) formData.append("hk_file", this.newAddWorkStage.hk_file);
        formData.append("profile", this.profile.id);

        await this.$axios.post("/api/hr/work-stage/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add-work");
        });
        await this.getInfo();
        this.$toast.success("Tạo mới giai đoạn làm việc thành công!", {
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
    async handleEditWorkStageSubmit() {
      try {
        let formData = new FormData();
        if (this.newEditWorkStage.pre_date) formData.append("pre_date", this.newEditWorkStage.pre_date.split("-").reverse().join("/"));
        if (this.newEditWorkStage.in_date) formData.append("in_date", this.newEditWorkStage.in_date.split("-").reverse().join("/"));
        if (this.newEditWorkStage.out_date) formData.append("out_date", this.newEditWorkStage.out_date.split("-").reverse().join("/"));
        formData.append("kind", this.workStageKindChoices[this.newEditWorkStage.kind]);
        if (this.newEditWorkStage.cv_file) formData.append("cv_file", this.newEditWorkStage.cv_file);
        if (this.newEditWorkStage.level_file) formData.append("level_file", this.newEditWorkStage.level_file);
        if (this.newEditWorkStage.syll_file) formData.append("syll_file", this.newEditWorkStage.syll_file);
        if (this.newEditWorkStage.ksk_file) formData.append("ksk_file", this.newEditWorkStage.ksk_file);
        if (this.newEditWorkStage.hk_file) formData.append("hk_file", this.newEditWorkStage.hk_file);

        await this.$axios.patch("/api/hr/work-stage/" + this.currentWorkStage.id + '/', formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-edit-work");
        });
        await this.getInfo();
        this.$toast.success("Cập nhật giai đoạn làm việc thành công!", {
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
    async handleDeleteWorkStageSubmit() {
      try {
        let url = "/api/hr/work-stage/" + this.currentWorkStage.id + '/'
        await this.$axios.delete(url);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete-work");
        });
        await this.getInfo();
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
    async handleAddEducationSubmit() {
      try {
        let formData = new FormData();
        formData.append('school', this.newAddEducation.school)
        formData.append('major', this.newAddEducation.major)
        formData.append('graduated_year', this.newAddEducation.graduated_year)
        formData.append("degree", this.degreeChoices[this.newAddEducation.degree]);
        formData.append("level", this.levelChoices[this.newAddEducation.level]);
        if (this.newAddEducation.level_file) formData.append('level_file', this.newAddEducation.level_file)
        formData.append("profile", this.profile.id);

        await this.$axios.post("/api/hr/education/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add-education");
        });
        await this.getInfo();
        this.$toast.success("Tạo mới bằng cấp thành công!", {
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
    async handleEditEducationSubmit() {
      try {
        let formData = new FormData();
        formData.append('school', this.newEditEducation.school)
        formData.append('major', this.newEditEducation.major)
        formData.append('graduated_year', this.newEditEducation.graduated_year)
        formData.append("degree", this.degreeChoices[this.newEditEducation.degree]);
        formData.append("level", this.levelChoices[this.newEditEducation.level]);
        if (this.newEditEducation.level_file) formData.append('level_file', this.newEditEducation.level_file)

        await this.$axios.patch("/api/hr/education/" + this.currentEducation.id + '/', formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-edit-education");
        });
        await this.getInfo();
        this.$toast.success("Cập nhật bằng cấp thành công!", {
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
    async handleDeleteEducationSubmit() {
      try {
        let url = "/api/hr/education/" + this.currentEducation.id + '/'
        await this.$axios.delete(url);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete-education");
        });
        await this.getInfo();
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
    async handleAddMemberSubmit() {
      try {
        let formData = new FormData();
        formData.append('name', this.newAddMember.name)
        formData.append("gender", this.genderChoices[this.newAddMember.gender]);
        if (this.newAddMember.birth_day) formData.append("birth_day", this.newAddMember.birth_day.split("-").reverse().join("/"));
        if (this.newAddMember.birth_file) formData.append('birth_file', this.newAddMember.birth_file)
        formData.append("profile", this.profile.id);

        await this.$axios.post("/api/hr/family-member/create/", formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-add-member");
        });
        await this.getInfo();
        this.$toast.success("Tạo mới thành viên trong gia đình thành công!", {
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
    async handleEditMemberSubmit() {
      try {
        let formData = new FormData();
        formData.append('name', this.newEditMember.name)
        formData.append("gender", this.genderChoices[this.newEditMember.gender]);
        if (this.newEditMember.birth_day) formData.append("birth_day", this.newEditMember.birth_day.split("-").reverse().join("/"));
        if (this.newEditMember.birth_file) formData.append('birth_file', this.newEditMember.birth_file)

        await this.$axios.patch("/api/hr/family-member/" + this.currentMember.id + '/', formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        });

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-edit-member");
        });
        await this.getInfo();
        this.$toast.success("Cập nhật thành viên trong gia đình thành công!", {
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
    async handleDeleteMemberSubmit() {
      try {
        let url = "/api/hr/family-member/" + this.currentMember.id + '/'
        await this.$axios.delete(url);

        // Hide the modal munally
        this.$nextTick(() => {
          this.$bvModal.hide("modal-delete-member");
        });
        await this.getInfo();
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
    async getCandidate() {
      try {
        let response = await this.$axios.get('/api/candidate/' + this.candidateId + '/')
        this.candidate = response.data
        console.log('dataa  ', response.data)
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
