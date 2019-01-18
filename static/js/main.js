new Vue({
    el: '#app',
	delimiters: ['[[',']]'],
	mounted () {
		var _self = this;
		axios
		  .get('getrecord')
		  .then(function(res){
			  console.log(res.data);
			  _self.tableData = res.data;
		  }
		  
		  )
    },
    data:  {	
          tableData: "",
		  editForm: {
			  ID: '',
			  MAC: '',
			  COMMENT: '',
			  POS: ''
			},
			editFormVisible: false,
			newFormVisible: false,
			newForm: {
			  ID: '',
			  MAC: '',
			  COMMENT: '',
			  POS: ''
			},
			formLabelWidth: '180px'
			
	},
	methods: {
		msgNotify: function (id,row) {
			alert(id)
			console.log(row.ID)
		},
		rowDelete: function (id,row) {
			this.tableData.splice(id,1)
			console.log(this.tableData)
		},
		rowSave: function (row) {
			console.log(this.tableData)
			this.editFormVisible = false
		},
		msgDelete: function (id,row) {
			this.$confirm('删除该MAC地址, 是否继续?', '提示', {
			  confirmButtonText: '确定',
			  cancelButtonText: '取消',
			  type: 'warning'
			}).then(() => {
				this.rowDelete(id,row),
			  this.$message({
				type: 'success',
				message: '删除成功!'
			  });
			}).catch(() => {
			  this.$message({
				type: 'info',
				message: '已取消删除'
			  })          
			})
		  },
		msgEdit: function (id,row) {
			this.editFormVisible = true,
			this.editForm = row
		  },
		newrecord: function () {
			this.newFormVisible = true
		  },
		newSave: function (row) {
			this.newForm.ID = this.tableData.length + 1,
			this.newForm.MAC = row.MAC,
			this.newForm.POS = row.POS,
			this.newForm.COMMENT = row.COMMENT,
			this.tableData.push(this.newForm),
			this.newFormVisible = false
		  },  
		savetofile: function () {
			axios.post('setrecord', this.tableData).then(function (response) {
				//this.saveNotify()
				console.log(response)
				alert('保存成功')
            })
		},
		saveNotify: function () {
			this.$alert('保存成功', 'Success', {
			  confirmButtonText: '确定',
			}).then(() => {
			  this.$message({
				type: 'success',
				message: '删除成功!'
			  })
			})
		}
	}
})



