<template lang="html">
	  <div class="header">
			<ul class="header-ul">
				<li class="header-ul-li"><a href="#/">首页</a></li>
				<li class="header-ul-li"><a href="#/blog">博客</a></li>
				<li class="header-ul-li"><a href="#">常见问题</a></li>
				<li class="header-ul-li"><a href="#">工具</a></li>
				<li class="header-ul-li"><a href="#">反馈</a></li>
			</ul>
		</div>
</template>

<script>
export default {
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
