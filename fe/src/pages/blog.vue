<template lang="html">
	<div class="container">
		<qui-header class="qui-header" v-on:logannnn="logFun"></qui-header>
		<div class="bar"></div>
		<el-container class="">
	  	<el-aside width="200px">
				<qui-tree class="qui-tree" :model="treeData"></qui-tree>
			</el-aside>

			<div class="span-border"></div>
	  	<el-main>
				<ul class="list-group" v-on:mouseover="mouseOver" v-on:mouseout="mouseOut">
					<li class="list-group-item"><a href="#">12</a></li>
					<li class="list-group-item"><a href="#">2222</a></li>
					<li class="list-group-item"><a href="#">3333</a></li>
					<li class="list-group-item"><a href="#">44444</a></li>
				</ul>
				<div class="">
					{{ content }}
				</div>
			</el-main>
		</el-container>

	</div>
</template>

<script>
import bus from '../assets/eventBus'
import quiHeader from '../components/header.vue'
import quiTree from '../components/tree.vue'
export default {
	components: {
		'qui-header': quiHeader,
		'qui-tree': quiTree,
	},
	data() {
		var data = {
			name: 'notebook',
			isFolder: true,
			children: [
				{
						name: 'hell',
						isFolder: false,
				},
				{
						name: 'abccd',
						isFolder: true,
						children: [],
				},
			],
		};
		return {
			treeData: data,
			isActive: false,
			content: '',
      props: {
         label: 'name',
         children: 'zones',
         isLeaf: 'leaf'
       },
     };
 	},
	mounted() {
		let self = this
		bus.$on('showTreeContent', (msg) => {

			self.content = msg
			console.log('getdata', msg)
		})
	},
	 methods: {
		 logFun(data) {
			 console.log('abdb', data)
		 },
		 mouseOver(event) {
			 let target = event.target
			 if (target.localName == 'li') {
				 target.classList.add('active')
			 }
		 },
		 mouseOut(event) {
			 let target = event.target
			 if (target.localName == 'li') {
 				 target.classList.remove('active')
 			 }
		 },
		 getListDir: function () {
			 let url = '/api/tree/get_tree_root'
			 // JSON.stringify(body)
			 this.axios.get(url).then((res) => {

				 let data = res.data

				 console.log('res',  typeof data, data )
				 this.treeData = data
				 // for (let i = 0; i < data.length; i++) {
				 // 	let item = data[i]
				 // 	this.updateTreeModel(item)
				 // }
			 }).catch((res) => {
				 console.log('res', res)
			 })
		 },
	 },
	 created(){
      this.log('hellcrewate')
 			let root = '/Users/cczy/yun/wiki/notebook'
 			this.getListDir()
   }
}
</script>

<style lang="css">

	.qui-header {
		background: #f6f6f6;
	}

	.qui-tree {
	  cursor: pointer;
	}

	.active {
		background: #ddd;
	}

	.bar {
		height: 20px;
		background: #fff;
	}

	.span-border {
		height: 90px;
		width: 0px;
		border: 1px solid #fff;
	}

	.el-tree {
		background: #f6f6f6;
	}

	.container {
		/*width: 970px;*/
		margin: 0 auto;
		background: #f6f6f6;
	}


	/* list-group */
	.list-group {
		border-radius: 4px;
		box-shadow: 0 1px 2px rgba(0,0,0,.075);
	}

	.list-group-item {
		/*position: relative;*/
    display: block;
    padding: 10px 15px;
    /*margin-bottom: -1px;*/
    /*background-color: #fff;*/
    /*border: 1px solid #ddd;*/
		border-bottom: 1px solid #ddd;
	}

	.el-container {

	}
</style>
