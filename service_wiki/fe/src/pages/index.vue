<template lang="html">
	<div class="container">
		<qui-header class="qui-header"></qui-header>

		  <div class="main">

				<h2>Bad luck, U come here.</h2>
				<el-input v-model="input"  placeholder="请输入内容"  @keydown.enter.native="keySearch" clearable>
					<el-button slot="append"
						icon="el-icon-search"
						v-on:click="googleSearch">
					</el-button>
				</el-input>
				<p>google it: {{ input }}</p>
			</div>
	</div>

</template>

<script>
	import quiHeader from '../components/header.vue'
export default {
	components: {
		'qui-header': quiHeader,
	},
	data() {
	 return {
		 input: '',
		 searchType: '',
	 }
 },
	methods: {
		googleSearch() {
			 let url = 'https://www.google.com/search?q=' + this.input
			//  window.location.href = url
			window.open(url, '_blank');
		},
		keySearch(event) {
			this.googleSearch()
		},
	},
	created() {

	}

}
</script>

<style lang="css" scoped>

	.container {
		width: 970px;
		margin: 0 auto;
	}

	.main {
		text-align: center;
	}

	.header {
		/*margin: 0 auto;*/
		/*width: 970px;*/
		/*min-height: 50px;*/
		margin-top: 20px;
		background-color: #fff;
		color: #333;
		/*line-height: 60px;*/
		border-color: #e7e7e7;
		border-radius: 4px;
    border: 1px solid transparent;
	}

	.header-ul {
		display: -webkit-flex; /* Safari */
  	display: flex;
		height: 50px;
		align-items: center;
		margin-top: 0px;
		margin-bottom: 0px;
	}

	.header-ul-li {
		/*float: left;*/
		margin-left: 10px;
		margin-right: 10px;
		list-style-type: none;
		line-height: 50px;
	}

</style>
