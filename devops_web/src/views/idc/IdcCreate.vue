<template>
    <el-dialog
        :model-value="visible"
        title="创建机房"
        @close="dialogClose"
        width="30%">
        <el-form :model="form" label-width="100px">
            <el-form-item label="机房名称:" prop="name"><el-input v-model="form.name"></el-input></el-form-item>
            <el-form-item label="城市:" prop="city"><el-input v-model="form.city"></el-input></el-form-item>
            <el-form-item label="运营商:" prop="provider"><el-input v-model="form.provider"></el-input></el-form-item>
            <el-form-item label="备注:" prop="note"><el-input v-model="form.note" type="textarea"></el-input></el-form-item>
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
        name: "IdcCreate",
        props: {
            visible: Boolean,
        },
        data() {
            return {
                form: {
                    'name': '',
                    'city': '',
                    'provider': '',
                    'note': ''
                }
            }
        },
        methods: {
            dialogClose(){
                this.$emit('update:visible', false)
            },
            submit(){
                this.$http.post('/cmdb/idc/', this.form).then(res=>{
                    if(res.data.code == 200) {
                        this.$message.success("创建成功")
                        this.$parent.getData()
                        this.dialogClose()
                    } else {
                        this.$message.error(res.data.msg)
                    }
                })
            }
        }
    }
</script>

<style lang="scss" scoped>

</style>