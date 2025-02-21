<template>
    <el-dialog
        :model-value="visible"
        title="修改机房信息"
        @close="dialogClose"
        width="30%">
        <el-form :model="row" label-width="100px">
            <el-form-item label="机房名称" prop="name"><el-input v-model="row.name"></el-input></el-form-item>
            <el-form-item label="城市:" prop="city"><el-input v-model="row.city"></el-input></el-form-item>
            <el-form-item label="运营商:" prop="provider"><el-input v-model="row.provider"></el-input></el-form-item>
            <el-form-item label="备注:" prop="note"><el-input v-model="row.note" type="textarea"></el-input></el-form-item>
        </el-form>

        <template #footer>
            <span class="dialog-footer">
                <el-button @click="dialogClose">取消</el-button>
                <el-button type="primary" @click="submit">确定</el-button>
            </span>
        </template>
    </el-dialog>
</template>

<script>

export default {
    name: "IdcEdit",
    props: {
        visible: Boolean,
        row: ''
    },
    data() {
        return {

        }
    },
    methods: {
        dialogClose() {
            this.$emit('update:visible', false) // 关闭组件
        },
        submit() {
            this.$http.put('/cmdb/idc/' + this.row.id + '/', this.row).then(
                res=>{
                    if(res.data.code == 200) {
                        this.$message.success("修改成功")
                        this.dialogClose()
                    } else {
                        this.$message.error(res.data.msg)
                    }
                }
            )
        }
    }

}
</script>

<style scoped>

</style>