new Vue({
    el: '#app',
	mounted () {
		var _self = this;
		axios
		  .get('getrecord')
		  .then(function(res){
			  console.log(res.data);
			  _self.tableData = res.data;
			  //console(_self.tableData);
		  }
		  
		  )
    },
    data:  {	
          tableData: ""
	},
	methods: {
		//var msg = this.tableData;
		saymsg: function (msg) {
			alert(this.tableData)
		},
		update: function () {
			 axios.post('setrecord', this.tableData).then(function (response) {
                    console.log(response);
                  })
		},

	}
})


