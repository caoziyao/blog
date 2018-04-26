<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>
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
			</el-main>
		</el-container>

	</div>
</template>

<script>
import quiHeader from '../components/header.vue'
import quiTree from '../components/tree.vue'
export default {
	components: {
		'qui-header': quiHeader,
		'qui-tree': quiTree,
	},
	data() {
		var data = {
			name: 'My Tree',
			children: [
				 { name: 'hello' },
				 { name: 'wat' },
				 {
      		name: 'child folder',
					children: [
						{ name: 'hello2' },
	 				  { name: 'wat2' },
					]
				}
			],
		};
		return {
			treeData: data,
			isActive: false,
      props: {
         label: 'name',
         children: 'zones',
         isLeaf: 'leaf'
       },
     };
 	},
	 methods: {
		 getTree: function() {
			 const log = this.
			 log('aaaa')
			 this.axios.get('/api/get/tree').then( (response) => {
 		    console.log(response);
 		  })
 		  .catch( (error) => {
 		    console.log(error);
 		  });
		 },


		 loadNode: function(node, resolve) {
			 const log = this.log

			 if (node.level === 0) {
				 return resolve([{ name: 'wiki' }]);
			 } else {
				 setTimeout(() => {
					 const data = [{
						 name: 'leaf',
						 leaf: true
					 }, {
						 name: 'zone'
					 }];
					 this.getTree();

					 resolve(data);
				 }, 500);
			 }


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

		 }
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
