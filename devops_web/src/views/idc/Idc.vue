<template>
    <el-card class="box-card">
        <div class="table-header">
            <div>
                <el-input style="width:150px"></el-input>
                <el-button>搜索</el-button>
            </div>

            <div>
                <el-button type="primary" @click="createDialogVisible=true"><el-icon><plus /></el-icon>&nbsp;创建</el-button>
                <!--展出弹出框-->
            </div>
        </div>

        <!--数据表-->
        <el-table :data="tableData" :border=true style="width: 100%" :header-cell-style="{background: '#F0F2F5'}">
            <el-table-column prop="name" label="机房名" width="180"></el-table-column>
            <el-table-column prop="city" label="城市" width="180" v-if="showColumn.city"></el-table-column>
            <el-table-column prop="provider" label="运营商" v-if="showColumn.provider"></el-table-column>
            <el-table-column prop="note" label="备注" v-if="showColumn.note"></el-table-column>
            <el-table-column prop="create_time" label="创建时间" v-if="showColumn.create_time"></el-table-column>

            <!--操作栏-->
            <el-table-column fixed="right" label="操作" width="150">
                <template #default="scope">
                    <el-button type="primary" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
                    <el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
                </template>
            </el-table-column>
        </el-table>
    </el-card>

    <IdcCreate v-model:visible="createDialogVisible"></IdcCreate>
    <IdcEdit v-model:visible="editDialogVisible" :row="row"></IdcEdit>
</template>

<script>
import IdcEdit from './IdcEdit'
import IdcCreate from './IdcCreate'
export default {
    data() {
        return {
            tableData: [],
            total: 0,
            showColumn: {
                'name': true,
                'city': true,
                'provider': true,
                'note': true,
                'create_time': true
            },
            urlParams: {
                page_num: 1,
                page_size: 10,
                search: ''
            },
            createDialogVisible: false,
            editDialogVisible: false,
            row: ''
        }
    },
    methods: {
        getData() {
            this.$http.get('/cmdb/idc/', {params: this.urlParams}).then(
                res=>{
                    this.tableData = res.data.data;
                    this.total = res.data.count;
                }
            )
        },
        handleEdit(index, row){
            this.editDialogVisible = true
            this.row = row
        },
        handleDel(index, row){
            this.$confirm("你确定要删除选中的吗?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning"
            }).then(()=>{
                this.$http.delete('/cmdb/idc/' + row.id + '/').then(res=>{
                    if(res.data.code==200){
                        this.$message.success("删除成功")
                        this.tableData.splice(index, 1)
                    } else {
                        this.$message.error(res.data.msg);
                    }
                })
            }).catch(()=>{
                this.$message({
                    type:'info',
                    message:'已取消操作'
                })
            })
        }
    },
    mounted() {
        this.getData();
    },
    components: {
        IdcEdit,
        IdcCreate
    }
}
</script>

<style scoped>
.table-header {
    display: flex;
    margin-bottom: 18px;
    justify-content: space-between;
}
</style>