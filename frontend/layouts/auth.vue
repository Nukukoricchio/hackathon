<script>
/**
 * Auth-layout
 */
export default {
    data() {
        return {

        }
    },
}
</script>

<template>
<div>
    <div class="account-pages mt-5 mb-5">
        <div class="container">
            <Nuxt />
        </div>
        <!-- end container -->
    </div>
    <!-- end page -->
    <footer class="footer footer-alt">
        {{new Date().getFullYear()}} &copy; Yody
    </footer>
</div>
</template>
