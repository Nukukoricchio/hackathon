function checkRoleName(role_list, role_name) {
  for (let role of role_list) {
    if (role.role_acronym_name.includes(role_name)) {
      return true
    }
  }
  return false
}

export default async function ({ store, redirect, app }) {
  let user = store.$auth.user
  if (user) {
    if (!(user.is_superuser || checkRoleName(user.role, 'hc-ns'))) {
      app.$toast.clear()
      app.$toast.error('Bạn không có quyền truy cập trang web này!', {
        icon: 'alert'
      })
      await store.$auth.logout();
    }
  }
}
  