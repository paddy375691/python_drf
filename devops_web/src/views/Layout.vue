<template>
    <div class="common-layout">
        <el-container>
            <el-aside :width="isCollapse ? '64px' : '200px'">
                <!-- 侧边栏 -->
                 <el-menu 
                    class="el-menu-vertical"
                    background-color="#304156"
                    text-color="#FFFFFF"
                    active-text-color="#ffd04b"
                    :default-active="this.$route.path"
                    router
                    unique-opened
                    :collapse="isCollapse"
                    :collapse-transition="false"
                    >
                    <div class="logo-title">Devops</div>
                    <template v-for="menu in this.$router.options.routes" :key="menu">
                        <el-menu-item v-if="menu.path=='/'" :index="menu.children[0].path">
                            <el-icon><component :is="menu.children[0].icon"></component></el-icon>
                            <span>{{ menu.children[0].name }}</span>
                        </el-menu-item>

                        <el-sub-menu v-else-if="menu.children" :index="menu.path">
                            <template #title>
                                <el-icon><component :is="menu.icon"></component></el-icon>
                                <span>{{ menu.name }}</span>
                            </template>
                            <!--生成二级菜单-->
                            <el-menu-item v-for="child in menu.children" :key="child" :index="child.path">{{ child.name }}</el-menu-item>
                        </el-sub-menu>
                    </template>
                </el-menu>
            </el-aside>
            <el-container>
                <el-main>
                    <router-view></router-view>
                </el-main>
            </el-container>

        </el-container>
    </div>
</template>

<script>
    export default {
        data(){
            return {
                isCollapse: false
            }
        }   
    }
</script>

<style scoped>
.common-layout,.el-container, .el-menu-vertical{
    height: 100%;
}
.el-main {
    background: #f5f5f5;
}
</style>