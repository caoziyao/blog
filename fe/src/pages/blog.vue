<template lang="html">
	<div class="container">
		<el-row>
		  <el-col :span="16">
				<qui-header class="qui-header" v-on:logannnn="logFun"></qui-header>
			</el-col>
		  <el-col :span="8">
				<el-input
					placeholder="search"
					suffix-icon="el-icon-search"
					v-model="searchData"
					v-on:input="search">
				</el-input>
			</el-col>
		</el-row>

		<div class="bar"></div>
		<el-container class="">
	  	<el-aside width="200px">
				<qui-tree class="qui-tree" :model="treeData"></qui-tree>
			</el-aside>

			<div class="span-border"></div>
	  	<el-main>
				 <a href="#/edit"><el-button v-if="content" v-on:click="editContent()" icon="el-icon-edit" circle></el-button></a>
				<!-- <ul class="list-group" v-on:mouseover="mouseOver" v-on:mouseout="mouseOut">
					<li class="list-group-item"><a href="#">12</a></li>
					<li class="list-group-item"><a href="#">2222</a></li>
					<li class="list-group-item"><a href="#">3333</a></li>
					<li class="list-group-item"><a href="#">44444</a></li>
				</ul> -->
					<div v-html="content"></div>
			</el-main>
		</el-container>

	</div>
</template>

<script>
import Remarkable from 'remarkable';
import bus from '../assets/eventBus'
import quiHeader from '../components/header.vue'
import quiTree from '../components/tree.vue'
export default {
	components: {
		'qui-header': quiHeader,
		'qui-tree': quiTree,
	},
	data() {
		var data = {};
		return {
			searchData: '',
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
	// html 挂载到页面上执行的函数，只执行一次
	mounted() {
		let self = this
		bus.$on('showTreeContent', (ret) => {
			let content = ret.content

			let md = new Remarkable();
			let m = md.render(content)
			self.content = m

			// update store
			this.$store.commit('updateNoteData', ret)
			// console.log('store', this.$store.state.noteData)
		})
	},
	 methods: {
		 logFun(data) {
			 console.log('logFun', data)
		 },
		 editContent(path) {
			 console.log('abdb', path)
		 },
		 search() {
			 // search
			 console.log(this.searchData)
		 },
		 initTree: function () {
			 let url = '/api/tree/get_tree_root'
			 // JSON.stringify(body)
			 this.axios.get(url).then((res) => {
					console.log('reeee', res)
				 let data = res.data
				 if (data) {
					 if (data.code === 401) {
						 // 页面跳转
						 this.$router.push({path:'/login'})
					 } else {
						 this.treeData = data
					 }
					// this.$store.commit('saveTreeData', data)
					//  this.treeData = data
				 }
			 }).catch((res) => {
				 console.log('res', res)
			 })
		 },
	 },
	 created(){

      this.log('hellcrewate')
 			let root = '/Users/cczy/yun/wiki/notebook'
			this.initTree()
   }
}
</script>

<style lang="css" scroped>

	.qui-tree {
	  cursor: pointer;
	}

	.el-input {
		position: relative;
		/*top: 32px;*/
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
