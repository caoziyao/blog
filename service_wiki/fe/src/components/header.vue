<template lang="html">
	  <div class="header">
			<ul class="header-ul">
				<li class="header-ul-li"><a href="#/">首页</a></li>
				<li class="header-ul-li"><a href="#/blog">博客</a></li>
				<li class="header-ul-li"><a href="#/book">书架</a></li>
				<li class="header-ul-li" v-on:click="loadNode"><a href="#">常见问题</a></li>
				<li class="header-ul-li">
					<el-dropdown>
					  <span class="el-dropdown-link">
					    <a href="#">工具</a><i class="el-icon-arrow-down el-icon--right"></i>
					  </span>
					  <el-dropdown-menu slot="dropdown">
					    <el-dropdown-item>1</el-dropdown-item>
					    <el-dropdown-item>2</el-dropdown-item>
					    <el-dropdown-item>3</el-dropdown-item>
					    <el-dropdown-item disabled>4</el-dropdown-item>
					    <el-dropdown-item divided>5</el-dropdown-item>
					  </el-dropdown-menu>
					</el-dropdown>
				</li>

				<li class="header-ul-li"><a href="#/feedback">反馈</a></li>
				<li class="header-ul-li"><a href="#/todo">Todo</a></li>
				<li class="header-ul-li"><a href="#/mznv">图片</a></li>
				<li class="header-ul-li"><a href="#/music">音乐</a></li>
			</ul>
		</div>
</template>

<script>
export default {
	methods: {
		loadNode: function() {
			console.log('logannnn')
			this.$emit('logannnn', 'content')
		}
	}
}
</script>

<style lang="css">
	.container {
		width: 970px;
		margin: 0 auto;
	}

	.header {
		/*margin: 0 auto;*/
		/*width: 970px;*/
		/*min-height: 50px;*/
		margin-top: 20px;
		/*background-color: #fff;*/
		color: #333;
		/*line-height: 60px;*/
		border-color: #e7e7e7;
		border-radius: 4px;
    border: 1px solid transparent;
		background: #f6f6f6;
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
